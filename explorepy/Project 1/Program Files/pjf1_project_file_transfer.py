import pandas as pd
import psycopg2
import random
import json
import boto3 
from io import BytesIO
from datetime import datetime

connect_todb = psycopg2.connect(
    host = 'localhost',
    database = 'zishta2024dump',
    user = 'postgres',
    password = 'log',
    port = 5432
)
schema = 'zishta2024'
extract_query = connect_todb.cursor()
# Company details
extract_query.execute(f"""select * from {schema}.company""")
comapany =  extract_query.fetchall()
columns = [desc[0] for desc in extract_query.description]
Comp_details = pd.DataFrame(comapany ,columns=columns)
#Branch Details
extract_query.execute(f"""select branchid,cancel,branchname,branchaddress,branchphone,active,companyname,country,state,city,pincode,tinno from {schema}.branch""")
branch =  extract_query.fetchall()
columns = [desc[0] for desc in extract_query.description]
branch_details = pd.DataFrame(branch ,columns=columns)
#  Location Details
extract_query.execute(f"""select locationid,cancel,companyname,branch,locationcode,locationname,active from {schema}.location""")
location =  extract_query.fetchall()
columns = [desc[0] for desc in extract_query.description]
location_details = pd.DataFrame(location ,columns=columns)
#  Item Details
extract_query.execute(f""" select itemid,itemdesc, itemcode, item_hsn,taxrate, active, itemname, sellingunit, 
                      stdcost, mrp, zishtaitemcode, comboitem, stdsellingprice from {schema}.item a """)
items = extract_query.fetchall()
columns = [desc[0] for desc in extract_query.description]
item_df = pd.DataFrame(items ,columns=columns)
# customer details
extract_query.execute(f"""select a.mobileno,a.customer_name,
                      a.branchid,a.locationid,a.daddress,a.dcountry,a.dstate,a.dcity,a.dpincode 
                      from {schema}.retail_customer a where a.mobileno is not null and a.mobileno not in ('0','')""")
customers_data = extract_query.fetchall()
cust_columns = [desc[0] for desc in extract_query.description]
cust_data= pd.DataFrame(customers_data,columns=cust_columns)
# print(len(cust_data))

# Creating a order details and push to s3
order_columns =['itemid','itemdesc', 'itemcode',"order_qty",'mrp','salesorder_id']
order_items_df = pd.DataFrame(columns=columns)

with open(r'C:\Users\user\pythontest\explorepy\Project 1\DataSet\email_pwd.json','r') as json_file:
    json_data = json.load(json_file)
last_orderno,last_seriesno = json_data['Details'][0]['orderno'],json_data['Details'][0]['item_sequw']
 
rand_customers_index = random.sample(range(len(cust_data)), random.randint(90, 120))
rand_customers = cust_data.iloc[rand_customers_index].copy()
 # Update 'Orderno' and 'salesorder_id' columns using .loc to avoid warnings 

rand_customers.loc[:, 'Orderno'] = [last_orderno + ordnum for ordnum in range(1, len(rand_customers_index) + 1)] 
rand_customers.loc[:, 'salesorder_id'] = [last_seriesno + ordnum for ordnum in range(len(rand_customers_index))]

# print(rand_customers)
# creating random order items.
item_df = item_df[['itemid','itemdesc', 'itemcode','mrp']]
order_item_list  = pd.DataFrame(columns=['itemid','itemdesc', 'itemcode',"order_qty",'mrp','salesorder_id'])
for noof_order in rand_customers['salesorder_id']:
    noof_items_prorder = random.randint(1,10)
    random_items = random.sample(range(len(item_df)),noof_items_prorder)
    orders_list = {'itemid':[item_df['itemid'].iloc[k] for k in random_items],
                   'itemdesc':[item_df['itemdesc'].iloc[k] for k in random_items],
                    'itemcode':[item_df['itemcode'].iloc[k] for k in random_items],
                    "order_qty":[random.randint(1,8) for _ in range(0,len(random_items))],
                    'mrp':[item_df['mrp'].iloc[k] for k in random_items],
                    'salesorder_id':[noof_order] * len(random_items)}
    orders_list = pd.DataFrame(orders_list)
    order_item_list = pd.concat([order_item_list,orders_list],ignore_index=True)
    # break
json_data['Details'][0]['orderno'] += len(rand_customers_index)
json_data['Details'][0]['item_sequw'] += len(rand_customers_index)

with open(r'C:\Users\user\pythontest\explorepy\Project 1\DataSet\email_pwd.json', 'w') as file: 
    json.dump(json_data, file, indent=4)

buffer = BytesIO() 
# Create a Pandas Excel writer using the XlsxWriter as the engine. 
with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer: 
    rand_customers.to_excel(writer, sheet_name='OrderedCustomer', index=False) 
    order_item_list.to_excel(writer, sheet_name='ItemsOrdered', index=False) 
# Ensure the buffer is set to the beginning 
buffer.seek(0) 
# Initialize the boto3 client 
s3_client = boto3.client('s3') 
# Upload the file to S3 
file_name = f"new_orders_{datetime.now().strftime('%d%m%y%H%M%S')}.xlsx"
s3_client.upload_fileobj(buffer, 'zishtacoretransit-process', file_name) 


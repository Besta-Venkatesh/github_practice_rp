from faker import Faker
import pandas as pd
import psycopg2
import random
import json
import boto3 
import io
# from io import BytesIO
from datetime import datetime , timezone, timedelta 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from cryptography.fernet import Fernet
import time

success_msg =f""" 
Dear Asperients, 

I am pleased to inform you that the job has been successfully executed at {datetime.now().strftime('%d-%m-%y %H:%M:%S')}. 
Thankyou.

Best regards, 
Venkatesh. """

Failure_message =f""" 
Dear Asperients, 

Job Has Been interepeted due to unexpected error Pls provide your atmost attencsion at {datetime.now().strftime('%d-%m-%y %H:%M:%S')}.
Thankyou. 

Best regards, 
Venkatesh. """

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

try:
    with open(r'C:\Users\user\pythontest\explorepy\Project 1\DataSet\email_pwd.json','r') as json_file:
        json_data = json.load(json_file) 
    last_orderno,last_seriesno = json_data['Details'][0]['orderno'],json_data['Details'][0]['item_sequw']
    
    rand_customers_index = random.sample(range(len(cust_data)), random.randint(90, 120))
    rand_customers = cust_data.iloc[rand_customers_index].copy()
    # Update 'Orderno' and 'salesorder_id' columns using .loc to avoid warnings 
    fake = Faker()
    start_date = datetime.now() - timedelta(hours= 24)
    end_date = datetime.now()
    rand_customers.loc[:, 'orderno'] = [last_orderno + ordnum for ordnum in range(1, len(rand_customers_index) + 1)] 
    rand_customers.loc[:, 'salesorder_id'] = [last_seriesno + ordnum for ordnum in range(1,len(rand_customers_index) + 1)]
    rand_customers.loc[:, 'docdate'] = sorted([fake.date_time_between_dates(start_date,end_date) for _ in range( len(rand_customers_index))])
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

    json_data['Details'][0]['orderno'] += len(rand_customers_index)
    json_data['Details'][0]['item_sequw'] += len(rand_customers_index)

    with open(r'C:\Users\user\pythontest\explorepy\Project 1\DataSet\email_pwd.json', 'w') as file: 
        json.dump(json_data, file, indent=4)

    # to keep the buffer open for further use file creation has kept in the function.
    def generate_excel_buffer(rand_customers,order_item_list):
        buffer = io.BytesIO() 
        # Create a Pandas Excel writer using the XlsxWriter as the engine. 
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer: 
            rand_customers.to_excel(writer, sheet_name='OrderedCustomer', index=False) 
            order_item_list.to_excel(writer, sheet_name='ItemsOrdered', index=False) 
        # Ensure the buffer is set to the beginning 
        buffer.seek(0)
        return buffer 
    # Initialize the boto3 client 

    s3_client = boto3.client('s3') 
    # Upload the file to S3 
    file_name = f"new_orders_details.xlsx"         #{datetime.now().strftime('%d%m%y%H%M%S')}
    s3_client.upload_fileobj(generate_excel_buffer(rand_customers,order_item_list), 'zishtacoretransit-process', file_name) 

    def trigger_the_mail(message,attachment_buffer):
        with open(r'C:\Users\user\pythontest\explorepy\Project 1\DataSet\email_pwd.json','r') as json_file:
            json_data = json.load(json_file)

        from_address = json_data['Details'][0]["email"]
        to_address = [j["Email"] for j in json_data['Details'][1::]]
        subject = "Job Status Notification!"
        body = message

        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = ', '.join([j["Email"] for j in json_data['Details'][1::]]) 
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment_buffer.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename='new_orders_details.xlsx')
        msg.attach(part)

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = json_data['Details'][0]["email"]
        smtp_password = json_data['Details'][0]["password"]

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            text = msg.as_string()
            for new_mail in to_address:
                server.sendmail(from_address, new_mail, text)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            server.quit()

    trigger_the_mail(success_msg,generate_excel_buffer(rand_customers,order_item_list))         #Email function call
    from psycopg2 import sql        #importing Sql Module from psycopg2 liber
    insert_intolog = sql.SQL('''insert into zishta2024.job_log(id,job_name,status,message,success) 
                             values(%s,%s,%s,%s,%s)''')
    extract_query.execute(insert_intolog,(f" SQ{datetime.now().strftime('%d%m%y%H%M%S')}",'Success trigger.','Success',f"Job Succesfully completed at {datetime.now().strftime('%d%m%y%H%M%S')}",'T'))
    connect_todb.commit()
except Exception as e:
    print(f'{e}')
    trigger_the_mail(Failure_message,generate_excel_buffer(rand_customers,order_item_list))
    insert_intolog = sql.SQL('insert into zishta2024.job_log(id,job_name,status,message,success) values(%s,%s,%s,%s,%s)')
    extract_query.execute(insert_intolog,(f"REJ{datetime.now().strftime('%d%m%y%H%M%S')}",'Failed trigger.','Failed',f"Error Msg: {e}",'F'))
    connect_todb.commit()


import pandas as pd
import psycopg2
'''
import pandas as pd
from sqlalchemy import create_engine
# Create an engine
engine = create_engine('postgresql://postgres:log@localhost/zishta2024dump')
# Execute a query and load data into a DataFrame
df = pd.read_sql_query("SELECT * FROM zishta2024.item", engine)
# Print DataFrame
print(df)

req_column= ['itemid', 'cancel', 'modifiedon', 'createdon','company', 'transid', 'itemdesc',
               'itemcode', 'item_hsn', 'taxcategorycode', 'taxrate',  'active',  'itemname','sellingunit', 'stdcost', 'mrp',
                 'zishtaitemcode',  'comboitem','stdsellingprice', 'shopify_id', 'itemcategoryid', 'itemcategory',
                  'productcategory', 'hsnno', 'purchaseac','amazonitemcode', 'amazon_code']

val = ''.join('a.'+i.strip('')+',' for i in req_column)

print(val)
'''
connect_todb = psycopg2.connect(
    host = 'localhost',
    database = 'zishta2024dump',
    user = 'postgres',
    password = 'log',
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
extract_query.execute(f""" select a.itemid,a.cancel,a.modifiedon,a.createdon,a.company,a.transid,a.itemdesc,a.itemcode,a.item_hsn,
                      a.taxcategorycode,a.taxrate,a.active,a.itemname,a.sellingunit,a.stdcost,a.mrp,a.zishtaitemcode,a.comboitem,
                      a.stdsellingprice,a.shopify_id,a.itemcategoryid,a.itemcategory,a.productcategory,a.hsnno,a.purchaseac,
                      a.amazonitemcode,a.amazon_code from {schema}.item a """)
items = extract_query.fetchall()
columns = [desc[0] for desc in extract_query.description]
item_df = pd.DataFrame(items ,columns=columns)
# customer details
extract_query.execute(f"""select a.retail_customerid,a.cancel,a.createdby,a.createdon,a.mobileno,a.customer_name,a.gstno,a.address,
                      a.branchid,a.locationid,a.baddress,a.bcountry,a.bstate,a.bcity,a.daddress,a.dcountry,a.dstate,a.dcity,a.bmobileno,
                      a.email,a.bpincode,a.dpincode,a.bcountry_code,a.bstate_code,a.dcountry_code,a.dstate_code 
                      from {schema}.retail_customer a where (a.mobileno is not null or a.mobileno<>'')""")
customers_data = extract_query.fetchall()
cust_columns = [desc[0] for desc in extract_query.description]
cust_data= pd.DataFrame(customers_data,columns=cust_columns)
print(len(cust_data))



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "your_email@example.com"
to_address = "recipient@example.com"
subject = "Email Notification"
body = "This is a test email notification from Python."

msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'your_email@example.com'
smtp_password = 'your_password'

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(from_address, to_address, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

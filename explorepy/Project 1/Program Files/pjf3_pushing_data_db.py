import pandas as pd
import psycopg2
import random
import json
import boto3 
import io
from io import BytesIO
from datetime import datetime , timezone, timedelta 
import time
from sqlalchemy import create_engine, text
import logging


# def get_latest_file(bucket_name):
s3 = boto3.client('s3')
bucket_name = 'zishtacoretransit-1'
response = s3.list_objects_v2(Bucket=bucket_name)
    
    # Check if the bucket is empty
# if 'Contents' not in response:
#     return None
    
    # Find the latest file
latest_file = max(response['Contents'], key=lambda x: x['LastModified'])
latest_file_name = latest_file['Key']
latest_file_time = latest_file['LastModified']
   
# Example usage

print(latest_file_name)

if latest_file_name.split('.')[-1] in ['xlsx','xls']:
    response = s3.get_object(Bucket=bucket_name, Key=latest_file_name)
    print(response['Body'])
    all_sheets= pd.read_excel(BytesIO(response['Body'].read()),sheet_name=None, engine='openpyxl')
    OrderedCustomer= all_sheets['OrderedCustomer']
    ItemsOrdered= all_sheets['ItemsOrdered']#, engine='openpyxl')
    # print(OrderedCustomer)


# print(f"Latest file: {latest_file_name}, Last modified time: {latest_file_time}")

logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db_connection_string = 'postgresql+psycopg2://postgres:log@localhost:5432/zishta2024dump'
engine = create_engine(db_connection_string)

# # Step 3: Specify the columns to insert (excluding the primary key column)
columns_to_insert = ['mobileno', 'customer_name', 'branchid', 'locationid', 'daddress',
       'dcountry', 'dstate', 'dcity', 'dpincode', 'orderno', 'salesorder_id','order_date']

missing_columns = [col for col in columns_to_insert if col not in OrderedCustomer.columns]
if missing_columns:
    raise ValueError(f"Missing columns in DataFrame: {missing_columns}")

# Check if DataFrame is empty
if OrderedCustomer.empty:
    raise ValueError("The DataFrame is empty. No data to insert.")
# print(pd.read_sql("select * from zishta2024.item",con=engine))
try:
    with engine.begin() as connection:
        OrderedCustomer[columns_to_insert].to_sql(name = 'sales_order_vnky', con=connection, schema='zishta2024',if_exists='append', index=False)
        ItemsOrdered.to_sql(name = 'itemsordered_vnky', con=connection, schema='zishta2024',if_exists='append', index=False)
        try:
            # text("CALL insert_employee(:emp_name, :emp_department, :emp_salary)"), {"emp_name": emp_name, "emp_department": emp_department, "emp_salary": emp_salary} )
            connection.execute(text('call sp_process_invoice()'))
        except Exception as e:
            print(f"Error inserting data: {e}")
    print("Data inserted successfully!")
    
except Exception as e:
    print(f"Error inserting data: {e}")
finally:
    connection.commit()
    connection.close()
    

from datetime import datetime,timedelta
import psycopg2  as pg2
import pandas as pd
import sys
from faker import Faker 
import random

# Get the directory path of the file where 'firstscript.py' is located
module_path = 'c:/Users/user/pythontest/explorepy/Python_explore/old_python_sheets'

# Add this directory to sys.path
if module_path not in sys.path:
    sys.path.append(module_path)

# Now, you can import the 'sums' function from 'firstscript'
#           from firstscript import sums

# Example usage of the 'sums' function
# result = sums(5, 10)
# print(result)

# from 'c:/Users/user/pythontest/explorepy/Python_explore/old_python_sheets/firstscript.py' import sums 
hostname = 'localhost'
dbname = 'zishta2024dump'
port = 5432
user = 'postgres'
password = 'log'
schema = 'zishta2024'

connections  = pg2.connect(
    host = hostname,
    dbname = dbname,
    user = user,
    password = password
)
ref_cursor  = connections.cursor()
ref_cursor.execute(f"select i.itemid,i.itemdesc,i.itemcode,i.mrp from {schema}.item i")
rows = ref_cursor.fetchall()
columns = [desc[0] for desc in ref_cursor.description]
df = pd.DataFrame(rows,columns=columns)

ref_cursor.execute(f'select l.* from {schema}.branch b join {schema}.location l on b.branchid = l.branch')
loc_columns = [ desc[0] for desc in ref_cursor.description]
all_rows = ref_cursor.fetchall()
loc_branch = pd.DataFrame(all_rows,columns =loc_columns )

ref_cursor.execute(f'select * from {schema}.retail_customer')
customer_data = ref_cursor.fetchall()
customers = pd.DataFrame(customer_data,columns = [ desc[0] for desc in ref_cursor.description])
# print(customers.columns)
unique_data = customers["branchid"].drop_duplicates()

# random_state = unique_data.sample().iloc[0] 
# print("Random state:", random_state)
fake = Faker('en_In')

# start_date = datetime.date(datetime.strftime(datetime.now() - timedelta(weeks= 125),'%Y/%m/%d'))
# end_date  = datetime.date(datetime.strftime(datetime.now(),'%Y/%m/%d'))
start_date = datetime.now() - timedelta(weeks= 125)
end_date  =datetime.now()

user_name = ['vnky','kiran','srikanth','vijay','tharun']

noo_records = 30000
customers_data = {'First_name' : [fake.first_name() for _ in range(noo_records)],
                  'Last_name' : [fake.last_name() for _ in range(noo_records)],
                  'mobile' :[fake.phone_number() for _ in range(noo_records)],
                  "Area" : [fake.address() for _ in range(noo_records)],
                  "username" :[user_name[random.randint(0,4)] for _ in range(noo_records)],
                  "Created_on" : [fake.date_time_between_dates(start_date,end_date) for _ in range(noo_records)],
                  "Email" : [fake.email() for _ in range(noo_records)],
                  "Branch Id": [unique_data.sample().iloc[0] for _ in range(noo_records)],
                  "Company Id" :[54644564 for _ in range(noo_records)]
                  }

actual_data = pd.DataFrame(customers_data)
# actual_data.to_csv('customer_data.csv')
actual_data.rename(columns={"Branch Id": 'branch_id'},inplace=True)

print(actual_data["branch_id"].value_counts())
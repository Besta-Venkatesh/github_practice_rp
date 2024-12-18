import csv
import random
from debugpy.common.log import newline
from faker import Faker
import pandas as pd
from datetime import datetime as dt

# Initialize Faker
fake = Faker()
start_date = dt.strptime('01/01/2023','%d/%m/%Y')
End_date = dt.strptime('31/12/2024','%d/%m/%Y')
print(dt.date(start_date))
print(dt)

# Number of rows to generate
num_rows = 100
print(fake.time(),fake.date_this_year(),fake.date_time_this_year(),fake.date_time_between_dates(start_date,End_date))
# Generate random data
data = {
    'id': [i for i in range(1, num_rows + 1)],
    'name': [fake.name() for _ in range(num_rows)],
    'address': [fake.address() for _ in range(num_rows)],
    'email': [fake.email() for _ in range(num_rows)],
    'phone_number': [fake.phone_number() for _ in range(num_rows)],
    'date':[fake.date_time_between_dates(start_date,End_date) for _ in range(num_rows)],
    'profit':[random.randint(1000,9999) for _ in range(num_rows)]
}

# Create DataFrame
df = pd.DataFrame(data)
lst_columns = ['name','age','address']
print(df)  # Print first 5 rows for brevity

df.to_excel(r"C:\Users\user\pythontest\explorepy\Datasets\excel_practice.xlsx", index=False)

from faker import Faker
import json

# Initialize Faker
fake = Faker()
# fake.date()
def generate_fake_data(columns, num_rows):
    data = []
    for _ in range(num_rows):
        row = {col: getattr(fake, col)() for col in columns}
        data.append(row)
    return json.dumps(data, indent=4)

# List of columns to generate
lst_columns = ['name', 'address', 'email', 'phone_number', 'date']

# Number of rows to generate
# Generate and print the JSON data
fake_json_data = generate_fake_data(lst_columns, num_rows)
list_dict = json.loads(fake_json_data)
# print(list_dict)
# with open('fack_data.csv','w',newline='') as csv_file:
#     fields = list_dict[0].keys()
#     write  = csv.DictWriter(csv_file,fieldnames=fields)
#     write.writeheader()
#     write.writerows(list_dict)
#     # json.dump(fake_json_data,csv_file,indent=4)
# print(fake)
# print(fake.json())
# print(fake.aba())
# print(fake.zipcode())
# print(fake.zipcode_plus4())
# val = fake.area_name()


'''Data Loading with Failure Recovery
Context
Data Engineer working for an e-commerce platform. The company regularly updates its customer database by loading transaction data into a SQL database using Python and Pandas.
While loading 10,000 transaction records, the system encountered an unexpected crash. 

You need to:
1.Verify how many records were successfully loaded before the crash.
2.Identify the remaining records to be loaded.
3.Resume the data loading process without reloading already loaded records.'''


import pandas as pd
import numpy as np

# Simulating 10,000 records
data = {
    'Transaction_ID': range(1, 10001),
    'Customer_ID': np.random.randint(1000, 5000, size=10000),
    'Amount': np.random.uniform(10.0, 1000.0, size=10000),
    'Timestamp': pd.date_range('2024-01-01', periods=10000, freq='S')
}

df = pd.DataFrame(data)
# print(f"Total records: {len(df)}")
# Loading Records in Chunks
# To prevent the crash from affecting the entire load, the script loads records in chunks of 1,000.
# Define a function to simulate record loading
def load_records(chunk, loaded_ids):
    for _, row in chunk.iterrows():
        # Simulating a crash at Transaction_ID = 5,500
        if row['Transaction_ID'] == 5500:
            raise Exception("Simulated crash at Transaction_ID = 5500")
        
        # Pretend to load the record into the database
        loaded_ids.add(row['Transaction_ID'])

# Tracking loaded records
loaded_ids = set()

try:
    chunk_size = 1000
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i + chunk_size]
        load_records(chunk, loaded_ids)

except Exception as e:
    print(f"Loading interrupted: {e}")

# Identifying Successfully Loaded Records

# Loaded records
loaded_records = df[df['Transaction_ID'].isin(loaded_ids)]
print(f"Records successfully loaded: {len(loaded_records)}")

# Identifying Remaining Records

# Remaining records to be loaded
remaining_records = df[~df['Transaction_ID'].isin(loaded_ids)]
print(f"Records remaining to be loaded: {len(remaining_records)}")

# Resuming the Load
# Now, load only the remaining records into the database.
try:
    for i in range(0, len(remaining_records), chunk_size):
        chunk = remaining_records.iloc[i:i + chunk_size]
        load_records(chunk, loaded_ids)
    print("Data loading completed successfully.")

except Exception as e:
    print(f"Error during reload: {e}")
 


#Different Method to insert data to database tables--------------------------------------------------------

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Example DataFrame
df = pd.DataFrame({'name': ['Alice', 'Bob'], 'age': [25, 30]})

# Create a connection to the database
conn = psycopg2.connect("dbname=database_name user=username password=password host=host")
cur = conn.cursor()

# Insert DataFrame into PostgreSQL table
execute_values(cur, "INSERT INTO your_table_name (name, age) VALUES %s", df.values)

conn.commit()
cur.close()
conn.close()

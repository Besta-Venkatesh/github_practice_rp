import psycopg2  as pg2
import pandas as pd
import sys
# import os

# Get the directory path of the file where 'firstscript.py' is located
module_path = 'c:/Users/user/pythontest/explorepy/Python_explore/old_python_sheets'

# Add this directory to sys.path
if module_path not in sys.path:
    sys.path.append(module_path)

# Now, you can import the 'sums' function from 'firstscript'
from firstscript import sums

# Example usage of the 'sums' function
result = sums(5, 10)
print(result)

# from 'c:/Users/user/pythontest/explorepy/Python_explore/old_python_sheets/firstscript.py' import sums 
hostname = 'localhost'
dbname = 'zishta2024dump'
port = 5432
user = 'postgres'
password = 'log'

connections  = pg2.connect(
    host = hostname,
    dbname = dbname,
    user = user,
    password = password
)
ref_cursor  = connections.cursor()
ref_cursor.execute("select i.itemid,i.itemdesc,i.itemcode,i.mrp from zishta2024.item i")
rows = ref_cursor.fetchall()
columns = [desc[0] for desc in ref_cursor.description]
df = pd.DataFrame(rows,columns=columns)
print(df)
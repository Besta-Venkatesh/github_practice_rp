
import  psycopg2
import logging
import pandas as pd

host = 'localhost'
dbname = "zishta2024dump"
user = "postgres"
password = "log"
schema = 'zishta2024'

try:

    pg_db_connection= psycopg2.connect(
        host =host,
        database = dbname,
        user = user,
        password = password
    )
    ref_todb_cursor = pg_db_connection.cursor()
    logging.basicConfig(level=logging.DEBUG)
    create_table_query = f'''drop table IF EXISTS {schema}.item_local;
        create table {schema}.item_local(
                        itemno numeric primary key,
                        itemname varchar,
                        mrp float,
                        sellingprice numeric,
                        uom varchar );'''
    ref_todb_cursor.execute(create_table_query)
    pg_db_connection.commit()
    logging.info(' Table Created:')

    insert_script = f'''
        insert into {schema}.item_local
        select x*100,'product'||x,x*10+28,x*10+9,'nos' from generate_series(101,200) x
    '''
    ref_todb_cursor.execute(insert_script)
    pg_db_connection.commit()
    logging.info(' Data Inserted:')

    get_query_data =f'''select * from {schema}.item '''

    ref_todb_cursor.execute(get_query_data)
    rows = ref_todb_cursor.fetchall()
    columns = [desc[0] for desc in ref_todb_cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)
    print(df.head())
    logging.info(' Data Fetched:')
    # print('Table created',schema)
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQLl", error)

finally:
    if pg_db_connection :
        ref_todb_cursor.close()
        pg_db_connection.close()
        print('Database connection closed')

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)

pd.options.display.max_rows =200

print(pd.options.display.max_rows)



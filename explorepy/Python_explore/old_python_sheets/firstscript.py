# a = [[1,2,34,4],[734,35,4,4,5],[1,1,333,34]]

# for i in a:
#     print(i)
# 9

# li=[1,2,3]
# print(li*2)

# import keyword
# print(keyword.iskeyword('string'))

# print(help('keywords'))

# print(list('asfg'),float(12))

# # print(str('ufhd',[7834,3847,283438]))

# p = [827348]
# p.extend('5')
# print(p)

x1 = 'hello world'

xyz = 'hello world'[::]

if __name__ == "__main__":
    print(x1,xyz)
    print(id(x1),id(xyz),end='\tjkhk ')
    print(x1,xyz)
    print(list('875348756')*2)
    print('string my be alowed{2} in between two other {0}strings'.format('vnky',9,['erer',546]))


var1 = []


for i in range(10):
    var1.append(i)


# print(var1)

def ram():
    val1 =1
    for i in range(1,10):
        val1 = val1 * i
    return val1


# print(ram())

lst = [[1,23,4,4],['dfsdf','wfewe','wefwf','effwf']]
lst[1][2] = '988'
if  __name__ == "__main__":
    print(lst)
    print(tuple('venkatesh'))


tup1 = tuple([[1,23,4,4],['dfsdf','wfewe','wefwf','effwf']])
# tup1[1]='hjd'
# print(tup1)
#
lst1 = 'venkatesh1998.31@gmail.com'

# print(set([32,32,4424]))

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
    if __name__ == "__main__":
        logging.info(' Table Created:')

    insert_script = f'''
        insert into {schema}.item_local
        select x*100,'product'||x,x*10+28,x*10+9,'nos' from generate_series(101,200) x
    '''
    ref_todb_cursor.execute(insert_script)
    pg_db_connection.commit()
    if __name__ == "__main__":
        logging.info(' Data Inserted:')

    get_query_data =f'''select * from {schema}.item_local fetch first 10 rows only'''

    ref_todb_cursor.execute(get_query_data)
    rows = ref_todb_cursor.fetchall()
    columns = [desc[0] for desc in ref_todb_cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    if __name__ == "__main__":
        print(df)
        logging.info(' Data Fetched:')
    # print('Table created',schema)
except (Exception, psycopg2.Error) as error:
    if __name__ == "__main__":
        print("Error while connecting to PostgreSQL", error)

finally:
    if pg_db_connection :
        ref_todb_cursor.close()
        pg_db_connection.close()
        # print('Database connection closed')


textdata = '''Parental Level of Education: Indicates the educational background of the student's family.
Lunch: Shows whether students receive a free or reduced lunch, which is often a socioeconomic indicator.
Test Preparation Course: This tells whether students completed a test prep course, which could impact their performance.
Math Score: Provides a measure of each student’s performance in math, used to calculate averages or trends across various demographics.
Reading Score: Measures performance in reading, allowing for insights into literacy and comprehension levels among students.
Writing Score: Evaluates students' writing skills, which can be analyzed to assess overall literacy and expression.'''
import csv
linelist = []
# with open(r'C:\Users\user\pythontest\explorepy\Datasets\writetofile.txt','a') as file:
#     file.write(textdata)
# #     # print(readrows)
# with open(r'C:\Users\user\pythontest\explorepy\Datasets\studentdata.csv','r') as file:
#     datafromfile = csv.reader(file)
#     for i in datafromfile:
#         linelist=linelist + [i]
#     # print(datafromfile)
# columns = linelist[0]
# df_data = pd.DataFrame(linelist[1::],columns=columns)
# with open(r'C:\Users\user\pythontest\explorepy\Datasets\writetofile.txt','a') as file:
#     file.writelines(linelist)

# with open(r'C:\Users\user\pythontest\explorepy\Datasets\writetofile.txt','r') as file:
#     print(file.readlines())
# print(df_data)
# import json
# print(json.dumps(data),type(json.dumps(data)))

def sums(a,b):
    return a+b
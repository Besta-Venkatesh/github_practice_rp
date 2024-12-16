from logging import exception, error
from time import strftime

import pandas as pd
import  psycopg2 as pg2
import logging as log

from pandas import to_datetime

pd.options.display.max_columns = None
# pd.set_option('display.max_width',None)

try:
    postgres_connection = pg2.connect(
        host = 'localhost',
        database = 'zishta2024dump',
        user = 'postgres',
        password = 'log'
    )
    open_curser = postgres_connection.cursor()
    open_curser.execute('''select a.locationid,a.locationname, a.cancel,a.active,b.branchname,b.branchid,b.active,
        b.createdby,b.createdon,b.tinno,b.branchaddress,b.city,b.state,b.country from zishta2024.location a 
                                        join zishta2024.branch b on a.branch = b.branchid  order by 5
                                        ''')
    execute_query = open_curser.fetchall()
    table_columns = [desc[0] for desc  in open_curser.description]
    df = pd.DataFrame(execute_query,columns=table_columns)
    lst_index = [ i for i in range(0,len(df)) ]
    # print(df)
    # print(df.dtypes)
    # print(df.dtypes.apply(lambda x: x.name).to_dict())
    second_curser = postgres_connection.cursor()
    second_curser.execute('''select a.docid,a.docdate,a.newcustomer,a.branch,a.location,
    a.total_sales_amount,a.bulk_discount,a.shipping_charges,sum(b.gross_amount) gross,sum(b.discount)discount,sum(b.taxableamount) taxamt,
	sum(b.net_amount)netamt,a.daddress||' '||a.dcity||' ' ||a.dstate||' ' ||a.dcountry|| ' '||a.dpincode address
	from zishta2024.salesinvoice_header a join zishta2024.salesinvoice_items b using(salesinvoice_headerid) 
	 where a.transid ='salco'
	 group by a.newcustomer,a.daddress||' '||a.dcity||' ' ||a.dstate||' ' ||a.dcountry|| ' '||a.dpincode,
    a.total_sales_amount, a.docid,a.docdate,a.bulk_discount,a.shipping_charges,a.createdon,a.branch,a.location
	order by a.createdon''')
    new_query = second_curser.fetchall()
    colms = [i[0] for i in second_curser.description]
    df2 = pd.DataFrame(new_query,columns=colms)
    # print(df2)
    x = df.merge(df2,left_on='branchid',right_on='branch')
    print(x.info())
except (Exception,pg2.Error) as errorname:
    print('Error in the output of Postgresql: ',errorname)

finally:
    open_curser.close()
    postgres_connection.close()
    print('Database Connection closed')

from datetime import datetime as dt
# print(pd.api.types(pd.to_datetime('2024-11-22 14:38:36.573397')))
# print(dt.strptime('2024-11-22 14:38:36','%Y-%m-%d %H:%M:%S'))
# print(type(to_datetime('2024-11-22 14:38:36.573397')))

# print(timestamp,type(timestamp))
# print()
# print(df.dtypes)

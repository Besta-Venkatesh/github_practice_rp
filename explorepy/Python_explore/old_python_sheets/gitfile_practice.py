from datetime import datetime ,timedelta
# print('Hello man')
# print('It is very importent to stick to what you belive and what you want.')
print(datetime.now() + timedelta(days = 10))
print(datetime.strftime(datetime.now() - timedelta(weeks=52),'%Y/%m/%d %H:%M:%S'))



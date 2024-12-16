import json

import pandas as pd

# from firstscript import columns

# a= [1,1,23,765,45,67,9,'kjbk',7]
# ser1 = pd.Series(a,index=[ chr(i) for i in range(65,65 + len(a))])
# print(ser1[::2])
# print()
# pd_series = {'day1':203,'day2':[72,31,3,21],'day3':4324}
# print(pd.Series(pd_series))
# print()
# list_dic = {'name':['raj','kiran','kishore','sreenu','shamala','priya'],'age':[19,38,23,34,52,42],
#             'gender':['M','M','M','F','F','F']}
#
# print(pd.DataFrame(list_dic))
# print()
#
data = [ ['Alice', 'hfh', 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago'] ]
#
# print(pd.DataFrame(data))


import pandas as pd

# Set pandas options to display all rows and columns
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Assume `df` is your DataFrame
# df = pd.DataFrame({'Column1': range(1200), 'Column2': range(1200)})  # Example DataFrame
pd.options.display.max_rows = None
# print(pd.options.display.max_rows)

var1=pd.read_csv(r'C:\Users\user\pythontest\explorepy\Datasets\all_youtube_analytics.csv')
dfs = pd.DataFrame(var1)
# print(dfs.info())
# print(dfs.columns)
# redViews

dfs.rename(columns={'redViews':'userViews'},inplace=True)
# print(dfs.columns)
# print(dfs.head())

dfs['userViews'] =dfs['userViews'].astype('bool')
# print(dfs.head())

# print(dfs['video_id'].value_counts(normalize=True))

data = {
    'Info': ['Alice,Johnson', 'Bob Smith', 'Charlie:Brown']
}
df = pd.DataFrame(data)

# Split the 'Info' column by multiple delimiters
df[['FirstName', 'LastName']] = df['Info'].str.split(r'[, :]', expand=True)
# print(df['Info'].str.split(r': ,', expand=True))
print(df[['Info','FirstName','LastName']])
print(df['FirstName'][1:])










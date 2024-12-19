import pandas as pd
import csv
import  re
import random
import string
from os import write


def generate_random_string():
    upper_case = ''.join(random.choices(string.ascii_uppercase, k=5))
    lower_case = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{upper_case} {lower_case}"

# Create a set to store unique strings
unique_strings = set()

# Generate 10 unique strings
while len(unique_strings) < 10:
    unique_strings.add(generate_random_string())

# Print the result
# print(unique_strings)

# print(''.join(random.choices(string.ascii_uppercase,k=8)))

names = {'HaRIsh PatEl','KIRan PATil', 'AniL RaO','SAnjaY KumaR','GaNEsh BAbu','ViNay KuMar','Pankaj KUmar','DivYa KUmaR','VinoD PaTil' }
unique_strings = unique_strings.union(names)
lst_names = ['Sanjay Kumar','Ganesh Rao','Ganesh Prem','Asha Rao','Anil Rao']
titled_phrases = map(lambda x: x.title(), unique_strings)
titled_phrases1 = list(titled_phrases)
titled_phrases2 = titled_phrases1[::]
# print(sorted(titled_phrases2))                          # sorted in asc
# print(sorted(titled_phrases1,reverse=True))             # sorted in desc
lst_names_to_find = ['Kumar','Patil']
count_of_names ={}
for i in lst_names_to_find:
    count_of_names[i] = 0
    for j in unique_strings:
        if j.lower().find(i.lower())>0:
            count_of_names[i] += 1
# print(count_of_names)                                   # print count of above list in dictionary

for i in lst_names:
    if i in titled_phrases1:
        titled_phrases1.remove(i)
# print(titled_phrases1)                                  # remove above elements from the list

# second problem---------------------------------------------------------------------------

keys = [random.randint(1000,9999) for i in range(10)]
keys.sort()
values =[ ''.join(random.choices(string.ascii_letters,k=12)).title() for i in range(10)]
from itertools import zip_longest
dic_out = dict(zip_longest(keys,values))

deleted_count =0
dic_out_afterdelete = dic_out.copy()
for i in dic_out:
    if dic_out[i][0].upper() in ('A','G'):
        dic_out_afterdelete.pop(i)
        deleted_count += 1
# print(dic_out)
# print('Total deleted Elements: '.split(),deleted_count)
# print(dic_out_afterdelete)

# 4th Probelem-----------------------------------------------------------------
lst_date =[]
with open('readfile','r') as file:
    for lines in file:
        lst_date =lst_date + re.findall(r'[0-9]+', lines)
    lst_date = [int(i) for i in lst_date if i.isnumeric() ]
# print(lst_date)
# print('Sum of all the numbers:',sum(lst_date))
# print('Average of all the numbers:',sum(lst_date)/len(lst_date))
lst_date.sort()
# print('Lowest Number in the list:',lst_date[0])
evenodd_count = {'Even':sum(1 for i in lst_date if i%2 ==0), 'Odd':sum(1 for i in lst_date if i%2 !=0)}
# print('Number Of even and Odds:',evenodd_count)

# 3rd Problem---------------------------------------------------------------------------------------

with open('stringfile','r') as file:
    # for file_line in range(len(file.readlines()),0,-1):
    var = file.read()
    # print(var[::-1])
    count_vovels = {'Vowels' :sum(1 for i in var if i.lower() in ('a','e','i','o','u')),
                    'Num Of Words': len(var.split())}
    # print(count_vovels)
    # print('First four Words',var.split()[0:3])
    # print('First last Words', var.split()[-1:-7:-1])

#------------------------------------------------------------------------------------------------
def send_afile(filenam,output_type):
    with open(filenam,'r') as file:
        varcha  =file.read()
        if output_type.lower() == 'content':
            return varcha
        elif output_type.lower() == 'upper':
            return varcha.upper()
        elif output_type.lower() == 'title':
            return varcha.title()

# print(send_afile('stringfile','uppER'))

#---------------------------------------------------------
with open('stringfile', 'r') as file:
    varcha = file.read()
    non_vowel_words = sum(1 for jj in varcha.split() if not re.search(r'[aeiou]+',jj))
    # print(len(varcha.split()))
    # print(non_vowel_words)
    tofetch_evenpos = varcha.split()
    # print([ tofetch_evenpos[i] for i in range(0,len(tofetch_evenpos)) if i%2 ==0])

print('\tuiestyligu\n'.strip())

#----------------------------------------------------------------------------------
s1 = "today is Wednesday"
s2 = "the month is December"
lst = ['and the year is 2024','All are waiting for 2025']
tup = ('Data Engg is a growing field','skills needed are SQL, Python , Pandas')

with open('append_data.txt','w',newline='') as append_data:
    append_data.writelines(s1)
    append_data.write(s2)
    append_data.writelines(tup)
    append_data.writelines(lst)

# with open('append_data.txt','r') as append_data:
#     print(append_data.read())


prod_3=[[100,'Laptop',56000,4,'A'],[200,'Mobile',22000,8,'B'],
        [122, 'charger', 1800, 5, 'A'],
        [818, 'Head phone', 1500, 12, 'B'],
        [111, 'Printer', 10500, 12, 'A']]
prod_1 = { 'prod ID':1414,'name':'speaker','price': 5500,'qty on hand':4,'prod type':'B'}
prod_2 = { 'prod ID':1004,'name':'mob cover','price': 500,'qty on hand':25,'prod type':'A'}
csv_desc = [prod_1,prod_2]
# with open('product.csv','a',newline='') as product:
#     fields = csv_desc[0].keys()
#     write = csv.DictWriter(product,fieldnames=fields)
#     write.writeheader()
#     write.writerows(csv_desc)
with open('product.csv','a',newline='') as product:
    fields = csv_desc[0].keys()
    write  = csv.writer(product)
    write.writerows(prod_3)

lst_dict = []
with open('product.csv','r',newline='') as product:
    # fields = csv_desc[0].keys()
    file_data = csv.DictReader(product)
    for i in file_data:
        lst_dict += [i]
        # print(i)
    product.close()

# print(lst_dict)
#
with open('product.csv', 'w',newline='') as product:
    fields = lst_dict[0].keys()
    write_to_file = csv.DictWriter(product, fieldnames=fields)
    var1 = 0
    for j in range(0,len(lst_dict)):
        lst_dict[j]['Prod val'] = int(lst_dict[j]['price']) * int(lst_dict[j]['qty on hand'])
        if var1 == 0:
            write_to_file.writeheader()
            var1=1
        write_to_file.writerow(lst_dict[j])


# with open('product.csv','r') as product:
#     dict_reader = csv.reader(product)
#     for i in dict_reader:
#         print(i)
#     print(dict_reader)
pandas_csv = pd.read_csv('product.csv')
print(pd.DataFrame(pandas_csv))






students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [58, 64]},
    {"name": "Charlie", "grades": []},
    {"name": "Diana", "grades": [99, 95, 100]}
]

# Name: Alice
# Average Grade: 85.0
# Assigned Grade: B
# Status: Pass

# gradeva = ''

def assingrade(i):
    if (sum(students[i].get('grades'))/len(students[i].get('grades')) if len(students[i].get('grades')) >0 else 1) in range(91,100):
        return 'A'
    elif (sum(students[i].get('grades'))/len(students[i].get('grades')) if len(students[i].get('grades')) >0 else 1) in range(81,90):
        return 'B'
    elif (sum(students[i].get('grades'))/len(students[i].get('grades')) if len(students[i].get('grades')) >0 else 1) in range(71,80):
        return 'C'
    elif (sum(students[i].get('grades'))/len(students[i].get('grades')) if len(students[i].get('grades')) >0 else 1) in range(61,70):
        return 'D'
    else:
        return 'F'

# for i in range(0,len(students)):
    # print('Name: ' + students[i].get('name'),
    #       'Average Grade: '+ str(sum(students[i].get('grades'))/ len(students[i].get('grades')) if len(students[i].get('grades')) >0 else 1),
    #       'Assigned Grade: ' + assingrade(i),
    #       'Status: Fail' if assingrade(i) in ('D','F') else 'Status: Pass',
    #       sep='\n' )
    # print()



st1 = 'ABCDEFHIJKLMNOPQRSTUVWXY Z'+ 'ABCDEFHIJKLMNOPQRSTUVWXYZ'[::-1]
str2 = ''
for i in range(0,len(st1)):
    if st1.isalpha():
        str2 =str2 + chr(ord(st1[i])+32)
    else:
        str2 = 'String Contain special Characters'
# print(str2)
 
#  Letter Frequency
# Task: Write a program to count the frequency of each letter in a given string.

var1 = '''Data Structures and Algorithms (DSA) is a fundamental part of Computer Science that teaches you how to think and solve complex problems systematically.
Using the right data structure and algorithm makes your program run faster, especially when working with lots of data.
Knowing DSA can help you perform better in job interviews and land great jobs in tech companies.'''

# unqval = sorted(list(set(var1)))
# unq = unqval[::]
# listcount = []
# # print(unqval)
# listcount = listcount + [{unqval[i]:var1.count(unqval[i])} for i in range(0,len(unqval))]

# print(listcount)

num_list = [12,4,344,536,457,596,796,977,89,57,245,13,63,46,2465,252435,345,8]
num_list2 = num_list[::]
st_len  = 0
sort_num = []

def bubble_sort(arr):
    n = len(arr)
    for var_i in range(n):
        for var_j in range(0, n-var_i-1):
            if arr[var_j] > arr[var_j+1]:
                arr[var_j], arr[var_j+1] = arr[var_j+1], arr[var_j]

# Example usage
num_list = [12, 4, 344, 536, 457, 596, 796, 977, 89, 57, 245, 13, 63, 46, 2465, 252435, 345, 8]
bubble_sort(num_list)
# print(num_list)


num_1 = 9487645
rnum_1 = 0
while num_1 != 0:
    val1 = num_1 % 10
    rnum_1 = rnum_1 * 10 + val1
    num_1 = num_1 // 10

print(9487645, rnum_1)
tup1 = {1,23,313,4565,7.568787,'ahga'}

# print(tup1.remove(23))
# print(tup1)

# import random
# print(random.randint(1000,9999))

restaurant_menu = {
    "Starters": {
        "Spring Rolls": 150,
        "Garlic Bread": 120,
        "Bruschetta": 130
    },
    "Main Course": {
        "Margherita Pizza": 350,
        "Grilled Chicken": 450,
        "Pasta Alfredo": 400,
        "Paneer Butter Masala": 300,
        "Mutton Biryani": 500
    },
    "Desserts": {
        "Chocolate Brownie": 200,
        "Ice Cream Sundae": 180,
        "Gulab Jamun": 120
    },
    "Beverages": {
        "Coke": 50,
        "Lemonade": 60,
        "Masala Chai": 40,
        "Espresso": 80
    }
}
restaurant_menu['Beverages']['Wine'] = 789
print(restaurant_menu['Beverages'])

lst_items = ['Main Course','Desserts','Beverages',]


restarant_data = { "a1" : {"1" : {"Spring Rolls": 150,
                    "Garlic Bread": 120,
                   "Bruschetta": 130
                  },
            }
}

print(restarant_data['a1']['1'])

print(dict(venky=26,jaish = 25,pradeep = 27,saritha = 29,renuka = 55,hari = 59))


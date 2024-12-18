# #sudoku program
# def is_valid(board, row, col, num):
#     for i in range(9):
#         if board[row][i] == num or board[i][col] == num or board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
#             return False
#     return True
#
# def solve_sudoku(board):
#     empty_spot = find_empty(board)
#     if not empty_spot:
#         return True
#     row, col = empty_spot
#     for num in range(1, 10):
#         if is_valid(board, row, col, num):
#             board[row][col] = num
#             if solve_sudoku(board):
#                 return True
#             board[row][col] = 0
#     return False
#
# def find_empty(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return (i,j)
#     return None
#
# # Example Sudoku board
# board = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]
# # print(find_empty(board))
# # solve_sudoku(board)
# # for row in board:
# #     print(row)

'''1 Given a set of items, each with a weight and a value, determine the maximum value you can obtain by putting
 items into a knapsack that has a weight capacity W.'''

lst_cole = [23,4,[33,5,46,20,45,3,4],4,2,3,[84,65,754,82,48,69,45,4,103],[72,97,38,52,81,117,]]
max_values = 0
last_value = 0
for values in lst_cole:
    if type(values) in (int,float):
        last_value = values
        if max_values < last_value :
            max_values,last_value = last_value,max_values
    elif type(values) == list:
        last_value = max(values)
        if max_values < last_value:
            max_values, last_value = last_value, max_values

# print(type(lst_cole[2]),type(lst_cole[1]))
print(max_values,last_value)


# find missing number
mis_lst = [4,3,6,19,9]
miss_num = []
for i in range(min(mis_lst)+1,max(mis_lst)):
    if  i not in mis_lst:
        miss_num +=[i]

print(miss_num)

prod_list = [2,3,5,8,9]

a= 'aaabbcdddefff'
d =''
for i in range(len(a)):
    if a[i] not in d:
        if a[i] ==a[i + 1]:
            d+=a[i]
print(d)
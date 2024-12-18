prime_list =[]
prime_num = 2
increment = 0
# for j in range(2,20):
while len(prime_list)<=999:
    for i in range(2,prime_num-1):
        if prime_num%i==0:
            increment =1
            break
    if increment == 0:
        prime_list += [prime_num]
    increment = 0
    prime_num+=1

print(len(prime_list),prime_list)
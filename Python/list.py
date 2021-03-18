import random as rnd
import random
import os

def cls(): return os.system('cls')

cls()
my_list=[]

#append
num=int(input('how many numbers do you want in the list? '))
number=0
# for x in range(num):
#    number=rnd.randint(1,1000)
#    #if number not in my_list:
#    my_list.append(number)
count=0
while count<num:
    number=rnd.randint(1,1000)
    if number not in my_list:
        my_list.append(number)
        count+=1
    else:
        pass 
print(my_list)

for index,number in enumerate(my_list):
    print(f"{index+1}: {number}")

my_list.sort()

print(my_list)

my_list.reverse()

print(my_list)

my_list.insert(rnd.randint(0,len(my_list)-1),rnd.choice(list("abcdefghijklmnopqrstuvwxyz")))
print(my_list)

print(my_list[-1])

my_number=int(input("type a number of your choice: "))

# if number  in my_list:
#     print(f"{my_number} is in my list")
index_=0
try:
    index_=my_list.index(my_number)
    # print(f"{my_number} is at index {index_}")
except:
    index_=None
if index_ is not None:
   print(f"{my_number} is in the list at index {index_}") 
else:
    print(f"{my_number} is not in the list") 
    my_list.append(my_number)
    print(my_list)

#extend
my_list2=['a','b','c','d','e','f']
my_list.extend(my_list2)
print(my_list)

my_list.append(['k','l','m'])
print(my_list)
    

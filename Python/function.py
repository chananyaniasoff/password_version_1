import random
def check(my_list):
    number=random.randint(1,1000)
    if number not in my_list:
        my_list.append(number)
        return True
    else:
        return False

numbers=[]
count=0

while True:
    if check(numbers):
        count+=1
    if count==10:
        break
    else:
        pass
print(numbers)
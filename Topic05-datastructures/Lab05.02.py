#populate a list with 10 random numbers, pop items from list one by one and print remainder of list
import random

random_list =[]
for i in range(10): #loop 10 times to append a random number to a list per loop
    random_list.append(random.randint(0,100))
print(f"Queue is: {random_list}")
while len(random_list) > 0: #while list still has items in it pop an item from list and print remaining
    print(f"Current Number is {random_list.pop()} and the queue is {random_list}")
print("The Queue is now empty!")

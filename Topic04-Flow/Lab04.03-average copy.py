#Program to keep reading numbers until user enters a 0

#take number from user
user_num = int(input("Enter a number please (0 to quit): "))
entered_numbers = [] #list of entered numbers
if user_num == 0: #if user has entered a 0 we proceed no further
    print("You entered 0 immediately")
else: #else user must not have entered 0
    while user_num !=0: #while user hasn't entered 0
        entered_numbers.append(user_num)#we don't need to add 0 to the end of the list when a user enter 0
        user_num = int(input("Enter a number again please (0 to quit): "))
    #print the average
    print(f"The average is {sum(entered_numbers)/len(entered_numbers)}")
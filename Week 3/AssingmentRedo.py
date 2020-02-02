#assignment was to take an input string from a user
#print every second letter in revese

to_be_reversed_str = str(input("Enter the number and let me cut it: "))
every_second_letter_str = to_be_reversed_str[1::2]
reversed_str = every_second_letter_str[::-1]
print(f"{every_second_letter_str} {reversed_str}")

#one line way of doing it
oneliner = to_be_reversed_str[1::2][::-1]
print(oneliner)

print(f"Cut up and reversed... {to_be_reversed_str[1::2][::-1]}")
#Programme to take input string from user and print appended string
users_string=str(input('Enter some string - '))
normalised_string = users_string.lower().strip()
print(f'Naked lower string: |{normalised_string}|')
print(f'Difference in length: {len(user_string)-len(normalised_string)}')
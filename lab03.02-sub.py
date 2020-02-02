#Programme to take two input numbers from user and print addend of the inputs
print("Watch me amaze and stupify by adding two numbers.")
num1=int(input('Hey... enter your first number...'))
num2=int(input('...alright now your second...'))
num3=str(num1-num2)
print("By my deductive reasoning, your number is - " +num3+"?")
#above line got me thinkings, what is preffered way to create the simple str for the print statement
#% formatting is an old alternative to the above, but it's clunkier.
#str.format() was a pretty good alternative, assigning variables, but seemed a bit clunky still (lot of extra typing vs '+')
#f-strings are a recent python 3.6 feature but very  nice, as you can see, really simplifies the str
print(f"By my deductive reasoning, your number is - {num1-num2}?")

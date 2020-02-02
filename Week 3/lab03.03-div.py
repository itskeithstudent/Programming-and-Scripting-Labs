#Lab3 Exercise3, program to divide two user supplied numbers and print result

def calc_quotient(dividend,divisor):
    return int(dividend/divisor)

in1=int(input("You got any numbers your want divided? "))
in2=int(input("so what you gonna divide it by? "))

quotient=calc_quotient(in1,in2)

print(f"We call this here answer of {quotient} the quotient")
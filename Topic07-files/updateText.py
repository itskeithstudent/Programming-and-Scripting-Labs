fileName = 'count.txt'

def readNumber():
    try:
        with open(fileName) as f:
            num = int(f.read())
            return num
    except IOError:
        return 0

def writeNumber(number):
    with open(fileName, 'wt') as f:
        f.write(str(number+1))

num = readNumber()
writeNumber(num)
print(f"file has now been ran {num+1} times")
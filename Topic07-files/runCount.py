fileName = 'count.txt'

with open(fileName) as f:
    num = int(f.read())

with open(fileName, 'wt') as f:
    f.write(str(num+1))

print(f"file has now been ran {num+1} times")
#Programme to have a Dictionary
currentBook={"Title": ["Harry Bopper", "Blade Itself", "Bloody Nine"]\
    ,"Author":["JK", "Joe Abercrombie", "Joe Abercrombie"], "Price": [1,2,3]}
print(currentBook)
print(currentBook["Author"])
print(currentBook.keys())
currentBook["ISBN"] = ["a1","b1","b2"]
print(currentBook)
for value in currentBook.values():
    print(value)
for value in currentBook["Author"]:
    print(value)

#dict constructor
newdict = dict(var1=["val1","val2"],var2="val1")
print(newdict)

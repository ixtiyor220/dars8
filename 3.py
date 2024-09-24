def hisobla(myList):
    myDct = {}
    
    for element in myList:
        if element in myDct:
            myDct[element] += 1
        else:
            myDct[element] = 1
    
    return myDct

inp = input("List elementlarini kiriting >>> ")
myList = list(map(int, inp.split(",")))

myDct = hisobla(myList)

print(myDct)


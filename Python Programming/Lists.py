#Lists(stroring ways) - to grouped together and need to keep it together
#name = [element, element2, element3,...elementN]

listOfNames = ["nalisha","ankit","rathod"]
print(listOfNames)


#listOfNames = listOfNames + ["Sweta"]
listOfNames += ["Sweta"]
print(listOfNames)

#access the list
print(listOfNames[-2])

print(listOfNames[1:2])
print(listOfNames[0:3:2])


print(listOfNames[::2])

listOfNames = listOfNames[::-1]
#print(listOfNames[::-1])


print("nalisha" in listOfNames)
print("lisha" in listOfNames)


for element in listOfNames:
       print(element)
print(len(listOfNames))


for index in range(len(listOfNames)):
   print(index,listOfNames[index])


listOfNames.append("Nalini")
print(listOfNames)

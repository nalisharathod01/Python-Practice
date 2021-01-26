import pygame

#pygame.init()

#Tuples - form of a DS ,allow to store ,organize the data
# to group the values

#tupleName = (element1,element2,element3,...)
#intTuples = (10,11)
#length of the Tuple = len(tupleName)


screenSize = (900,700) #(width,height)
print(screenSize)
print(screenSize[0])

print(screenSize[1:])

screenText = ("Hello" , "world")
print(screenText[1:])

#for one tuple put a comma after the first element

testTuple = ("screen Size",) + screenSize
testTuple = ("screen Size",) + (screenSize,)
print(testTuple)


print(len(testTuple))
print(len(screenSize))


#Operations on Tuples

#check certain elemeent contain in any tuple(give us a Boolean value 
#something in tupleName
#print(x in testTuple)

print(screenSize in testTuple)

print(testTuple[0])
print(testTuple[0] [:5])  #splice the string
print(testTuple[1][0])

secondTuple = testTuple[1]
print ("'secondTuple' -" ,secondTuple[0])



for var in testTuple:
       print(var)
       

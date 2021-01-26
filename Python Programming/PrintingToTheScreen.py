#print('" hello \n  world\'s" ' , 'nalisha') # \n new line
#print('" hello \tworld\'s" ') #\t tab
#print('" hello \\ world\'s"  \n ') #prints /

#name = content

helloworld = "Hello World"
caseTwo = " overwite"
#print(helloworld ,'\n' , 'ankit')
#print(helloworld)
#print(helloworld , ankit)
print(helloworld)
print(caseTwo)


#slice the string
#[start:stop:(step-> optional)]
print(helloworld[0:5])
print(helloworld[0:5:2])
print(helloworld[:5])
print(helloworld[::2])


#-1 is the last cnaharcter
print(helloworld[-1:-5:-1])
print(helloworld[::-1])

#contatination
concatStr = helloworld + " testing" + caseTwo
print(concatStr)


concatStr = helloworld + " testing" + caseTwo
print(concatStr[::-1])

print("well" *3)


toomManySpaces = "Spaceman "
print(toomManySpaces[0:-1] *2)

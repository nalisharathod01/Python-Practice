#def -> function

#def functionName(intput1, input2..):
#    code
#    return value

#result =functionName(int1,int2...)
#result = value

tesCase = 4

def addOne(x):
    y = x+1
    print(y)
    return y

result = addOne(tesCase)
print(result)


def addTwo(a,b):
    c = a+b
    return c
resultTestTwo = addTwo(3,5)
print(resultTestTwo)


ressultForStrint = addTwo("hello", str(1.0))
print(ressultForStrint)

print(addTwo(2.0, 3.5))


def inputfuc(x):
    y = x/3
    z= x/5
    return (int(y),int(z))

print(inputfuc(16))
       

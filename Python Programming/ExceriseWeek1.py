for i in range(0,5):
    print("O" * (i+1))      


numberofLines= 3
numberOs = 1
for i in range(1,4):
    whiteSpace = numberofLines - i
    print(" "*whiteSpace+ "0"*numberOs+" "*whiteSpace)
    numberOs += 2
    


    
def radiusofCircle (radius):
    pie = 3.14
    area = 2*pie*radius
    return area
print(radiusofCircle(5))


def inputChar (height , character):
    numberofLines= 3
    numberOs = 1
    for i in range(1,height):
           whiteSpace = numberofLines - i
           print(" "*whiteSpace+ character *numberOs+" "*whiteSpace)
           numberOs += 2
inputChar(4, "0")


def inpChar(height, charac):
    for i in range(height):
        print(charac * (i+1))
inpChar(5, "0")


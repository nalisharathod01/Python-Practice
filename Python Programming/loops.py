#for variableName in somethingToLoopOver:
#    code
#    moreCode

#range(start,stop,step)-> start , start+step,....,

#for decimal divide by 10 in print
for number in range(0,10,2):
    print(number/10)


    
for num2 in range(0,10,1):
    print(num2)

    
#while certain thing is true continue to do it until the condition is no longer to use
#while condition,booleanExpression:
#      code
#      moreCode

counter = 0


while counter < 10:
      print(counter)
      counter += 1  # counter + 1
      
print(counter)


text = ""
while text != "AAA":
   print(text)
   text += "A"
print(text)


#BreakingLoops

#startVariable = 0
#while True:
      # startVariable += 1
       #if startVariable >10:
        #   break
       #print(startVariable)
       

start = 0
while start< 20:
       while True:
              start += 1
              print(start)
              if start >10:
                  break
              print("after if")



testList = [1,5,7]
for element in testList:
       if element == 5:
          continue  #we dont stop the loop but skip the rest loop and move to next element
       print(element)


for i in range(0,5,1):
   if i == 3:
     continue
   #print(i)

x = 0
while x <4:
    x += 1
    print(x)
    break
       

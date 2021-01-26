#if condition:
   #doApproritateThing

#elif differentCondition:  #else of
       #doMoreStuff
#elif condition3:
     # morestuff
#else:
       #doBaseCase/FallBack


number = 6
if number == 7:
       print ("this number is 7")
       
elif type(number) == type(7):
       print("same Type")
       
elif number ==6:
     print("this is number 6")
     
else:
  print("this is not a number nothing")


for num in range(10):
       print(num)
       if num%3 == 0:
             print("Divisible by 3")
       elif num%2 == 0:
             print("Divisible by 2")
       else:
             print("Not divisible by 2 or 3")


#something in something
#something  not in something

greeting = "Hello World"
checkWord = "Hello"
notCheck = "Good-Bye"

if checkWord in greeting:
 print("This is a Greeting")
else:
       print("this is not a Greeting")

if notCheck not in greeting:
 print("This not  a Greeting")
else:
       print("this is a Greeting")


if True:
       print("True")
else:
       print("False")

def inputChar (height , character ,outName):
            numberofLines= 3
            numberOs = 1
            for i in range(1,height):
                   whiteSpace = numberofLines - i
                   #print(" "*whiteSpace+ character *numberOs+" "*whiteSpace)
                   numberOs += 2
                   out = open(outName, "a")
                   out.write(str(" "*whiteSpace+ character *numberOs+" "*whiteSpace))
                   out.write("\n")
                   out.close()
inputChar(5, "*", "text.txt")






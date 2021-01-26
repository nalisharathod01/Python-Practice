def inputfile(outLoc):
    inputf = open("open.txt" , "r")
    fileContent = inputf.read()
    print("Contents of the File-" + " " + fileContent)
    print("Reverse Content of the file - " + " " +fileContent[::-1])
    inputf.close()
inputfile("")

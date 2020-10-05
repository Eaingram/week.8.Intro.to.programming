import os
import sys

directory=input("enter a directory to save the file in (for example C:/Python)")
isDirectory = os.path.isdir(directory)

if isDirectory == False:
    sys.exit("Error directory does not exist")

fileName=input("enter the filename you wish to save (for example file.txt)")

isFile = os.path.isfile(fileName)

print(isDirectory)
print(isFile)
filePath = directory + "/" + fileName

name=input("please enter your name")
address=input("please enter your address")
phoneNumber=input("please enter your phone number")

file = open(filePath, "w")
file.write(str(name) + "," + str(address) + "," + str(phoneNumber) + ",")
file.close

print ("printing file contents")

file = open(filePath, "r")
for line in file:
    print (line)
file.close

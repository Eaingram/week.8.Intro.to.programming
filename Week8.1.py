import os
import sys

directory=input("enter a directory to save the file in (for example C:\\Test)")
isDirectory = os.path.isdir(directory)

if isDirectory == False:
    os.mkdir(directory)

fileName=input("enter the filename you wish to save (for example file.txt)")
filePath = directory + "\\" + fileName

name=input("please enter your name")
address=input("please enter your address")
phoneNumber=input("please enter your phone number")

file = open(filePath, "w")
file.write(str(name) + "," + str(address) + "," + str(phoneNumber) + ",")
file.close

print("printing file contents")

file = open(filePath, "r")
for line in file:
    print(line)

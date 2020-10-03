import os

#------print working directory------
def printPWD() :
    pwd = os.getcwd()
    print (pwd)

#------change directory------
printPWD()
os.chdir('C:\\Users\\Nima\\Downloads')
printPWD()

#------is calc.exe file exist ?------
isExist = os.path.exists('C:\\Windows\\System32\\calc.exe')
print (isExist)

#------the size of calc.exe file------
size = os.path.getsize('C:\\Windows\\System32\\calc.exe')
print (size)

#------make a bunch of directories------
os.makedirs('C:\\Users\\Nima\\Desktop\\TestDir\\Waffles')

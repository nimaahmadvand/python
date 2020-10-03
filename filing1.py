#------RE-WRITE------
#echo "Hello Friend" > FirstOutput.txt
myfile = open ("FirstOutput.txt" , "w") #open the file
myfile.write ("Hello Friend")           #write in it
myfile.close ()                         #close it

#------APPEND------
#echo "Hello Friend" >> FirstOutput.txt
myfile = open ("FirstOutput.txt" , "a")
myfile.write ("\nHello")
myfile.write (" Friend")
myfile.close ()

#------READ------
myfile = open ("FirstOutput.txt" , "r")
content = myfile.read()
print (content)
myfile.close()


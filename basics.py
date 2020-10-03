#####################################
print ("------Variables & I/O------")
#name = input ("please enter your name: ")
foo = "Hello Friend"
bar = str (177013)
print (foo + "!" , bar)

##################################
print ("------if then else------")
age = 12
if age >= 21 :
    print ("you allow in & you allow to drink")
elif age >= 18 :
    print ("you allow in & you dont allow to drink")
else :
    print ("you dont allow in")
#+-+-+-+-+-+-+-+-+-
foo = "Hello"
bar = "Hello World"
if foo not in bar :
    print ("This is probably not a greeting")
else :
    print ("This is a greeting")
	
###########################
print ("------loops------")
num = 9
prime = True #a boolean to remember if this
         #number is prime or not
for i in range (2 , 10 , 1) : #2,3,...,9
    if num % i == 0 and num != i :
        print (num , '=' , i , '*' , num/i)
        prime = False
if prime :
    print (num , "is prime")
else :
    print (num , "is not prime")
#+-+-+-+-+-+-+-+-+-
names = ['ben' , 'all' 'mag']
for i in names :
    print (i , "is a greate person")
#+-+-+-+-+-+-+-+-+-
sum = 0
while sum < 10 :
    print (sum)
    sum += 1

#################################
print ("------Collections------")
list = [ 1 , 2.5 , "bob" , [3 , 4] ]
tuple = ( 1 , 2.5 , "bob" ) #a constatnt list
dictionary = {'fname':'nima' , 'lname':'ahmadvand' , 'age':22}
print (list , list , dictionary , sep='\n')
print (list[2]) #output -> bob
print (list[3][1]) #output -> 4
print (dictionary['fname'])
#+-+-+-+-+-+-+-+-+-
for i in range (0 , len(list)) :
    print (list[i] , "is found in index" , i)
for i in dictionary :
    print (i , '=' , dictionary[i])
#+-+-+-+-+-+-+-+-+-
list[2] = "alice"
list.append ("joe")
list.remove ("joe")
print (list[1:])
dictionary['age'] = 32 #replace
dictionary['height'] = 175 #add
del dictionary['lname']
print (dictionary)

###############################
print ("------Functions------")
#from func import *
#x = pow(2 , 10)
import func
x = func.pow(2 , 10)
print (x)
#+-+-+-+-+-+-+-+-+-
func.HW ()

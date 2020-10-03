print ("newton's second law of motion")
print ("a=F/m (a:acceleration ,  F:force , m:mass)")

F = input ("please enter the value of force: ")
m = input ("please enter the value of mass: ")
try :
    a = float(F) / float(m)
    print ("the value of acceleration is equal to: " , a)
except ZeroDivisionError :
    print ("error: you tried to divide by zero.")
except :
    print ("something else went wrong") #like entering a string for F or m

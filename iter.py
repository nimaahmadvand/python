from itertools import permutations
lst = []
n = int(input("Enter number of elements: "))
for i in range(0, n) :
    ele = input(">")
    lst.append(ele)
p = int(input("Enter number of permutations (---): "))
for x in range (2 , p+1) :
		perm = permutations(lst , x)
		lists = list(perm)
		myfile = open ("passlist.txt" , "a")
		for i in range(len(lists)) :
				  for j in range(x) :
				      myfile.write (lists[i][j])
				  myfile.write ("\n")
myfile.close()
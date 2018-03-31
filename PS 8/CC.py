#James Gardner
#Math of CS 202 PS 8
#October



#n= list of card numbers
#change list to check other numbers, list must be 15 digits long
n=[1,3,9,0,1,1,2,7,0,1,1,8,5,1,4] #cc number
nn=n[::2] #cc odd indice number
nnn=n[1::2] #cc even indice number

def odd(x):
	total = 0
	x=x[::2]
	for i in range(len(x)):
		if ((x[i])*2) > 9:
			st=str(x[i]*2)
			t=map(int,st)
			total += sum(t)
		else:
			total += x[i]*2
	return total

def even(y):
	total = 0
	y=y[1::2]
	total = sum(y)
	return total
	
total=sum([even(n),odd(n)])

#print(n)
print(nnn)
print(even(n))
print(nn)
print(odd(n))

lastNum=10-total%10	
n.append(lastNum)



#print(n)

print("The last digit is",lastNum,)

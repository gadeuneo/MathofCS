# James Gardner
# Math of CS 202, PS 8
# Eric Alexander

#Credit Card Number Analysis



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

def main():
	cont=True
	lastNum=0
	total=0
	while cont==True:
		legalChars="0123456789"
		numChars="0123456789"
		phrase=input("\nEnter Credit Card Number 15 digits long. Press enter to sumbit.\n".title())
		valid=False
		while valid==False:
			valid=True
			for i in phrase:
				if i not in legalChars or len(phrase) != 15:
					valid=False
			if valid==False:
				phrase=input("\nInvalid input. Please enter new number containing 15 numbers. Press enter to sumbit.\n".title())
			hasNum=False
			if valid==True:
				while hasNum==False:
					for k in phrase:
						if k in numChars:
							#print(phrase) #debug
							hasNum=True
					if hasNum==False:
						phrase=input("\nInvalid input. Please enter new number containing 15 numbers. Press enter to sumbit.\n".title())
						#print(phrase) #debug
						valid=False
		
		phrase=(list(map(int,str(phrase))))	
		#print(phrase) #debug
		total=sum([even(phrase),odd(phrase)])
		if total%10 ==0:
			lastNum=0
		else:
			lastNum=10-total%10
		print("The last digit is",lastNum,)
		prompt=input("\nDo you want to try another? Type 'yes' or 'no': \n".title())
		while len(prompt) ==0:
			prompt=input("\nDo you want to try another? Type 'yes' or 'no': \n".title())
		if prompt[0] in "nN":
			cont=False
		while prompt[0] not in "nNyY":
			print("\nplease enter yes or no \n".title())
			prompt=input("\nDo you want to try another? Type 'yes' or 'no': \n".title())
			if prompt[0] in "nN":
				cont=False
						
main()



#added by wankim
#thanks for reading
print "wankim's footprint"
print
print

# isPrime() - check if an input number is a prime number 
def isPrime(i):
	for j in range(2,i/2+1):
		if i%j :
			continue
		else :
			return 0
	return 1
	
def Mod2(i):
	if i%2 :
		print "It's ODD"
	else:
		print "It's EVEN"

something=raw_input("Type I Valuse : ")
i=int(something)
if ((i>=2)and (i <=9)):
	for j in range(2,10):
		print ("%s * %s : %s") %(i,j,int(i)*j)
	Mod2(i)
else:
	print "It's not my number "+str(i)

print "My TEST2 Python is finished"
print "JamLee added this line 20160119"
print "JamLee added this line AGAIN"
print "seulee added - 1"

# usage of isPrime()
if isPrime(i):
	print "\n%s is a prime number!\n" %(i)
else:
	print "\n%s is NOT a prime number!\n" %(i)



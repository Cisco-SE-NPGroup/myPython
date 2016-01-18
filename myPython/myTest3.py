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
print "My TEST2 Python is finished again"


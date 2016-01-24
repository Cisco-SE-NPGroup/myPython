i = raw_input("Enter Your Number:")

if (int(i)>=2) and (int(i)<=9):
	for j in range(2,10):
		k = int(i)*j
		print k
else:
	print "Wrong Number"


def xor(a , b):
	if (a == 1 and b == 1):
		t1 = 0
	else:
		t1 = 1
	if (a == 1 or b == 1):
		t2 = 1
	else:
		t2 = 0
	if (t1 == 1 and t2 == 1):
		return(1)
	else:
		return(0)
		

def halfadder(a, b):
	if(a == 1 and b == 1):
		return(1, xor(a, b))
	else:
		return(0, xor(a, b))
	
def fulladder(a, b, c = 0):
	c1, s1 = halfadder(a, b)
	c2, s_out = halfadder(s1, c)
	if (c1 == 1 or c2 == 1):
		c_out = 1
	else: 
		c_out = 0
	return(c_out, s_out)

def add(x, y):
	x_bin = []
	for i in bin(x)[2:]:
		x_bin.append(i)
	y_bin = []
	for i in bin(y)[2:]:
		y_bin.append(i)
	dif = len(x_bin) - len(y_bin)
	if (dif > 0):
		for i in list(range(0,dif)):
			y_bin = [0] + y_bin
	elif (dif < 0):
		for i in list(range(0,abs(dif))):
			x_bin = [0] + x_bin
	x_bin_rev = x_bin[::-1]
	y_bin_rev = y_bin[::-1]
	
	# Store binary result in reverse
	result = []
	for i in list(range(0, len(x_bin_rev))):
		# There is no carry for the first digit
		if (i == 0):
			c_out = 0
		c_out, s_out = fulladder(a = int(x_bin_rev[i]), b = int(y_bin_rev[i]), c = c_out)
		print(c_out, s_out)
		if (i < len(x_bin_rev) - 1):
			result.append(s_out)
		else:
			result.append(s_out)
			if (c_out == 1):
				result.append(c_out)
	return(result[::-1])
	
print(add(25675666555,2**256))

print(bin(25675666555+2**256))

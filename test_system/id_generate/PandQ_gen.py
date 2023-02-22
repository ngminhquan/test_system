import random
def euclid(a, b):
	r1 = a 
	r2 = b
	s1 = 1
	s2 = 0
	t1 = 0
	t2 = 1
	while(r2>0):
		q = r1//r2
		r = r1 - q*r2
		r1 = r2
		r2 = r 

		s = s1 - q*s2
		s1 = s2
		s2 = s 

		t = t1 - q*t2
		t1 = t2
		t2 = t 
	return r1, s1, t1

def listed(p,q):
	n = q* p
	phi = (p-1)*(q-1)
	result = []
	count = 0
	while(count < 10):
		num = random.randrange(2,n)
		a,b,c=euclid(phi,num)
		
		if a != 1:
			continue
			
		else:
			if c<0:
				c+=phi
			count+=1
			result.append([num,c])
	'''
	with open ("Caccapkey.txt", "w") as f:
		for i in range(10):
			for j in range(2):
				f.write(str(result[i][j])+"\n")
			f.write("\n")'''
	return ' '.join([str(result[i][j]) for i in range(1) for j in range(2)])
def rdnumfile(a):
	ret =""
	for i in a:
		if (i.isalnum()):
			ret+=i
		else:
			break
	return int(ret,16)
# Bat dau chuong trinh
x, y = 0, 0
with open ("PaQ.txt", "r") as f:
	
	x = rdnumfile(f.readline())
	
	y = rdnumfile(f.readline())

print(listed(x,y))

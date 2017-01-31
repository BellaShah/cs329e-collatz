

import random
def main():
	for d in range (10):
		a=random.randint(2,100)
		b=random.randint(2,100)
		print(str(a)+" "+str(b))
	for a in range (20):
		a=random.randint(1,100000)
		b=random.randint(1,100000)
		print(str(a)+" "+str(b))
	for b in range (20):
		a=random.randint(1,20000)
		b=random.randint(1,20000)
		print(str(a)+" "+str(b))
	for c in range (40):
		a=random.randint(1,999999)
		b=random.randint(1,999999)
		print(str(a)+" "+str(b))
	for i in range (20):
		a=random.randint(500000,999999)
		b=random.randint(500000,999999)
		print(str(a)+" "+str(b))
	for i in range (10):
		a=random.randint(1,999999)
		b=random.randint(1,1000)
		print(str(a)+" "+str(b))
	for i in range (5):
		a=random.randint(20000,30000)
		b=random.randint(10000,15000)
		print(str(a)+" "+str(b))
main()
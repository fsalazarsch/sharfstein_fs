#def factorial(n):
#	if n == 0 or n == 1:
#		return 1
#	return n*factorial(n-1); 

def factorial(n):
	fact =1
	if n == 1 or n==0:
		return fact
	else:
		for i in range (1,n+1):
			fact *= i
		return fact

def binomio(m,n):
	return int(factorial(m)/( factorial(n)*factorial(m-n)))

columnas = int(input())

if columnas == "":
	columnas = 10

for i in range(columnas):
	for j in range(int((columnas-i+1)/2)):
		print(end='\t')
	
	for j in range(i+1):
		print(binomio(i,j), end='\t')
	print()


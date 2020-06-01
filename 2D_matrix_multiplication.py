R1 = int(input("Enter the number of rows:")) 
C1 = int(input("Enter the number of columns:")) 

matrixA = [] 
print("Enter the entries rowwise:") 

for i in range(R1):		 
	a =[] 
	for j in range(C1):	 
		a.append(int(input())) 
	matrixA.append(a) 
 
for i in range(R1): 
	for j in range(C1): 
		print(matrixA[i][j], end = " ") 
	print()
R2 = int(input("Enter the number of rows:")) 
C2 = int(input("Enter the number of columns:"))  
matrixB = [] 
print("Enter the entries rowwise:") 
 
for i in range(R2):		  
	a =[] 
	for j in range(C2):	  
		a.append(int(input())) 
	matrixB.append(a) 
 
for i in range(R2): 
	for j in range(C2): 
		print(matrixB[i][j], end = " ") 
	print() 

result = [] 
print("Enter the entries rowwise:") 
 
for i in range(R1):		  
	a =[] 
	for j in range(C2):	 
		a.append(int('0')) 
	result.append(a)

for i in range(len(matrixA)):
   for j in range(len(matrixB[0])):
       for k in range(len(matrixB)):
           result[i][j] += matrixA[i][k] * matrixB[k][j]

for r in result:
   print(r)
 

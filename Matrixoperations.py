X, Y = map(int,(input("Enter the sizes of 1st matrix : ").split()))  
matrixX = [] 														   

for i in range(X): 													  
	print("Enter the",i,"row elements:")
	matrixX.append((list)(input().split()))

print(matrixX) 														   

x,y = map(int,(input("Enter the sizes of 2nd matrix :").split()))
matrixY = []
for j in range(Y):
	print("Enter the",j,"row elements: ")
	matrixY.append((list)(input().split()))

print(matrixY)

addition = [] 														 
addlist = []
if(X == x and Y == y):												   
	for a in range(X):
		for b in range(Y):
			addlist.append(int(matrixX[a][b]) + int(matrixY[a][b]))
			addition.append(addlist)

print("addition of given matrices:",addition)

subtraction = [] 														   
sublist = []
if(X == x and Y == y):												   
	for c in range(X):
		for d in range(Y):
			sublist.append(int(matrixX[c][d]) - int(matrixY[c][d]))
			subtraction.append(sublist)
print("Subtraction of the given matrices :",subtraction)



multiplication = []
multilist = []
for l in range(c):
	for m in range(y):
		for n in range(d):
			multilist.append(int(matrixX[l][n])*int(matrixY[n][m]))
			multiplication.append(multilist)
print("multiplication of the given matrices:",multiplication)
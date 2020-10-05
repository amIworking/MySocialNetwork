matrix=[]
stroka=int(input("How many strok you need?\n"))
stolbec=int(input("How many stolbcov you need?\n"))
#number=int(input("Input numbers in the matrix\n"))
print("Input numbers in the matrix:\n")
for i in range(stroka):
        testMatrix=[]
        for j in range(stolbec):
                testMatrix.append(int(input()))
        matrix.append(testMatrix)
for i in matrix:
        print(i)


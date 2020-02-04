# function declaration

def print_matrix(matrix):
    for row in range(0,len(matrix)):
        print(matrix[row])

def swap_row(matrix,row1,row2):
    for i in range(0,len(matrix)+1):
        temp=matrix[row1][i]
        matrix[row1][i]=matrix[row2][i]
        matrix[row2][i]=temp
def scale_row(matrix,row,factor):
    for i in range(0,len(matrix)+1):
        matrix[row][i]=float(matrix[row][i])*float(factor)
def add_to_row(matrix,rowTarget,rowSource,factor):
    for i in range(0,len(matrix)+1):
        matrix[rowTarget][i]=float(matrix[rowTarget][i])+float(matrix[rowSource][i])*float(factor)


size=float(input("Enter the size of the matrix: "))
#initializing list with rows and columns: extra column for constant term
matrix=[[] *(int(size)+1) for i in range(int(size))]
for row in range(0,int(size)):
    for column in range(0,int(size)+1):
        matrix[int(row)].append(input("Enter row "+str(row+1)+" column "+str(int(column)+1)+": "))


print("The size of the matrix is :",len(matrix))
print("The original matrix is:\t")
print_matrix(matrix)


# matrix reducing loop
for row in range(0,len(matrix)):
    # while the first element is 0, swap until it is not
    if float(matrix[row][row])==0:
        swap=0
        while matrix[swap][swap]==0:
            swap+=1
        swap_row(matrix,row,swap)
    # now the row we're on is not 0 in the diagonal
    scale_row(matrix,row,1.0/float(matrix[row][row]))
    for i in range(0,len(matrix)):
        if i!=row:
            add_to_row(matrix,int(i),int(row),-float(matrix[i][row]))

# making the numbers nice
for row in range(0,int(size)):
    for column in range(0,int(size)+1):
        matrix[row][column]=round(float(matrix[row][column]),4)
        if float(matrix[row][column])==0:
            matrix[row][column]=float(0)

# final print
print("\nThe RREF form is:")
print_matrix(matrix)



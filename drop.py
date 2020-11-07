def corner(matrix,i,j):#ith row, j th column
    if j==0 and matrix[i][j]=='\' and matrix[i][j+1]=='\':
        return i+1,j+1
    elif j==len(matrix[0])-1 and matrix[i][j-1]=='/' and matrix[i][j]=='/':
        return i+1,j-1
    else:
        return -1,-1
def middle(matrix,i,j): #ith row, jth column
    if matrix[i][j-1]=='/' and matrix[i][j]=='/':
        return i+1,j-1
    elif matrix[i][j]=='\' matrix[i][j+1]=='\' :
        return i+1,j+1
    else:
        return -1,-1
def run(matrix,i,j):
    while i!=-1 and j!=-1 and i!=len(matrix)-1:
        if j==0 or j==len(matrix[0])-1:
            i,j = corner(matrix,i,j)
        else:
            i,j = middle(matrix,i,j)
    if i==-1 or j==-1:
        return -1
    else:
        return j
def main(matrix):
    result = []
    i = 0
    for j in range(len(matrix[0])): # for each ball
        result.append(run(0,j))

        
        

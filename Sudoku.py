def check_valid_sudoku(l):
    lenght1=len(l)
    p=[]
    length2=len(l[0])
    digit=1 #starts with checking number 1
    if(lenght1!=length2):#checks if it's a square matrix
        return False
    else:
        while(digit<=lenght1): #for all numbers from 1 to l(square matrix)
            i=0
            while i<lenght1:  #for row traversal
                row=0         #number of row occurences of the digit
                col=0           #no. of col occurences
                j=0
                while j < lenght1:
                    if digit==l[i][j]: #checking row
                        row+=1
                    if digit==l[j][i]:  #checking column
                        col+=1
                    j+=1
                if row!=1 or col!=1:  #a number can only occur once in it's row and column otherwise not sudoku
                    return False
                i+=1
            digit+=1
        return True  #if the loop doesn't break the matrix is a legit sudoku
list=[[1,2,3,4],[3,4,1,2],[2,3,4,1],[4,1,2,3]]

print check_valid_sudoku(list)
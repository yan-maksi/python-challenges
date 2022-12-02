""" 
-- Task - Using smart logic, loops, and algorithms to output the mirror image of an identity matrix --
An identity matrix is defined as a square matrix with 1's running from the 
top left of the square to the bottom right. The rest are 0's. The identity 
matrix has applications ranging from machine learning to the general theory of relativity.

Examples of identity matrix:
    Input :  4
    Output : 1 0 0 0
             0 1 0 0
             0 0 1 0
             0 0 0 1

Examples of mirror image of identity matrix:
    Input :  4
    Output : 0 0 0 1
             0 0 1 0
             0 1 0 0
             1 0 0 0
"""
# Here is the code that generates an nxn identity matrix:-
print()
print("Identity matrix") 
for row in range(0, size):
    for col in range(0, size):

       # Here end is used to stay in same line
      if (row == col):
          print("1 ", end=" ")
      else:
          print("0 ", end=" ")
    print()  
     
#  my code (mirror image of identity matrix):
def matrix_mirror(size):
    if isinstance(size, int):
        print()
        print("Identity matrix")
        list_matrix = []
        for row in range(0, size):
            for col in range(0, size):
                
                # Here end is used to stay in same line
                if row == col:
                    list_matrix.append(1)
                    print(1, end=" ")
                else:
                    list_matrix.append(0)
                    print(0, end=" ")
            print()

        print()
        # convert list matrix to normal matrix
        matrix = [list_matrix[i:i + size] for i in range(0, len(list_matrix), size)]
        # creating an empty array to store the reversed column matrix
        reversed_matrix = []
        # looping through matrix_1 and appending matrix_2
        for i in range(len(matrix)):
            reversed_matrix.append(matrix[i][::-1])
        print('Mirrored identity matrix:')
        for rev_matrix in reversed_matrix:
            print(*rev_matrix)
    else:
        print("Error")


if __name__ == "__main__":
    size = int(input("Identity matrix size: "))
    matrix_mirror(size)


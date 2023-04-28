#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix,div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
    

    size=None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats") 
            
        if size is None:
            size=len(row)

        elif len(row)!=size:
            raise TypeError("Each row of the matrix must have the same size") 
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")  
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number") 
        if div==0:
            raise ZeroDivisionError("division by zero") 
    new_matrix=[]
    for row in matrix:
        new_row=[]
        for i in row:
            new_row.append(round(i/div,2))
        new_matrix.append(new_row)    
    return new_matrix             


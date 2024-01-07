#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): The number to divide each element of the matrix.

    Returns:
        list: A new matrix with elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Define an error message for invalid matrices
    errorMessage = "matrix must be a matrix (list of lists) of integers/floats"
    
    # Check if the matrix is not empty and is a list
    if not matrix or not isinstance(matrix, list):
        raise TypeError(errorMessage)
    
    # Validate the matrix elements
    for lists in matrix:
        """
        Each element in the matrix must be a list,
        and each item in the lists must be an integer or a float.
        Each list in the matrix must not be empty.
        """
        if not isinstance(lists, list):
            raise TypeError(errorMessage)
        
        for item in lists:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError(errorMessage)
            
        if len(lists) == 0:
            raise TypeError(errorMessage)
    
    # Check if div is a number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    # Check if all rows of the matrix have the same size
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Perform the matrix division and rounding
    return [[round(item / div, 2) for item in lists] for lists in matrix]

# Example usage:
if __name__ == "__main__":
    matrixA = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
    matrixB = [[1, 2, 3], [4, 5, 6]]

    # Valid cases
    resultA = matrix_divided(matrixA, 4)
    resultB = matrix_divided(matrixB, 3)
    print(resultA)
    print(resultB)

    # Invalid cases
    try:
        matrix_divided(None, 3)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        matrix_divided([], 2)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        matrix_divided([[1], [2, 3], [4, 5, 6]], 3)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        matrix_divided(matrixA, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")


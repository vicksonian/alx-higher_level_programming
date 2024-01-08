#!/usr/bin/python3
"""
Module to perform lazy matrix multiplication using NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function to perform lazy matrix multiplication using NumPy

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix

    Returns:
        numpy.ndarray: Result of matrix multiplication
    """
    # Perform matrix multiplication using NumPy
    return numpy.matmul(m_a, m_b)

#!/usr/bin/python3
"""A module that contains the function 'lazy_matrix_mul'"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """returns the product of two conformable matrices in a lazy way"""
    return np.matmul(m_a, m_b)

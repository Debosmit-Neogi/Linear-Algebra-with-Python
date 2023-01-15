#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:20:32 2023

@author: debosmit2001
"""

import numpy as np
from scipy.linalg import svd

""" A = U * sigma * V_transpose

   A = M x N
   U = M x R (R = Rank of matrix A)
   sigma = R x R
   V = N x R
=> V_transpose = R x N

"""
A = np.array([[3, 1, 1], [-1, 3, 1]])
U, Sigma, V_transpose = svd(A)
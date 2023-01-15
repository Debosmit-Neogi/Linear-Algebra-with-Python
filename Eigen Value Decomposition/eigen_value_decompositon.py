#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 10:55:26 2023

@author: debosmit2001
"""

import numpy as np

# Perform eigendecomposition of matrix A

A = np.array([[0,1],[-2,3]])

#print(A)

lamda, U = np.linalg.eig(A)

#print(lamda)

"""Decomposition is as follows:
   
    A = U * diag(lamda) * U_inverse
    """

component1 = U
component2 = np.diag(lamda)
component3 = np.linalg.inv(U)
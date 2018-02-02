# -*- coding: utf-8 -*-
"""
Implements the algorithm of iteratively reweighted least squares
for approximating a solution to a l_0-minimization problem, which reads as

min ||x||_0 s.t. Ax = b

for given matrix A and vector b and it is described and analyzed in [IRLS]_.
"""

import numpy as np
import numpy.linalg as npl


def recover(mat_A, arr_b, num_eps, num_s, verbose=0):
    """
        Iteratively Reweighted Least Squares

    Parameters
    ----------

    mat_A : ndarray
        system matrix
    arr_b : ndarray
        measurement vector
    num_eps : float
        stopping criterion
    num_steps : int
        iteration steps

    Returns
    -------
    ndarray
        estimated sparse solution
    """

    num_s = int(num_s)
    num_n, num_m = mat_A.shape
    arr_w = np.ones(num_m)
    num_thrs = 1

    arr_x = np.ones(num_m)
    arr_x_o = np.zeros(num_m)

    num_s = 0

    while npl.norm(arr_x - arr_x_o) > num_eps and num_s < num_steps:
        mat_D = np.diag(1.0/arr_w)
        arr_x_o = arr_x
        arr_x = mat_D.dot(LA.H(mat_A)).dot(
            npl.solve(mat_A.dot(mat_D.dot(LA.H(mat_A))), arr_b))
        num_thrs = min(num_thrs, num_eps*(-np.sort(-arr_x))[num_s])
        if verbose == 1:
            print(num_thrs)
        arr_w = 1/np.sqrt(np.abs(arr_x)**2 + num_thrs**2)
        num_steps += 1

    return(arr_x*(np.abs(arr_x) > num_eps*(-np.sort(-arr_x))[num_s]))

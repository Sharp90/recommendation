import pandas as pd
import numpy as np


def gp_ucb(D, sigma_zero, ker_mode, beta):
    mu = 0
    sigma = sigma_zero
    cul_reg = 0
    t = 1
    
    # linear function
    if ker_mode == 0:
        ker_func = lambda x,y: x.dot(y)
    # polynomial function
    elif ker_mode == 1:
        ker_func = lambda x,y: ((x.dot(y)) * gamma + coef0) ** degree
    # radial basis function(RBF)
    elif ker_mode == 2:
        ker_func = lambda x,y: np.exp(-(np.linalg.norm(x - y) ** 2))
    else:
        exit(1)
        
    while(1):
        if t != 1:
            mu = 
            sigma = 
        
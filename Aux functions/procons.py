# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:59:47 2023

@author: 42845
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, gamma, norm 
import utils as utils

def procons(p1, p2, alpha_1, alpha_2, N, sigma):
    PR = 0
    M = np.arange(1, N)
    for j in M:
        PR = PR + utils.prob_client_decision(p1, p2, sigma[j])
    return PR/(N-1)


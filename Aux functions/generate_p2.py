# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 17:08:30 2023

@author: 42845
"""
import numpy as np
import utils as utils

def generate_p2(p1_samples, alpha_1, alpha_2, N, value_2, init_price, price_step):
    SAMPLE = []
    prices_r2 = np.arange(value_2, init_price, price_step)
    p1 = p1_samples
    sigma = list(utils.sigma_2_client_decision(alpha_1, alpha_2, N))
    for p in p1:
        for sig in sigma:
            MAX = -N
            for p2 in prices_r2:
                h_p2 = (p2-value_2)*np.sum(utils.prob_client_decision(p2, p, sig))
                if h_p2 > MAX:
                    MAX = h_p2
                    SAMPLE_utility = p2
            SAMPLE = np.append(SAMPLE, SAMPLE_utility)
    return SAMPLE
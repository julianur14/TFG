# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:02:30 2023

@author: 42845
"""
import procons as pc
import numpy as np

def pricing(p2_samples, prices_r1, alpha_1, alpha_2, p_val, N, value_1):
    MAX = -N
    list_probs = []
    util = []
    for price_1 in prices_r1:
        phi = 0
        for price_2 in p2_samples:
            MAX_2 = -N
            phi = phi + (price_1-value_1)*pc.procons(price_1, price_2, alpha_1, alpha_2, N)
            if phi > MAX_2:
                MAX_2 = phi
        list_probs = np.append(list_probs, pc.procons(price_1, price_2, alpha_1, alpha_2, N))
        util = np.append(util, (price_1-value_1)*pc.procons(price_1, price_2, alpha_1, alpha_2, N))
        if phi > MAX:
            MAX = phi
            OPT = price_1
            prob = pc.procons(price_1, price_2, alpha_1, alpha_2, N)
    return OPT, prob, list_probs, util

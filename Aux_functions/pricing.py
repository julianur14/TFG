# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:02:30 2023

@author: 42845
"""
import Aux_functions.procons as pc
import numpy as np

def pricing(p2_samples, prices_r1, alpha_1, alpha_2, p_val, N, value_1, sigma):
    MAX = -N
    list_probs = []
    util = []
    for price_1 in prices_r1:
        print(price_1)
        phi = 0
        probs = 0
        for price_2 in p2_samples:
            #MAX_2 = -N
            phi = phi + (price_1-value_1)*pc.procons(price_1, price_2, alpha_1, alpha_2, N, sigma)
            probs = probs + pc.procons(price_1, price_2, alpha_1, alpha_2, N, sigma)
            #if phi > MAX_2:
                #MAX_2 = phi
        #list_probs = list_probs.append(pc.procons(price_1, price_2, alpha_1, alpha_2, N, sigma))
        list_probs = np.append(list_probs, probs/len(p2_samples))
        util = np.append(util, phi)
        if phi > MAX:
            MAX = phi
            OPT = price_1
            prob = probs
            #prob = pc.procons(price_1, price_2, alpha_1, alpha_2, N, sigma)
    return OPT, prob, list_probs, util


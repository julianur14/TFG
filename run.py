# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:04:23 2023

@author: 42845
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, gamma, norm 
from pricing import pricing
from set_config import read_json
import utils as utils
from inverse_transform import inverse_transform_sampling
from generate_p2 import generate_p2

config = read_json("C:/Users/42845/Documents/TFG/config.json")
def run_pricing(config):
    #Define params from config
    lower_lim = config["lower_lim"]
    upper_lim = config["upper_lim"]
    min_value = config["min_value"]
    max_value = config["max_value"]
    poly_degree = config["poly_degree"]
    n_steps = config["n_steps"]
    n_samples = config["n_samples"]
    p_val = np.linspace(lower_lim, upper_lim, n_steps)
    alpha_1 = config["alpha_1"]
    alpha_2 = 1/config["alpha_2"]
    N = config["N"]
    value_1 = config["value_1"]
    value_2= config["value_2"]
    init_price_1 = config["init_price_1"]
    init_price_2 = config["init_price_2"]
    price_step = config["price_step"]
    
    #Generate p1 samples
    p1_samples = inverse_transform_sampling(n_samples, lower_lim, upper_lim, min_value, max_value, poly_degree, p_val)
    
    #Paint the samples
    probs = np.array([utils.unnorm_pdf(x, min_value, max_value, poly_degree) for x in p_val])
    plt.cla()
    plt.hist(p1_samples, bins = 50, density = True)
    plt.plot(p_val, probs * utils.analytic_norm_constant_q2_p1(p_val, probs), linewidth = 3)
    plt.show()
    
    #Generate p2 samples
    p2_samples = generate_p2(p1_samples, alpha_1, alpha_2, N, value_2, init_price_2, price_step)
        
    #Fix final price for p1
    prices_r1 = np.arange(value_1, init_price_1, price_step)
    final_price = pricing(p2_samples, prices_r1, alpha_1, alpha_2, p_val, N, value_1)
    
    return final_price
    
a = run_pricing(config)

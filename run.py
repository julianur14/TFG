# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 13:04:23 2023

@author: 42845
"""
import numpy as np
import pandas as pd
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
    poly_degree = config["poly_degree"]
    n_steps = config["n_steps"]
    n_samples = config["n_samples"]
    price_step = config["price_step"]
    p_val = np.arange(lower_lim, upper_lim, price_step)
    alpha_1 = config["alpha_1"]
    alpha_2 = 1/config["alpha_2"]
    N = config["N"]
    value_1 = config["value_1"]
    value_2= config["value_2"]
    init_price_1 = config["init_price_1"]
    init_price_2 = config["init_price_2"]
    sigma = list(utils.sigma_2_client_decision(alpha_1, alpha_2, N))
    #sigma = np.ones(10)*0.001
    #Generate p1 samples for retailer 2 
    p1_samples = inverse_transform_sampling(n_samples, lower_lim, upper_lim, value_1, init_price_1, poly_degree, p_val)

    #Paint the samples
    probs = np.array([utils.unnorm_pdf(x, value_1, init_price_1, poly_degree) for x in p_val])
    plt.cla()
    plt.hist(p1_samples, bins = 50, density = True)
    plt.plot(p_val, probs * utils.analytic_norm_constant_q2_p1(p_val, probs), linewidth = 3)
    plt.show()
    
    #Generate p2 samples
    #p2_samples = generate_p2(p1_samples, alpha_1, alpha_2, N, value_2, init_price_2, price_step, sigma)
    p2_samples = np.ones(100)*30

    #Fix final price for p1
    prices_r1 = np.arange(value_1, upper_lim, price_step)
    final_price, prob, list_probs, util = pricing(p2_samples, prices_r1, alpha_1, alpha_2, p_val, N, value_1, sigma)
    
    return prices_r1, p1_samples, p2_samples, final_price, prob, list_probs, util, sigma
    
a, b, c, d, e, f, g, h= run_pricing(config)

"""
df = pd.DataFrame()
df['prices'] = a
df['probs'] = f
df['utils'] = g
plt.plot(df)
df.plot.scatter(x = 'prices', y = 'probs')
df.plot.scatter(x = 'prices', y = 'utils')

plt.plot(a, f, color = 'red')
plt.plot(a, g, color = 'blue')
plt.show()
"""

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('price (€)')
ax1.set_ylabel('probs', color=color)
ax1.plot(a, f, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('utilities', color=color)  # we already handled the x-label with ax1
ax2.plot(a, g, color=color)
ax2.tick_params(axis='y', labelcolor=color)
max_index = np.argmax(g)
ax2.axvline(a[max_index], color = 'green', linestyle = '--')

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()

"""
Experimentos:
    guardar plot (save_fig) https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html (tamaño decente)
    ejecutar pruebas diferentes e intentar sacar conclusiones y ejemplos curiosos
    ejemplo: precios cada 0.5 con p2 alto, p2 bajo, p2 intermedio y sigmas muy bajos
    ejemplo: manteniendo p2 fijo (en 25 p.e.) probar a cambiar sigma pero que no tengan mucha variabilidad https://en.wikipedia.org/wiki/Gamma_distribution
    usar alpha diferentes (pdf de la gamma cerca del 0 pintar en python y probar)
    ejemplo: mantener sigma fijo (muy pequeños) y cambiamos los p2 y probamos
    """
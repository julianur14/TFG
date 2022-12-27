import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, gamma, norm

#parte de Simon
min_value = 1
max_value = 5
n = 1
n_steps = 100
p_val = np.linspace(0,6, n_steps)

def unnorm_pdf(x, min_value, max_value, n):

    if ((min_value < x) and (x <= max_value)):
        y = (x - min_value)**n
    else:
        y = 0

    return y
    
def norm_constant_q2_p1(prices_probs, available_prices):
    # return (1/np.trapz(y = available_prices, x = prices_probs)) # scipy.metrics area under curve (auc)
    return (1/np.sum(available_prices))

probs = np.array([unnorm_pdf(x, min_value, max_value, n) for x in p_val])
norm_const = norm_constant_q2_p1(p_val, probs)

# plt.plot(p_val, probs * norm_const, 'k-')
n_steps = 100
p_val = np.linspace(0,6, n_steps)
def cdf(x, norm_const = norm_const):
    avail_p = p_val[p_val < (x + 0.001)]
    cum_probs = np.sum( np.array([unnorm_pdf(y, min_value, max_value, n) for y in avail_p]) )
    return norm_const * cum_probs

cdf_vals = np.array([cdf(x) for x in p_val])

print(norm_const)
print(np.sum(probs))
print(np.sum(norm_const * probs))

unif = np.random.uniform(size = 100)
test = []
for i in np.arange(np.size(unif)):
    test.append(cdf_vals[np.argmin(np.abs(cdf_vals - unif[i]))])

print(unif)
print(test)


plt.plot(p_val, cdf_vals,'k-')
# plt.show()

#En teoría hasta aquí genera las muestras de la distribución de p2, pero no termino de entenderlo bien y no parece funcionar pues los valores de la lista se encuentran entre 0 y 1

#Definimos la función de la sigma (más adelante esto podría ir en un archivo tipo utils con funciones auxiliares para varios scripts

def sigma_2_client_decision(alpha_1, alpha_2, N):
    """
    Obtain a sample from the sigma^2 for the client decision

    Input:
        alpha_1
        alpha_2

    Output:
        (gamma distribution sampled in value (x) with parameters alpha_1, alpha_2
    """

    # Client's decision variance
    return np.random.gamma(alpha_1, alpha_2, N)

def prob_client_decision(price_1, price_2, sigma_2):
    """
    Obtain the probability that the client chooses a given offer

    Input:
        price_1
        price_2
        sigma_2
        
    Output:
        (gamma distribution sampled in value (x) with parameters alpha_1, alpha_2
    """

    # The default Normal distribution is already the standard N(0,1)
    return 1 - norm.pdf((price_1 - price_2) / sigma_2)


#Aquí estaría la función main, donde los test los meto directamente del código de Simón de la parte superior (por eso está comentado el cálculo)
    
def generate_p2_2(p_val, alpha_1, alpha_2, N, value_2, init_price, price_step, test):
    SAMPLE = []
    v2 = 7
    prices_r2 = np.arange(value_2, init_price, price_step)
#    cdf_vals = np.array([cdf(x) for x in p_val])
 #   unif = np.random.uniform(size = 100)
  #  test = []
   # for i in np.arange(np.size(unif)):
    #    test.append(cdf_vals[np.argmin(np.abs(cdf_vals - unif[i]))])
    p1 = test
    sigma = list(sigma_2_client_decision(alpha_1, alpha_2, N))
    #   sigma = sigma.append(sigma_2_client_decision(alpha_1, alpha_2, N)[j])
    for p in p1:
        for sig in sigma:
            MAX = -N
            for p2 in prices_r2:
                h_p2 = (p2-v2)*np.sum(prob_client_decision(p2, p, sig))
                if h_p2 > MAX:
                    MAX = h_p2
                    SAMPLE_utility = p2
            SAMPLE = np.append(SAMPLE, SAMPLE_utility)
    return SAMPLE

#Prueba
a = generate_p2_2(p_val, 2, 1/2, 100, 7, 40, 0.5, test)        

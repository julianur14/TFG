import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, gamma, norm 


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
    return 1 - norm.cdf((price_1 - price_2) / sigma_2)


def procons(p1, p2, alpha_1, alpha_2, N):
    PR = 0
    M = np.arange(1, N)
    sigma = sigma_2_client_decision(alpha_1, alpha_2, N)
    for j in M:
        PR = PR + prob_client_decision(p1, p2, sigma[j])
    return PR/N


#Some tests
a = procons(3, 5, 1, 1/2)
a = sigma_2_client_decision(2, 1/2, 1000)
plt.hist(a, bins = 10)
def count(a):
    M = np.arange(1, 100)
    b = 0
    for i in M:
        if a[i] == 0:
            b += 1
    return b
b = count(a) 

        
#plt.plot(a, color = 'magenta', marker = 'o', mfc = 'pink')
#plt.xticks(range(0,len(a)+1, 1))
#plt.ylabel('a')
#plt.xlabel('index')
#plt.title("Plotting gamma")
#plt.show()













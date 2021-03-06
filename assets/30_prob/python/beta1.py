
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from scipy.stats import beta
fig, ax = plt.subplots(1, 1)

with PdfPages('beta1.pdf') as pdf:
    a, b = 2, 2
    x = np.linspace(beta.ppf(0.00, a, b), beta.ppf(1, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b),'r-', lw=2, alpha=1, label='beta pdf')

    a, b = 1, 1
    x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b),'k-', lw=2, alpha=1, label='beta pdf')


    a, b = .5, .5
    x = np.linspace(beta.ppf(0.05, a, b), beta.ppf(0.95, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b),'b-', lw=2, alpha=1, label='beta pdf')

    a, b = 10, 10
    x = np.linspace(beta.ppf(0.00, a, b), beta.ppf(1, a, b), 1000)
    ax.plot(x, beta.pdf(x, a, b),'c-', lw=2, alpha=1, label='beta pdf')

    a, b = 0.2, .2
    x = np.linspace(beta.ppf(0.25, a, b), beta.ppf(.75, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b),'g-', lw=2, alpha=0.6, label='beta pdf')

    plt.text(0.5, .09, r'(0.2, 0.2)', fontsize=12, color = 'green')
    plt.text(0.5, .4, r'(0.5, 0.5)', fontsize=12, color = 'blue')
    plt.text(0.5, 1.1, r'(1, 1)', fontsize=12, color = 'black')
    plt.text(0.4, 1.6, r'(2, 2)', fontsize=12, color = 'red')
    plt.text(0.4, 3.6, r'(10, 10)', fontsize=12, color = 'c')

    ax.set_yticks([])
    plt.xlim([0,1])
#     plt.ylim([0,6])
#     plt.axis('equal')
    plt.xlabel('$\lambda$', fontsize = 15)
    plt.ylabel('$(\lambda)$', fontsize = 15)
    # ax.set_yscale('linear')

    # pdf.savefig()
    plt.show()
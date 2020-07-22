import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
import seaborn as sns
import streamlit as st


"""
# Fair/Unfair Coin Simulator
We toss a coin (N) times and record N_H heads, is the coin fair?
"""

x = st.slider('underlying probability of getting a head (we are unaware of this value): ', 0.0, 1.0)

df_N = pd.DataFrame({
                   'N': [50, 100, 200, 300, 400, 500, 1000, 2500]
                   })

df_Nsim = pd.DataFrame({
                   'Nsim': [500, 1000, 5000, 10000, 15000]
                   })

#
N = st.sidebar.selectbox(
    'N: Number of coin tosses: ',
    df_N['N'])


N_sim = st.sidebar.selectbox(
    'N_sim: Number of simulated N coin tosses: ',
    df_Nsim['Nsim'])


#'You selected:', x
r'$\mathcal{H}_0$', '(Null Hypothesis): Coin is fair'

# Fair coin
coin = np.array(['H', 'T'])

# Toss a fair coin 900 times
fair_coin = np.random.choice(coin, size = N, p = [x, 1-x])

# Repeat the above line 10,000 times
fair_coin_sample = np.array([np.sum(np.random.choice(coin, size = N, p = [0.5, 0.5]) == 'H')
                                     for i in range(N_sim)])
ci_low, ci_high = np.percentile(fair_coin_sample, [2.5, 97.5])

N_H = np.sum(fair_coin == 'H')
'Number of heads: ', N_H

#condition = 'fiar' if
if N_H > fair_coin_sample.mean():

    p_value = 2 * np.mean(fair_coin_sample >= N_H)

else:

    p_value = 2 * np.mean(fair_coin_sample <= N_H)

'p-value: ', np.round(p_value, 4)



'The observed p-value is ','smaller' if p_value <= 0.05 else 'larger ', 'than 0.05 so we ', 'reject' if p_value <= 0.05 else 'are unable to reject', 'the null hypothesis.'

condition = 'not fair' if p_value <= 0.05 else 'fair'

'If we toss a coin ', N, ' times and record ', N_H, ' heads the coin is ', condition,'.'

plt.figure(figsize = (7, 5))

plt.vlines(fair_coin_sample.mean(), 0, 0.028, color = 'crimson', linestyle = '-', label = 'Mean of '+str(N_sim)+' simulations', lw = 2.5)
plt.vlines(ci_low, 0, 0.02, color = 'tomato', linestyle = '--', label = '95% Confidence Interval', lw = 2)
plt.vlines(ci_high, 0, 0.02, color = 'tomato', linestyle = '--', lw = 2)
plt.vlines(N_H, 0, 0.025, color = 'dodgerblue', linestyle = '-', label = str(N_H)+" (Observed Number)", lw = 2.5)
sns.distplot(fair_coin_sample, hist = 'True', kde = True, bins = 15, color = 'teal')
#plt.ylim([0.0, 0.045])


st.markdown("""
                Made by [Nareg Mirzatuny](https://github.com/NaregM)                                     
Source code: [GitHub](
                https://github.com/NaregM/coin_simulator) 
                
""")

















plt.margins(0.3)
plt.legend(prop = {'size': 8})

st.pyplot()

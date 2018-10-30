
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math 
from scipy.stats import binom


# In[16]:


# Define the variable 
num_of_question = 20

# probability of wrong answer of a single question
prob_wrong_answer = 3/4  # as one of the 4 question is right
print('Probality of wrong answer of a single question:\t', prob_wrong_answer)

print('\nProbability of 5 wrong answers')
print('----------------------------')
print('\nSolution -1 - Mathemetical Model')
print('\t Using Formula: 20C5 * power((1-prob_wrong_answer),15) * power(prob_wrong_answer, 5)')

p_five_wrong_answer = (math.factorial(20)/(math.factorial(15)*math.factorial(5)))                       * math.pow((1-prob_wrong_answer),15) * math.pow(prob_wrong_answer,5)
print('\nProbability of 5 wrong answers',p_five_wrong_answer)

print('\nSolution -2 - Using scipy - probability mass function')
print('\t Using Formula: binom.pmf(5,total_num_of_question,p_wrong_answer)')

p_five_wrong_answer=binom.pmf(5,num_of_question,prob_wrong_answer)
print('\nProbability of 5 wrong answers',p_five_wrong_answer)


# In[17]:


# Define the variable 
num_of_roll = 50

# probability of getting D in single roll 
prob_D = 1/5  # as in a roll, D has equal chance among A to E
print('Probability of getting D in single roll:\t', prob_D)

print('\nProbability of getting D exactly 5 times')
print('--------------------------------------')
print('\nSolution -1 - Mathemetical Model')
print('\t Using Formula: 50C5 * power((1-prob_D),45) * power(prob_D, 5)')

p_five_D = (math.factorial(50)/(math.factorial(45)*math.factorial(5)))                       * math.pow((1-prob_D),45) * math.pow(prob_D,5)
print('\nProbability of getting D exactly 5 times',p_five_D)

print('\nSolution -2 - Using scipy - probability mass function')
print('\t Using Formula: binom.pmf(5,total_num_of_roll,p_D)')

p_five_D=binom.pmf(5,num_of_roll,prob_D)
print('\nProbability of 5 wrong answers',p_five_D)


# In[18]:


# Define the variable 
num_of_balls = 10
num_of_red_balls = 4
num_of_black_balls = 6

# Two balls are drawn at random in succession without replacement
# If Red ball is denoted by R and Balck ball is denoted by B then
# Possible outcome - RR, RB, BR, BB
# probability of 1st ball red = 4/10
# probability of 2nd ball red = 3/9 [when first ball is red]
# probability of 2nd ball red = 4/9 [when first ball is black]
# probability of 1st ball black = 6/10
# probability of 2nd ball black = 5/9 [when first ball is black]
# probability of 2nd ball black = 6/9 [when first ball is red]

probability_RR = (4/10) * (3/9)
probability_RB = (4/10) * (6/9)
probability_BR = (6/10) * (4/9)
probability_BB = (6/10) * (5/9)

# Create a DF with the Probability distribution and random variable

lst_color=['RR','RB','BR','BB']

df_probability=pd.DataFrame({'Color':lst_color,
                            'Probability':[probability_RR,probability_RB,probability_BR,probability_BB]})
print(df_probability)

# Plot the Probabalitis distributions
plt.bar(df_probability.Color,df_probability.Probability,width=.3)
plt.xlabel('Color of the Balls')
plt.xticks(lst_color)
plt.ylabel('Probability')
plt.title('\nProbabalities distribution Plot\n')
plt.show()


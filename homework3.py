# PPHA 30537
# Spring 2024
# Homework 3

# Will Sigal

# YOUR CANVAS NAME: Will Sigal
# YOUR GITHUB USER willsigal

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
import us
import statsmodels.formula.api as smf

path = ('/Users/willsigal/Documents/GitHub/homework-3-willsigal')
os.chdir(path)
x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

fig, ax = plt.subplots()
ax.scatter(x, y1, color = 'turquoise', label = 'y1')
ax.plot(x, y2, color = 'orange', label = 'y2')
ax.legend(loc = 'best')
fig.autofmt_xdate() #https://matplotlib.org/3.3.4/gallery/recipes/common_date_problems.html
ax.set_xlabel("date")
ax.set_ylabel("value")
fig.savefig("q1_1_plot.png")
#%%
# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.
x2 = np.array([10 ,20])
y1 = np.array(x2)


fig, ax = plt.subplots()
ax.plot(x2, y1, label='Blue', color='blue') 
ax.plot(x2, y1[::-1], label='Red', color='red')
ax.legend(loc = 'center left')
ax.set_title('X marks the spot :)')
fig.savefig('q1_2_figure.png')
#%%
# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.
mpg = pd.read_csv('mpg.csv')
mpg.head()

plt.subplot(1,4, 1)
sns.regplot(x='displacement', y='mpg', data= mpg, scatter_kws={}, line_kws={'color':'red'})

plt.subplot(1, 4, 2)
sns.regplot(x='horsepower', y='mpg', data=mpg, scatter_kws={},line_kws={'color':'orange'} )
plt.subplot(1, 4, 3)
sns.regplot(x='weight', y='mpg', data=mpg, scatter_kws={}, line_kws={'color':'green'})
figsize=(10, 8)
plt.savefig('q1_3_plot.png')

#%%
# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
sns.regplot(x='cylinders', y='mpg', data=mpg, scatter_kws={},line_kws={'color':'turquoise'} )
plt.savefig('q1_4_plot_a.png')
#The issue is that cylinders is a discreet variable and therefore has a range of mpgs in takes for a given number of
#cylinders. The way we plotted it assumes a linear continuity, where there is none. 
#The regression line here can be misleading and thus a box plot would be better.
#%%

sns.boxplot(x='cylinders', y='mpg', data=mpg)
plt.savefig('q1_4_plot_b.png')



#%%
# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.
sns.set_theme(style='whitegrid') #https://seaborn.pydata.org/tutorial/relational.html

fig, axs = plt.subplots(2, 2, figsize=(12, 10)) #chat gpt, how do I make axis labels fit
#with multiple subplots in seaborn. 
#displacement
ax1 = plt.subplot(2, 2, 1)
sns.regplot(x='displacement', y='mpg', data=mpg,  line_kws={'color':'green'})
ax1.set_xlabel('displacement')

#horespower
ax2 = plt.subplot(2, 2, 2)
sns.regplot(x='horsepower', y='mpg', data=mpg,  line_kws={'color':'red'})
ax2.set_xlabel('horsepower')

#weight
plt.subplot(2, 2, 3)
ax3 = sns.regplot(x='weight', y='mpg', data=mpg,  line_kws={'color':'purple'})

#acceleration
ax4 = plt.subplot(2, 2, 4)
sns.regplot(x='acceleration', y='mpg', data=mpg,  line_kws={'color':'yellow'})


ax2.set_yticklabels([])

ax4.set_yticklabels([])

fig.suptitle('Changes in MPG')
fig.supylabel('mpg')

plt.savefig('q1_5_plot.png')


#%%
# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
mpg.head()
ax5 = sns.boxplot(x = 'origin', y = 'mpg', data = mpg)
ax5.set_title('Fuel Dfficiency by Country of Orgin')
plt.savefig('q1_6_plot.png')

#On average US made cars are the least efficent on average, compared to those from Japan or Europe.



#%%
# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.
ax7 = sns.scatterplot(x = 'displacement', y = 'mpg', hue = 'origin', data = mpg)

ax7.set_title('MPG vs Displacement Organized by Country of Origin')

plt.savefig('q1_7_plot.png')

#This plot confirms the findings of the prior plot aswell as showing that some 
#of the relationship has to do with the displasment differences between the countries.


#%%
# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).
unemp = pd.read_csv('unemp.csv')
uncertainty = pd.read_excel('policy_uncertainty.xlsx')
#%%
#2.1: Merge both dataframes together
unemp.head()
uncertainty.head()
unemp.columns = [col.lower() for col in unemp.columns] #https://stackoverflow.com/questions/19726029/how-can-i-make-pandas-dataframe-column-headers-all-lowercase
unemp.head()
unemp['date'] = pd.to_datetime(unemp['date'])
uncertainty['date'] = pd.to_datetime(uncertainty[['year', 'month']].assign(DAY = 1)) #https://stackoverflow.com/questions/48304927/cleanly-combine-year-and-month-columns-to-single-date-column-with-pandas
uncertainty = uncertainty.drop(['year', 'month'], axis = 1 )
uncertainty.columns = [col.lower() for col in uncertainty.columns]

uncertainty['state'] = uncertainty['state'].apply(lambda x: us.states.lookup(x).abbr if us.states.lookup(x) else None) #Hw 2

uncertainty.head()

merged_df = pd.merge(uncertainty, unemp, on = ['date', 'state'], how = 'inner')
merged_df.head()
 #%%
#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
merged_df['log_epu_composite'] = np.log(merged_df['epu_composite'])

merged_df['lfd_epu_composite'] = merged_df['log_epu_composite'].diff()
                                        
merged_df.head()                              
state_data['date'] = pd.to_datetime(state_data['date'])
          
#%%
#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.

states = ['NY', 'CA', 'FL', 'TX', 'IL']
state_data = merged_df[merged_df['state'].isin(states)]
state_data.dropna()
state_data

fig, axs = plt.subplots(2, 1, figsize=(10, 8))

for state in states: #https://www.youtube.com/watch?v=iszfitjRvGw
    data = state_data[state_data['state'] == state]
    sns.lineplot(data=data, x='date', y='unemp_rate', ax=axs[0], label=state) #https://forum.posit.co/t/for-loop-multiple-line-plots/112692
    
for state in states:
    data = state_data[state_data['state'] == state]
    sns.lineplot(data=data, x='date', y='lfd_epu_composite', ax=axs[1], label=state)

axs[0].set_title('Economic Uncertainty and Unemployement by State')

plt.savefig('q2_2_plot.png')

#%%

#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
state_dummies = pd.get_dummies(merged_df['state'], drop_first=True) #drop first to avoid multicollinearity
merged_df = pd.concat([merged_df, state_dummies], axis=1)

model = smf.ols('unemp_rate ~ lfd_epu_composite + C(state)', data = merged_df).fit()

#%%
#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.
print(model.summary())

#We find that the model using the log-first difference of EPU-C and the fixed effects
#for states explains 14.4% of the variation in the unemployment rate, based on our Adj. r-squared.
# we find that our p-value from the f-state is statistically significant at 5.62e-42.
# lfd of EPU composite has a coefficent of -.115 however it is not statistically 
#siginificant below 5% with the P-value at .251. Some states seem to be more statistically significant to unemployment than others. 
#However, more robust tests are needed before we draw any conclusions. 

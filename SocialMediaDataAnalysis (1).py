#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[1]:


# your code here


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# In[3]:


categories = ["Food", "Travel", "Fashion", "Fitness", "Music", "Culture", "Family", "Health"]

# Set number of tweets
n_tweets = 500

# Generate random dates
dates = pd.date_range(start="2021-01-01", periods=n_tweets)

# Generate random categories
categories = [random.choice(categories) for _ in range(n_tweets)]

# Generate random likes between 0 and 10000
likes = np.random.randint(0, 10000, size=n_tweets)

# Create data dictionary
data = {
    "Date": dates,
    "Category": categories,
    "Likes": likes
}


# In[4]:


df = pd.DataFrame(data)


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


print(df['Category'].value_counts())


# In[9]:


df.drop_duplicates(inplace = True)


# In[ ]:





# In[10]:


df['Date'] = pd.to_datetime(df['Date'])


# In[11]:


df.info()


# In[12]:


df['Likes'] = df['Likes'].astype('int')


# In[13]:


import seaborn as sns


# In[14]:


pip install --upgrade seaborn


# In[15]:


import seaborn
print(seaborn.__version__)


# In[16]:


total_likes_df = df.pivot_table(index='Category', values='Likes', aggfunc='sum')

total_likes_df


# In[17]:


sns.histplot(data = total_likes_df, x ='Category',  weights = 'Likes', shrink= .5 , color = 'Green')
plt.xlabel("Category")
plt.ylabel("Total Likes")


# In[24]:


sns.boxplot(x = 'Category', y = 'Likes' , data = df)


# In[25]:


Mean_total_like =df[['Likes']].mean()
Mean_total_like


# In[26]:


df.groupby('Category')['Likes'].mean()


# My purpose in starting this portfolio project was to go deeper into data analysis topics and uncover insights that might be turned into social media marketing tactics. Through a meticulous process of data collection, analysis, and interpretation, I traversed a succession of hurdles, each serving as a stepping stone towards a more comprehensive understanding of the data set at hand.
# 
# ## Analysis:
# 
# 
# Average Likes per Post:
# The average likes per post across all categories is 4968.39, indicating a substantial level of engagement with the audience.
# 
# Average Likes per Category:
# 
# Culture:  4879.56. 
# 
# Family - 4775.33
# Fashion- 5491.24
# Fitness- 3993.68
# Food  -  5288.58
# Health - 5215.83
# Music -  4934.02
# Travel - 5012.82
# 
# ## Insights:
# 
# 
# Fashion and Food categories tend to perform exceptionally well in terms of average likes per post, indicating a high level of interest and engagement from the audience.
# Although Fitness posts have a lower average likes per post compared to other categories, they still receive a considerable amount of engagement.
# The Health category has the highest total number of likes, indicating a consistent level of engagement despite a slightly lower average likes per post compared to Fashion and Food.
# Culture and Family categories, while still receiving a significant number of likes, have relatively lower average likes per post compared to other categories.
# 
# ## Recommendations:
# 
# 
# Content Strategy: 
#                     Create more content related to fashion and food, as these categories have proven to be popular with the audience and drive higher engagement.
# 
# Engagement Strategies: 
#                         Encourage more interactions and discussions in the Fitness and Health categories to increase engagement, despite a slightly lower average like per post.
# 
# Diversification:
#                     While focusing on high-performing categories, continue to diversify content across all categories to appeal to the audience's various interests.
#                     
# Analytical Approach: 
#                        Consistently monitor and analyse social media metrics to identify trends, preferences, and areas for improvement in content strategy.
# 
# 
# ## Conclusion:
#   In conclusion, this portfolio project stands as a testament to my ability to navigate complex datasets, extract actionable insights, and propose data-driven solutions. By combining technical expertise with analytical prowess, I am confident in my ability to drive value and innovation in the realm of digital marketing.
# 
#                     

# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[1]:


# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style("whitegrid")
sns.set_context("poster")


# In[2]:


df = pd.read_csv('data/search.csv', encoding='utf8')
df.head() 


# In[3]:


df.describe()


# In[4]:


df.info()


# In[ ]:





# In[5]:


subset = df[['First Search Time (GMT)','All Department (APS) or Category', 'Keywords', 'Is From External Link (Y/N)','Search From External Site (Y/N)','Paid Purchase (Y/N)','Number of Clicked Items', 'Number of Items Added to Cart', 'Number of Items Ordered']]
subset.columns = ['time','category','keyword','ext_link','ext_search','purchase','clicks', 'card_added','card_ordered']
subset.describe()


# In[6]:


print(subset.time.min())
print(subset.time.max())


# In[7]:


category=subset.groupby(['category']).size()
category.plot(kind='bar',figsize=(17,5));


# In[8]:


subset_card = subset[(subset['card_added']>0) & (subset['category']=='aps')]
print (len(subset_card))
subset_card.mean()


# In[9]:


subset_clicked = subset[(subset['clicks']>1)]
print (len(subset_clicked))
subset_clicked.mean()


# In[10]:


subset_card.reset_index(drop=True, inplace=True)
cols = ['time','category','keyword','purchase','clicks','card_added','card_ordered']
print(subset_card.loc[:,cols].head())


# In[11]:


subset_clicked = subset_clicked.sort_values('card_ordered', ascending=False)
subset_clicked.reset_index(drop=True, inplace=True)
subset_clicked


# In[12]:


cols = ['category','keyword','purchase','clicks','card_added','card_ordered']
print(subset_clicked.loc[:,cols].head(30))


# In[13]:


#df1.plot('Country',['Corruption','Freedom','Generosity','Social support'],kind = 'line')

clicks=subset.groupby(['category']).sum()

clicks = clicks.loc[:,['clicks','card_added','card_ordered']].sort_values('card_ordered', ascending=False)
clicks.reset_index(inplace=True)
clicks = clicks.loc[1:,:]
clicks [0:40]


# In[14]:


plot = clicks.plot('category',['clicks','card_added','card_ordered'],grid=False, kind='bar',ylim =[0,50], width=0.8, figsize=(17,5))
plot.set_xticklabels(clicks['category'], rotation=80)


# In[15]:


spearmancorr = clicks.corr(method ='spearman') #non-parametric since no normal distribution 
spearmancorr


# In[17]:


sns.set_context('poster')
sns.set_style('whitegrid')
fig, ax = plt.subplots(figsize=(5,5))  

sns.heatmap(spearmancorr, 
            xticklabels=spearmancorr.columns,
            yticklabels=spearmancorr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5,
           )


# In[ ]:





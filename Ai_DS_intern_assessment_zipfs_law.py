# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:50:23 2018

@author: hrm1886

This program collects the words from the summary columns of the 
movie dataframe and puts them all into a dictionary such that the 
frequencies of the top 5 words can be counted and returned.
The top 5 words and their frequencies are then plotted to investigate
evidence of Zipf's law.
"""


import numpy as np
import pandas as pd
import seaborn as sns
import os
from collections import Counter
import re
from nltk.corpus import stopwords
#from wordcloud import WordCloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\hrm1886\\Desktop')

movie_data = pd.read_csv('movie_data.csv')

#add each word from all the summaries to a dictionary
def zipfs_law(df):
    summary_word_dict = {}
    summary_list = df['summary'].tolist()
    for summary in summary_list:
        summary = re.sub(r'\W+', " ", summary)
        summary = summary.split(" ")
        
        for word in summary:
            if word == 's': #get rid of s's that came from plurals
                continue
            if word in summary_word_dict.keys():
                summary_word_dict[word] += 1
            else:
                summary_word_dict[word] = 1

    return summary_word_dict

zipfs_dist = zipfs_law(movie_data)

#return the top 5 frequently occuring words
top_words_zipf = dict(Counter(zipfs_dist).most_common(15))
print(top_words_zipf)

#put those words and their values back into dataframe for plotting
top_words_dataframe = pd.DataFrame.from_dict(top_words_zipf,orient='index')

#plot the results
ax = top_words_dataframe.plot(kind='bar', title ="Zipf's Distribution",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("Word",fontsize=20)
ax.set_ylabel("Frequency",fontsize=20)
for tick in ax.get_xticklabels():
    tick.set_rotation(360)
    tick.set_fontsize(20)
for tick in ax.get_yticklabels():
    tick.set_rotation(45)
    tick.set_fontsize(15)
plt.savefig('Word_dist.jpg')
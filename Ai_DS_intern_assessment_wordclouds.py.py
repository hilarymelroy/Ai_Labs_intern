# -*- coding: utf-8 -*-
"""
This program iterates through movies of a certain genre and collect 
the words in their summaries, storing them in a dictionary. The wordcloud
package is used to visualize the top 100 most frequent words in the collective 
summaries of each movie of a given genre, minus the stop words as defined
in the word cloud package.
The function genre_word_summary takes a dataframe and a genre as
arguments.
@author: hrm1886
"""
import numpy as np
import pandas as pd
import seaborn as sns
import os
from collections import Counter
import re
from nltk.corpus import stopwords
from wordcloud import WordCloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#iterate through summaries of all movies of a given genre..
#..appending them to a summary list         
def genre_word_summary(df,genre):
    new_movie_data = movie_data[movie_data['genres'].str.contains(genre)]
    summary_list = []
    for summary in new_movie_data['summary']:
        summary_list.append(summary)
    return summary_list
words_summary = genre_word_summary(movie_data,'drama')

#strip the non alphanumeric characters and split the summaries on.. 
#..spaces
all_words_list = []
for word_string in words_summary:
    word_string = re.sub(r'\W+', ' ',word_string)
    word_string = word_string.split(" ")
    for i in word_string:
        all_words_list.append(i)
all_words_text = ' '.join(all_words_list)
        
#use wordcloud library to remove stopwords from the summary list..
#..and to generate a visual of the most characteristic words of..
#..a given genre
stopwords = set(STOPWORDS)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=40, 
        scale=3,
        random_state=1 
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.savefig('Action3_Wordcloud.jpg')    
    plt.show()
    
show_wordcloud(all_words_text)

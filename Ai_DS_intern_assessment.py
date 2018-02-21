# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:05:58 2018

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

movie_data = pd.read_csv('movie_data.csv')

def top_genres(df):
    genres_dict = {}
    genre_list = movie_data['genres'].tolist()
    for genre in genre_list:
        genre=genre.replace('[',"")
        genre=genre.replace('"',"")
        genre=genre.replace("]","")
        genre=genre.replace(" ", "")
        genre=genre.split(",")

        for word in genre:
            if word in genres_dict.keys():
                genres_dict[word] += 1
            else:
                genres_dict[word] = 1
    return dict(Counter(genres_dict).most_common(5))
top_5_genres = print(top_genres(movie_data))
 
            
def genre_word_summary(df,genre):
    new_movie_data = movie_data[movie_data['genres'].str.contains(genre)]
    summary_list = []
    for summary in new_movie_data['summary']:
        summary_list.append(summary)
    return summary_list
words_summary = genre_word_summary(movie_data,'drama')

all_words_list = []
for word_string in words_summary:
    word_string = re.sub(r'\W+', ' ',word_string)
    word_string = word_string.split(" ")
    for i in word_string:
        all_words_list.append(i)
        
def remove_stopwords(word_list):
        processed_word_list = []
        for word in word_list:
            word = word.lower() # in case they arenet all lower cased
            if word not in stopwords.words("english"):
                processed_word_list.append(word)
        return processed_word_list
new_words_summary = remove_stopwords(all_words_list)

new_words_text = ' '.join(new_words_summary)

stopwords = set(STOPWORDS)
print(stopwords)

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.savefig('Drama_Wordcloud.jpg')
    plt.show()
    
show_wordcloud(new_words_text)

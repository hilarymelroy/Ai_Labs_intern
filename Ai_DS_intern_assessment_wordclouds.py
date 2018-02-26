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

import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
from collections import Counter

#read in data to a dataframe
os.chdir('C:\\Users\\hrm1886\\Desktop')
movie_data = pd.read_csv('movie_data.csv')

def top_genres(df):
    genres_dict = {}
    genre_list = movie_data['genres'].tolist()
    for genre in genre_list:
        genre=genre.replace("-","")
        genre=genre.replace('[',"")
        genre=genre.replace('"',"")
        genre=genre.replace("]","")
        genre=genre.split(",")

        for word in genre:
            word=word.strip()
            if word in genres_dict.keys():
                genres_dict[word] += 1
            else:
                genres_dict[word] = 1
    return dict(Counter(genres_dict).most_common(5))

#iterate through summaries of all movies of a given genre..
#..appending them to a summary list    
     
def genre_word_summary(df,genre):
    new_movie_data = movie_data[movie_data['genres'].str.contains(genre)]
    summary_list = []
    for summary in new_movie_data['summary']:
        summary_list.append(summary)
    return summary_list
#words_summary = genre_word_summary(movie_data,'romance')

#strip the non alphanumeric characters and split the summaries on.. 
#..spaces
def create_freqs(summaries):
    all_words_list = []
    for word_string in summaries:
        word_string = re.sub(r'\W+', ' ',word_string)
        word_string = word_string.split(" ")
        for i in word_string:
            all_words_list.append(i)
    all_words_text = ' '.join(all_words_list)
    return all_words_text
        
#use wordcloud library to remove stopwords from the summary list..
#..and to generate a visual of the most characteristic words of..
#..a given genre

def show_wordcloud(data, genre,title = None):
    stopwords = set(STOPWORDS)
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
    plt.savefig(genre+'_Wordcloud.jpg')    
    plt.show()
    

def all_genres_wordcloud(df):
    top_five_genres = top_genres(df).keys()
    for genre in top_five_genres:
        genre_summaries = genre_word_summary(df,genre)
        summary_word_freqs = create_freqs(genre_summaries)
        show_wordcloud(summary_word_freqs,genre)
        print(genre)
        
all_genres_wordcloud(movie_data)
        

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

'''
This function saves movie data in a pandas dataframe and creates
 a dictionary with genres as keys and frequency of occurances of genres
 as values. It outputs the top 5 genres in the movie data.
It assumes a file type of csv.
'''

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
<<<<<<< HEAD:Ai_DS_intern_assessment_top_genres.py
=======
 
            

            
>>>>>>> ede99ca38702d68bee1953bb837aede7fdd4fe9c:Ai_DS_intern_assessment_top_genres.py

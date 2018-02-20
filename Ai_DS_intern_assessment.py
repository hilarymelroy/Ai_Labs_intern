# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:44:39 2018

@author: hrm1886

Ai labs data science intern assessment

"""
import numpy as np
import pandas as pd
import seaborn as sns
import os
from collections import Counter

os.chdir('C:\\Users\\hrm1886\\Desktop')

movie_data = pd.read_csv('movie_data.csv')
movie_data.dtypes

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
print(dict(Counter(genres_dict).most_common(5)))



    



            

            
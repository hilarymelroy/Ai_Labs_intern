# Ai_Labs_intern
Intern assessment for Ai Labs Data Science team
## Dependencies

Python 3.6.1

* pandas 
* Wordcloud ```conda install -c https://conda.anaconda.org/amueller wordcloud```
* matplotlib 
* re 
* os
* Counter

## Usage

For all files - the working directory is set to my desktop, so that will probably 
need to be changed. Otherwise see the brief descriptions with any instructions needed
below.

In this repository are 3 files, each corresponding to one of the prompts given in the
assignment.

Ai_intern_assessment_top_genres.py takes a .csv file containing movie data and creates a 
dictionary of all the genres associated with the movies in the dataset. Once the dictionary
is created, the 5 genres with the highest frequency of occurance is returned as a smaller 
dictionary, displaying the genre and its count. To run this file, just make sure the 
top_genres function is passed a dataframe 'movie_data'.

Ai_DS_intern_assessment_wordclouds.py collects all the summaries of the movies of a given genre
(from the top 5 genre list) and appends them to a list. The list is then stripped of any 
characters that are not alphanumeric and split on the spaces to create one big list of 
words from all the summaries. The wordcloud function has a built in stopwords set 
which corrects for the stop words, then creates a word cloud of the top 100 words in those summaries. To run this file, just
make sure the all_genres_wordcloud() function is passed the movie dataframe. This program needs
the wordcloud import to run.

Ai_DS_intern_assessment_zipfs_law.py is very similar to Ai_intern_assessment_top_genres, except
this compiles all the words in all the summaries and adds them to a dictionary. This time, no
words have been removed. The top 5 words are obtained and assessed for evidence of Zipf's law.
To run this file, just make sure the zipfs_law function is passed the movie dataframe.

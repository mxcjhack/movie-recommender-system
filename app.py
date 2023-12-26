import streamlit as st
import pickle
import numpy as np
import pandas as pd
import ast

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
movie_list = pickle.load(open('movies.pkl', 'rb'))
movie_list = movie_list['title'].values

st.title('Movie Recommendor System')

select_movie_name = st.selectbox('MOVIE LIST', movie_list)


if st.button('Recommend'):
   recommendations = recommend(select_movie_name)
   for i in recommendations:
        st.write(i)
        

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 22:23:11 2022

@author: viral
"""
import streamlit as st
import pandas as pd
import pickle
import response
import requests

# def fetch_poster(movie_id):
#     response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
#     data=response.json()
#     return  ""
def recommand(movie):
    movie_index=movies[movies['original_title']==movie].index[0]
    dis=similarity[movie_index]
    movie_list=sorted(enumerate(list(dis)),reverse=True,key=lambda x:x[1])[1:6]

    reco_movie=[]
    for i in movie_list:
        movie_id=i[0]
        reco_movie.append(movies.iloc[i[0]]['original_title'])
    return reco_movie

st.title("Movie Recommendation System")
movies=pd.read_csv(r"C:\Users\viral\OneDrive\Desktop\D\K N Extra\Reco Sys\TMDB 5000 (Using Weighted Average) - Copy\movies.csv")
movie_list=list(movies['original_title'])
# print(movie_list)

similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie=st.selectbox('Select Movie',movie_list)

# print(recommanded_movies)
if st.button("Recommand"):
    recommanded_movies=recommand(selected_movie)
    for i in range(len(recommanded_movies)):
        st.write(recommanded_movies[i])

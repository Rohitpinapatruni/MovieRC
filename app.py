
import pickle
import streamlit as st
import requests
import pandas as pd
import gzip
from pandas import Index



st.title("MovieRS")
st.header("Movie Recommendation System using Streamlit")
movies = pickle.load(open('Artifacts/movies_list.pkl', 'rb'), encoding='latin1')
similarity = pickle.load(gzip.open('Artifacts/similarity.pkl.gz', 'rb'))

movies_list = movies['title'].values
selected_movie=st.selectbox('Select a movie:', movies_list)
def fetch_poster(movie):
    pass
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    #rm_poster = []
    for i in movie_list:
        #movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        #rm_poster.append(fetch_poster(movie_id))
    
    return recommended_movies
cols=st.columns(5)
rcmv=recommend(selected_movie)
if st.button(f'Show Recommend'):
    for i in range(5):
        with cols[i]:
            st.text(rcmv[i])
            #st.image(rm_poster[i], width=200)



 
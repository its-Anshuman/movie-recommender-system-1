import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=2b77de5376e9e504d628187f5d39dd50&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Load the movie data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)  # Convert to DataFrame

st.title("Movie Recommender System")

# Dropdown for movie selection
selected_movie_name = st.selectbox(
    'Which Movie?',
    movies['title'].values
)

# Define the recommendation function
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # Top 5
        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

        return recommended_movies,recommended_movies_posters
    except IndexError:
        return ["No recommendations found."]

if st.button('Recommend Movies'):
    names,posters = recommend(selected_movie_name)  # Call function

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

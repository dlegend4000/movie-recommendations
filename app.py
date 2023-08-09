import streamlit as st
import pickle
import requests

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/premium-vector/space-background-with-stars-vector-illustration_97886-319.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("Movie Recommender System")
selectvalue = st.selectbox("select movie from dropdown", movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


def recommend(movie):
     index = movies[movies['title'] == movie].index[0]
     distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
     recommend_movie=[]
     recommend_poster=[]
     for i in distance[1:22]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
     return recommend_movie, recommend_poster
 
if st.button("Show Recommendation"):
    movie_name, movie_poster = recommend(selectvalue)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
        st.text(movie_name[6])
        st.image(movie_poster[6])
        st.text(movie_name[11])
        st.image(movie_poster[11])
        st.text(movie_name[16])
        st.image(movie_poster[16])

    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
        st.text(movie_name[7])
        st.image(movie_poster[7])
        st.text(movie_name[12])
        st.image(movie_poster[12])
        st.text(movie_name[17])
        st.image(movie_poster[17])

    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
        st.text(movie_name[8])
        st.image(movie_poster[8])
        st.text(movie_name[13])
        st.image(movie_poster[13])
        st.text(movie_name[18])
        st.image(movie_poster[18])

    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
        st.text(movie_name[9])
        st.image(movie_poster[9])
        st.text(movie_name[14])
        st.image(movie_poster[14])
        st.text(movie_name[19])
        st.image(movie_poster[19])

    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
        st.text(movie_name[10])
        st.image(movie_poster[10])
        st.text(movie_name[15])
        st.image(movie_poster[15])
        st.text(movie_name[20])
        st.image(movie_poster[20])                
       
 
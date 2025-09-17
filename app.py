import streamlit as st
import pickle

# Load Data
movies = pickle.load(open("movies.pkl", 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation Function
def recommend(movie):
    # find index of the given movie
    movie_index = movies[movies['title'] == movie].index[0]
    
    # distances for that movie
    distances = similarity[movie_index]
    
    # top 5 most similar movies (excluding the same movie itself)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies


# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Get Recommendations For the Selected Movie!',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.subheader("Top 5 Recommendations:")
    for i in recommendations:
        st.write(i)

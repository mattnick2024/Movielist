import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

API_key = "5fa14b11eb00ababb5cc2307d9ff8266"  

movies = pickle.load(open('_WBS/Movielist/pickle/movielist.sav', 'rb'))
genres = pickle.load(open('_WBS/Movielist/pickle/genres.sav', 'rb'))
maxRatingCount = int(movies["Rating_Count"].max())

def get_poster_url(tmdbId):
    load_dotenv()
#    api_key = os.getenv('TMDB_API_KEY')
#    api_key = "5fa14b11eb00ababb5cc2307d9ff8266"
    response = requests.get(f'https://api.themoviedb.org/3/movie/{tmdbId}?api_key={API_key}')
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    else:
        return None


def main():
    with st.sidebar:
        items = genres
        def updateMovielist():
            df = movies
            select_labels = values #['IMAX','Documentary']
            mask = df['genres'].str.contains('|'.join(select_labels))
            subset_df = df[mask]
            return subset_df[["title","genres","Rating_Count","Rating_Mean","tmdbId"]].sort_values("Rating_Mean")
        values = st.multiselect('Choose genres', 
                                items, 
                                [], 
                                #on_change=updateMovielist, 
                                key='issue')  
        minRatings = st.slider('Choose minimum of user ratings', 5, maxRatingCount, 10)
        st.write(minRatings)
    udml = updateMovielist().sort_values(by="Rating_Mean")[0:5]
    udml = udml.loc[udml["Rating_Count"] >= minRatings]
        #st.write(len(udml)) 
        
#         p1 = get_poster_url(udml["tmdbId"][0:1])
# #    p2 = get_poster_url(udml["tmdbId"][1:2])
# #    p1 = get_poster_url(8844)
#         p2 = get_poster_url(8844)
#         p3 = get_poster_url(2756)
#         p4 = get_poster_url(72867)
#         p5 = get_poster_url(19913)
#         col1, col2, col3,col4, col5 = st.columns(5, gap="small")
#         w = 120
#         # with col1:
#         #     st.image(p1,width=w)
#         # with col2:
#         #     st.image(p2,width=w)
#         # with col3:
#         #     st.image(p3,width=w)        
#         # with col4:
#         #     st.image(p4,width=w)    
#         # with col5:
#         #     st.image(p5,width=w)    
#         with col1:
#             st.write(p1,width=w)
#         with col2:
#             st.image(p2,width=w)
#         with col3:
#             st.image(p3,width=w)        
#         with col4:
#             st.image(p4,width=w)    
#         with col5:
#             st.image(p5,width=w)    
    
    st.dataframe(udml.sort_values(by="Rating_Mean")[0:5])
#    st.dataframe(udml)
        

if __name__ == '__main__':
    main()

    
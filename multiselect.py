import streamlit as st
from st_click_detector import click_detector
import pickle
import requests
import os
from dotenv import load_dotenv
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

#API_key = os.getenv('TMDB_Key') 
API_key = "5fa14b11eb00ababb5cc2307d9ff8266" 

movies = pickle.load(open(f'{dir_path}/pickle/movielist.sav', 'rb'))
genres = pickle.load(open(f'{dir_path}/pickle/genres.sav', 'rb'))
maxRatingCount = int(movies["Rating_Count"].max())

def footer():
    st.write("Hurray! It works!!!")
    st.write("Finally, human tenacity defeated artificial recalcitrance !!! ")


def get_poster_url(tmdbId):
    load_dotenv()
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
        footer()


        
    udml = updateMovielist()    
    udml = udml.loc[udml["Rating_Count"] >= minRatings].sort_values(by="Rating_Mean",ascending=False)[0:5]
    
    l1 = udml["tmdbId"][0:1].to_list()[0]
    l2 = udml["tmdbId"][1:2].to_list()[0]
    l3 = udml["tmdbId"][2:3].to_list()[0]
    l4 = udml["tmdbId"][3:4].to_list()[0]
    l5 = udml["tmdbId"][4:5].to_list()[0]
    
        
    def getClickableImage(id):
        # Displaying the clickable image
        image_url = get_poster_url(id) 
        link_url =  f"https://www.themoviedb.org/movie/{id}"
        clickable_image = f'<a href="{link_url}" target="_blank" rel="noopener noreferrer">' \
                      f'<img src="{image_url}" alt="Clickable Image" style="width: 75%; max-width: 300px;"></a>'
        return clickable_image


    
    col1, col2, col3,col4, col5 = st.columns(5, gap="small")
    w=120
    with col1:
        st.markdown(getClickableImage(l1), unsafe_allow_html=True)
    with col2:
        st.markdown(getClickableImage(l2), unsafe_allow_html=True)
    with col3:
        st.markdown(getClickableImage(l3), unsafe_allow_html=True)
    with col4:
        st.markdown(getClickableImage(l4), unsafe_allow_html=True)
    with col5:
        st.markdown(getClickableImage(l5), unsafe_allow_html=True)
    
    
    st.dataframe(udml)
        

if __name__ == '__main__':
    main()
  
 
    


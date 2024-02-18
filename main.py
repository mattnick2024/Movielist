import pandas as pd
import seaborn as sns
import requests
import streamlit as st
import streamlit_theme as stt
import pickle
import os
from dotenv import load_dotenv

def get_poster_url(tmdbId):
    load_dotenv()
    api_key = os.getenv('TMDB_API_KEY')
    api_key = "5fa14b11eb00ababb5cc2307d9ff8266"
    response = requests.get(f'https://api.themoviedb.org/3/movie/{tmdbId}?api_key={api_key}')
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500{poster_path}'
    else:
        return None


API_key = "5fa14b11eb00ababb5cc2307d9ff8266"  
stt.set_theme({'primary': '#1b212121'})



#st.title("Movie-List")
st.write("# Movie-List")
movielist = pickle.load(open('_WBS/Movielist/pickle/movielist.sav', 'rb'))
#movielist["title"] = movielist["longtitle"]
st.write(f"{len(movielist)} movies loaded")
#st.balloons()
#st.toast('Movielist has been loaded ... start recommendations!', icon='😍')
# 
movies = movielist[["title","tmdbId"]]
#.sort_values(by="titles")


    

with st.sidebar:
    option = st.selectbox(
    'select movie',
    movies)
    tmdbId = int(movielist["tmdbId"].loc[movielist["title"]==option])
    st.write(f'tmdbId={tmdbId}')
    st.spinner('Loading...')
#     time.sleep(5)
    response = requests.get(f"""https://api.themoviedb.org/3/find/{tmdbId}?api_key={API_key}""")
    url = get_poster_url(tmdbId)
    st.image(url)
#    st.success('Done!')

    
    #st.write(url)
#    st.write(response.json())
#    st.image(('https://image.tmdb.org/t/p/w92' + response.json()['movie_results'][0]['poster_path']))
# st.write(response)
# #    st.write(f'You selected: {option}')

p1 = get_poster_url(8844)
p2 = get_poster_url(10688)
p3 = get_poster_url(2756)
p4 = get_poster_url(72867)
p5 = get_poster_url(19913)
#st.image([p1,p2,p3],caption=["Jumanji","p2","p3"],width=150)
  
    
col1, col2, col3,col4, col5 = st.columns(5, gap="small")
w = 120
with col1:
#   st.header("A cat")
   st.image(p1,width=w)

with col2:
#   st.header("A dog")
   st.image(p2,width=w)

with col3:
#   st.header("An owl")
   st.image(p3,width=w)    
    
with col4:
#   st.header("An owl")
   st.image(p4,width=w)    
    
with col5:
#   st.header("An owl")
   st.image(p5,width=w)    
    
#   
# 

# #




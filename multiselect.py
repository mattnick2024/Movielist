import streamlit as st
import pickle

movies = pickle.load(open('_WBS/Movielist/pickle/movielist.sav', 'rb'))
genres = pickle.load(open('_WBS/Movielist/pickle/genres.sav', 'rb'))

# def filterMovies(opt):
#     st.write('You selected:', opt)
#     # return 
#         # st.write(st.session_state['issue'])

# options = st.multiselect(
#     'What are your favorite colors',
#     genres,
#     on_change=filterMovies([1,2,3]))

# #st.write('You selected:', options)
# st.dataframe(movies)


def main():
    items = genres
    def updateMovielist():
        return(movies)
 #       st.write(st.session_state['issue'])
    values = st.multiselect('Choose genres', items, [], on_change=updateMovielist, key='issue')  
 #   st.write(values)
    st.write(updateMovielist()) # < returns correct list

if __name__ == '__main__':
    main()

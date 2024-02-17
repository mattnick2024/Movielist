import streamlit as st

# # Function to define the Home page
# def home():
#     st.title("Home Page")
#     st.write("Welcome to the Home page!")

# # Function to define the About page
# def about():
#     st.title("About Page")
#     st.write("This is the About page.")


def BasicPop():
    st.title("Basic Popularity")
    st.write("very simple")
    
def UserBased():
    st.title("User-Based")
    st.write("a bit more complicated")
    
def ItemBased():
    st.title("Item-Based")
    st.write("ufff.....")
    



def main():
 st.sidebar.title("Navigation")
 page = st.sidebar.radio("Choose Recommender Method", ["Basic Popularity", "User-Based","Item-Based"])
 if page == "Basic Popularity":
     BasicPop()
 elif page == "User-Based":
     UserBased()
 elif page == "Item-Based":
     ItemBased()

if __name__ == "__main__":
    main()

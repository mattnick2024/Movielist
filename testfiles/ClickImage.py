# import streamlit as st

# # Displaying the image
# image_url = "https://example.com/your_image.jpg"
# img1 = st.image(image_url, caption='Click me!', use_column_width=True)

# # Creating a clickable link
# # link_url = "https://example.com/your_target_page"
# link_url = "https://image.tmdb.org/t/p/w500/qbYgqOczabWNn2XKwgMtVrntD6P.jpg"
# link_text = "Click mich"
# st.image(link_url)
# # link_markdown = f"[{link_text}]({link_url})"
# # st.markdown(link_markdown, unsafe_allow_html=True)


# link_markdown = f'<a href="{link_url}" target="_blank" rel="noopener noreferrer">{link_text}</a>'
# st.markdown(link_markdown, unsafe_allow_html=True)




# import streamlit as st

# # Displaying the clickable image
# image_url = "https://image.tmdb.org/t/p/w500/qbYgqOczabWNn2XKwgMtVrntD6P.jpg"
# link_url = "https://image.tmdb.org/t/p/w500/qbYgqOczabWNn2XKwgMtVrntD6P.jpg"

# clickable_image = f'<a href="{link_url}" target="_blank" rel="noopener noreferrer">' \
#                    f'<img src="{image_url}" alt="Clickable Image" style="width: 100%; max-width: 600px;"></a>'

# st.markdown(clickable_image, unsafe_allow_html=True)



import streamlit as st

def getClickableImage(url):
    # Displaying the clickable image
    image_url = url 
    link_url =  "https://www.themoviedb.org/movie/8844"
    clickable_image = f'<a href="{link_url}" target="_blank" rel="noopener noreferrer">' \
                      f'<img src="{image_url}" alt="Clickable Image" style="width: 50%; max-width: 200px;"></a>'
    return clickable_image

st.markdown(getClickableImage("https://image.tmdb.org/t/p/w500/qbYgqOczabWNn2XKwgMtVrntD6P.jpg"), unsafe_allow_html=True)

import streamlit as st
from few_short import FewShortPosts
from post_generator import generate_post
def main():
    st.title("LinkedIn Post Generator")
    col1,col2,col3= st.columns(3)
    fs = FewShortPosts()
    with col1:
        selected_tag=st.selectbox("Title",options=fs.get_tags())
    
    with col2:
        selected_language=st.selectbox("Language",options=["English","Hinglish"])
    
    with col3:
        selected_length=st.selectbox("Length",options=["Short","Medium","Long"])

    if st.button("Generate Post"):
        post = generate_post(selected_tag,selected_language,selected_length)
        st.write(post)
        
if __name__ == "__main__":
    main()
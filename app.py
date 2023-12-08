import streamlit as st
from PIL import Image
from translation import translate_text
from image_processing import process_image

def upload_image():
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        return Image.open(uploaded_file)

def main():
    st.set_page_config(layout="wide")
    st.title("Image Translation with EasyOCR")

    st.sidebar.title("Menu")
    img = upload_image()
    process_btn = st.sidebar.button("Process Image")

    if img is not None:
        st.sidebar.image(img, caption='Uploaded Image', use_column_width=True)

    if process_btn and img is not None:
        st.sidebar.text("Image is being processed...")
        processed_img = process_image(img)
        st.subheader("Processed Image with Translated Text")
        st.image(processed_img, caption='Translated Text on Processed Image', use_column_width=True)

if __name__ == "__main__":
    main()

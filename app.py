import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="URL and System Image Viewer", page_icon=":computer:")

def main():
    st.title("Basic Image Viewer")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "ico"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Your uploaded Image", use_column_width=True)
    else:
        st.info("Please upload an image file.")

if __name__ == "__main__":
    main()



def main():
    st.title("Basic Image Viewer from URL")

    image_url = st.text_input("Enter Image URL:")
    if image_url:
        try:
            # Fetch the image from the URL
            response = requests.get(image_url)
            if response.status_code == 200:
                # Open the image using PIL
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Image from URL", use_column_width=True)
            else:
                st.error("Failed to retrieve image. Please check the URL.")
        except Exception as e:
            st.error("An error occurred while fetching or displaying the image.")
            st.error(str(e))

if __name__ == "__main__":
    main()

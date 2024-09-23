import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Background Removal App")

# File uploader for foreground image
foreground_file = st.file_uploader("Upload Foreground Image", type=["jpg", "jpeg", "png"])

# File uploader for background image
background_file = st.file_uploader("Upload Background Image", type=["jpg", "jpeg", "png"])

if foreground_file is not None and background_file is not None:
    # Remove background
    foreground_img = Image.open(foreground_file).convert("RGBA")
    foreground_no_bg = remove(foreground_img)

    # Open and resize the background image
    background_img = Image.open(background_file).convert("RGBA")
    background_img = background_img.resize(foreground_no_bg.size)
    
    # Paste the foreground on the background
    background_img.paste(foreground_no_bg, (0, 0), foreground_no_bg)

    # Display the output
    st.image(background_img, caption="Combined Image", use_column_width=True)

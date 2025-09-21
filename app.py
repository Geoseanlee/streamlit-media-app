import io
from pathlib import Path
import streamlit as st
from PIL import Image, ImageEnhance
# st.set_page_config(page_title="MY VIDEO", page_icon="🎬", layout="wide")
# st.title("Travel Around")
st.logo("assets/Icon-colored-nobg.png", size="large")
st.image("assets/videos/Banner.png", caption=None, width = 1040)
img_col1, img_col2 = st.columns(2)
with img_col1:
    st.image("assets/videos/Poster.png", caption="test test test test test test test test test test ")
with img_col2:
    st.image("assets/videos/Poster.png", caption="poster poster test test test poster test test test test ")
    
col1, col2 = st.columns(2)
with col1:
    st.video("assets/videos/REC-20250921173036.mp4")
with col2:
    st.video("assets/videos/REC-20250921173036.mp4")

import streamlit as st
from streamlit_drawable_canvas import st_canvas
st.title('Dibujitos')

# Add canvas component
# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:",
    ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
)
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = st.sidebar.color_picker("Pick A Color", "#00f900", "000000", "ffffff")
bg_color = '#000000'

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    drawing_mode=drawing_mode,
    height=200,
    width=200,
    key="canvas",
)

"""
UI Components
=============

Components for UI using Streamlit.

AUTHOR
    rafidini@GitHub

CREATED AT
    Sat. 23 Apr. 2022 00:28
"""
# External package
import streamlit as st
import base64
import requests
import typing
from enum import Enum

# Functions
def render_select(option: dict) -> str:
    res: str = st.sidebar.selectbox(
        option['label'],
        options=option['options'],
        key=option['label']
    )
    return None if res == 'null' else f"{option['label']}={res}"

def side_bar(styles: typing.Iterable) -> str:
    st.sidebar.title('Settings')

    # Settings
    style_names: list = [style.NAME for style in styles]
    style: str = st.sidebar.selectbox('Pick your style', options=style_names)
    
    # Get style options
    index_style: int = style_names.index(style)
    style_options: list = styles[index_style].STYLE_OPTIONS
    format_options: list = [
        dict(label=option.get_label(), options=option._member_names_)
        for option in style_options
    ]
    choices: list = [render_select(option) for option in format_options]
    return '&'.join([choice for choice in choices if choice if not None])

def render_svg(svg: str):
    """Renders the given svg string."""
    svg_b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % svg_b64
    st.write(html, unsafe_allow_html=True)

def render_image(image_url: str):
    response: requests.Response = requests.get(image_url)
    render_svg(response.text)

def main_page(**kwargs):
    # Sidebar
    options: str = side_bar(styles=kwargs.get('styles'))
    
    # Main page
    st.title('DiceBearPicker · Pick your avatar')
    api_endpoint: str = kwargs.get('api_endpoint')
    image_url: str = f'{api_endpoint}?{options}'
    st.write(f"{image_url}", language='bash')
    
    render_image(image_url)

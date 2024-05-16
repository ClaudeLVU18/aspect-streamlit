import json
import streamlit as st 
from streamlit_lottie import st_lottie
import requests

st.markdown("<h1 style='text-align: center; co  lor: #FFFF;'>ASPECT</h1>", unsafe_allow_html=True)

st.markdown("<h5 style='text-align: center; color: pink;'> <em>Aspect takes images and loads them into a model to find common points cloud points.\n Begin by uploading your images down below: </em </h5>", unsafe_allow_html=True)

df = st.file_uploader(label = "Upload images: ")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<")
        
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
with open("lottiefiles/anim.json", "r") as f:
    lottie_file = json.load(f)

st_lottie(lottie_file)

local_css("style/style.css")

animation_symbol = '△'
animation_symbol2 = '▨'
animation_symbol3 = '⍜'
animation_symbol4 = '⌲'
animation_symbol5 = '▰'
animation_symbol6 = '⌘ '
animation_symbol7 = '⍋'
animation_symbol8 = '▣'
animation_symbol9= '⍍'
animation_symbol10= '⌬'
animation_symbol11= '⬢'


st.markdown(
    f"""
    <div class="snowflake">{animation_symbol11}</div>
    <div class="snowflake">{animation_symbol10}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol3}</div>
    <div class="snowflake">{animation_symbol4}</div>
    <div class="snowflake">{animation_symbol5}</div>
    <div class="snowflake">{animation_symbol6}</div>
    <div class="snowflake">{animation_symbol7}</div>
    <div class="snowflake">{animation_symbol8}</div>
    <div class="snowflake">{animation_symbol2}</div>
    <div class="snowflake">{animation_symbol3}</div>
    <div class="snowflake">{animation_symbol4}</div>
    <div class="snowflake">{animation_symbol5}</div>
    <div class="snowflake">{animation_symbol6}</div>
    <div class="snowflake">{animation_symbol7}</div>
    <div class="snowflake">{animation_symbol8}</div>
    <div class="snowflake">{animation_symbol9}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol3}</div>
    <div class="snowflake">{animation_symbol11}</div>
    """,
    unsafe_allow_html=True,
)

st.image('icon.png')
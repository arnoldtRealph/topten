import streamlit as st
import time
from PIL import Image

st.set_page_config(page_title="Top 10 - Saul Damon High School", layout="centered")

# Student data
students = [
    {"rank": 10, "name": "Constance Moko", "image": "images/moko.jpg"},
    {"rank": 9, "name": "Renaldi Roux", "image": "images/roux.jpg"},
    {"rank": 8, "name": "Beth Jobson", "image": "images/jobson.jpg"},
    {"rank": 7, "name": "Diablo Bock", "image": "images/bock.jpg"},
    {"rank": 6, "name": "Cheniqua Bosman", "image": "images/bosman.jpg"},
    {"rank": 5, "name": "Relebogile Silwana", "image": "images/silwana.jpg"},
    {"rank": 4, "name": "Abigail Beukes", "image": "images/beukes.jpg"},
    {"rank": 3, "name": "Aj September", "image": "images/september.jpg"},
    {"rank": 2, "name": "Mosa Motsoto", "image": "images/motsoto.jpg"},
    {"rank": 1, "name": "Elduwayne Swarts", "image": "images/swarts.jpg"},
]

# Custom diplomatic styling with blue and minimal glow
st.markdown("""
    <style>
        body {
            background: linear-gradient(180deg, #1E3A5F, #3A5F8A);
            color: #F5F6F5;
        }
        .main-title {
            text-align: center;
            font-size: 50px;
            font-family: 'Merriweather', serif;
            color: #F5F6F5;
            text-shadow: 0 0 4px #A8C4E6;
            background: rgba(30, 58, 95, 0.8);
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 40px;
        }
        .fade-text {
            text-align: center;
            font-size: 34px;
            font-family: 'Lora', serif;
            color: #000000;
            margin-top: 20px;
            animation: slideIn 1s ease-in-out;
        }
        .fade-name {
            text-align: center;
            font-size: 30px;
            font-family: 'Lora', serif;
            color: #000000;
            margin-bottom: 20px;
            animation: fadeIn 1.5s ease-in-out;
        }
        .image-container {
            border: 2px solid #A8C4E6;
            border-radius: 8px;
            padding: 5px;
            box-shadow: 0 0 5px #A8C4E6;
            transition: transform 0.3s;
        }
        .image-container:hover {
            transform: scale(1.02);
        }
        .stButton>button {
            background: linear-gradient(45deg, #1E3A5F, #A8C4E6);
            color: #FFFFFF;
            font-family: 'Merriweather', serif;
            font-size: 16px;
            padding: 10px 20px;
            border: none;
            border-radius: 20px;
            box-shadow: 0 0 4px #A8C4E6;
            transition: all 0.3s ease;
            margin: 5px;
        }
        .stButton>button:hover {
            box-shadow: 0 0 8px #A8C4E6;
            transform: translateY(-2px);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-30px); }
            to { opacity: 1; transform: translateX(0); }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@700&family=Lora:wght@400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>Saul Damon High School - Top 10</div>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #000000; font-family: \"Lora\", serif;'>Grade 12 Honours</h3>", unsafe_allow_html=True)

def place_name(rank):
    places = {
        10: "tenth", 9: "ninth", 8: "eighth", 7: "seventh", 6: "sixth",
        5: "fifth", 4: "fourth", 3: "third", 2: "second", 1: "first"
    }
    return places.get(rank, f"{rank}th")

# Initialize session state
if 'slideshow_started' not in st.session_state:
    st.session_state.slideshow_started = False
if 'paused' not in st.session_state:
    st.session_state.paused = False
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0

def toggle_pause():
    st.session_state.paused = not st.session_state.paused

# Create two columns for buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("🎖️ Begin Top 10 Reveal"):
        st.session_state.slideshow_started = True
        st.session_state.current_index = 0
        st.session_state.paused = False

with col2:
    pause_label = "⏸️ Pause" if not st.session_state.paused else "▶️ Resume"
    if st.button(pause_label, disabled=not st.session_state.slideshow_started):
        toggle_pause()

placeholder = st.empty()

if st.session_state.slideshow_started and not st.session_state.paused and st.session_state.current_index < len(students):
    student = students[st.session_state.current_index]
    with placeholder.container():
        st.markdown(f"<div class='fade-text'>In {place_name(student['rank'])} place...</div>", unsafe_allow_html=True)
        
        try:
            img = Image.open(student['image'])
            st.markdown("<div class='image-container'>", unsafe_allow_html=True)
            st.image(img, use_container_width=True, caption=None)
            st.markdown("</div>", unsafe_allow_html=True)
        except FileNotFoundError:
            st.error(f"⚠️ Image not found for {student['name']}")

        st.markdown(f"<div class='fade-name'>{student['name']}</div>", unsafe_allow_html=True)

    time.sleep(5)
    placeholder.empty()
    time.sleep(0.3)
    st.session_state.current_index += 1
    st.rerun()

elif st.session_state.slideshow_started and st.session_state.current_index >= len(students):
    st.balloons()
    st.markdown(
        "<div style='text-align: center; font-family: \"Merriweather\", serif; font-size: 24px; color: #F5F6F5; text-shadow: 0 0 4px #A8C4E6;'>"
        "🎉 End of Ceremony! Congratulations to Our Top Achievers!"
        "</div>",
        unsafe_allow_html=True
    )
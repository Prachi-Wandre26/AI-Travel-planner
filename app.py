import streamlit as st
from travel_planner import get_travel_options
from streamlit_extras.add_vertical_space import add_vertical_space

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# --- HEADER ---
st.markdown(
    """
    <style>
        .main-title {text-align: center; font-size: 36px; color: #007BFF;}
        .sub-title {text-align: center; font-size: 18px; color: #555;}
        .stButton>button {background-color: #007BFF; color: white; width: 100%; font-size: 18px;}
        .stTextInput>div>div>input {font-size: 16px; height: 40px;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title'>🌍 AI-Powered Travel Planner ✈️</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='sub-title'>Find the best travel options with AI recommendations</h3>", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
st.sidebar.header("Settings ⚙️")
st.sidebar.info("🔍 This AI-powered tool helps you find optimal travel options between locations.")

# --- MAIN INPUT SECTION ---
st.write("## 🏙️ Enter Travel Details")

col1, col2 = st.columns(2)
source = col1.text_input("📍 Source Location", placeholder="Enter city or address")
destination = col2.text_input("📍 Destination Location", placeholder="Enter city or address")

add_vertical_space(2)

# --- PROCESS INPUT ---
if st.button("🔎 Find Travel Options"):
    if source and destination:
        with st.spinner("🔄 Finding the best travel options..."):
            travel_results = get_travel_options(source, destination)
        
        st.success("✅ Travel recommendations generated successfully!")
        st.write("### 🚀 Recommended Travel Modes:")
        
        # Display results in a structured way
        for option in travel_results:
            st.markdown(f"""
                <div style="background:#f8f9fa;padding:15px;border-radius:8px;margin-bottom:10px;">
                    <h4>🚗 Mode: {option['mode']}</h4>
                    <p>💰 Estimated Cost: <b>{option['cost']}</b></p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Please enter both source and destination!")

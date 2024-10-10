import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_lottie as st_lottie
import requests
import tempfile
from pathlib import Path

# Set page configuration
st.set_page_config(page_title="Anuvaad", page_icon="🌐", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .big-font {
        font-size:75px !important;
        font-weight: bold;
        color: white;
    }
    .medium-font {
        font-size:30px !important;
        font-weight: bold;
        color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Navbar
selected = option_menu(
    menu_title=None,
    options=["Home", "Translate", "About", "Contact"],
    icons=["house", "translate", "info-circle", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "black"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#4CAF50"},
    }
)

# Update session state based on navbar selection
st.session_state.page = selected

# Function to load Lottie animations with fallback
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Function to display Lottie animation or fallback text
def display_lottie_or_text(lottie_url, fallback_text, height=200):
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie.st_lottie(lottie_json, height=height)
    else:
        st.write(fallback_text)

# Function to save uploaded file
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            return temp_file.name, file_details
    return None, None

# Home Page Content
if st.session_state.page == "Home":
    # Title and description
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<p class="big-font">Welcome to Anuvaad</p>', unsafe_allow_html=True)
        st.markdown('<p class="medium-font">Breaking Language Barriers in Video Content</p>', unsafe_allow_html=True)
        st.write("Anuvaad is your go-to solution for translating audio and subtitles in English videos to multiple languages. Our cutting-edge technology ensures accurate and seamless translations, opening up your content to a global audience.")
        st.write("Whether you're a content creator, educator, or business professional, Anuvaad helps you reach audiences across language barriers with just a few clicks.")
        if st.button("Get Started"):
            st.session_state.page = "Translate"  
    
    with col2:
        display_lottie_or_text(
            "https://assets5.lottiefiles.com/packages/lf20_V9t630.json",
            "🌍 Anuvaad: Bridging Language Barriers",
            height=300
        )
    
    # Features
    st.write("---")
    st.header("Features")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🎥 Video Translation")
        st.write("Translate both audio and subtitles in your videos with high accuracy.")
        st.write("Support for various video formats including MP4, MOV, and AVI.")
    with col2:
        st.subheader("🌍 Multiple Languages")
        st.write("Support for a wide range of global languages including Hindi, Marathi, Tamil, Telgu, Gujrati.")
        st.write("Continuously expanding language offerings to meet global needs.")
    with col3:
        st.subheader("🚀 Fast & Accurate")
        st.write("State-of-the-art AI technology ensures quick processing with high accuracy translations.")
        st.write("Preserve the essence and context of your original content in translations.")

    # How it works
    st.write("---")
    st.header("How It Works")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("1. Upload your English video")
        display_lottie_or_text(
            "https://assets9.lottiefiles.com/packages/lf20_4kx2q32n.json",
            "📤 Upload Video",
            height=200
        )
        st.write("Simply upload your English video file. We support various formats for your convenience.")
    with col2:
        st.write("2. Choose target languages")
        display_lottie_or_text(
            "https://assets2.lottiefiles.com/packages/lf20_qwl4gi2d.json",
            "🗣️ Select Languages",
            height=200
        )
        st.write("Select one or multiple target languages for your video translation.")
    with col3:
        st.write("3. Download your translated video")
        display_lottie_or_text(
            "https://assets5.lottiefiles.com/packages/lf20_V9t630.json",  # Changed animation link
            "⬇️ Download Translated Video",
            height=200
        )
        st.write("Once the translation is complete, easily download your video with translated audio and subtitles.")

      # Call to Action
    st.write("---")
    st.header("Ready to Go Global?")
    st.write("Start translating your videos today and expand your reach to international audiences!")
    
    # Button to switch to the "Translate" page
    if st.button("Start Translating Now"):
        st.session_state.page = "Translate" 

# Translate Page
elif st.session_state.page == "Translate":
    st.title("Upload Your Video")
    st.write("Upload your English video for translation.")

    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
    
    if uploaded_file is not None:
        file_path, file_details = save_uploaded_file(uploaded_file)
        if file_path:
            st.success("File successfully uploaded!")
            st.video(file_path)
            st.json(file_details)
            
            st.write("---")
            st.subheader("Choose Target Languages")
            languages = ["Hindi", "Marathi", "Tamil", "Telgu", "Gujrati"]
            selected_languages = st.multiselect("Select languages for translation", languages)
            
            st.write("---")
            st.subheader("Supers Customization")
            translate_supers = st.selectbox("Do you want to translate the supers?", ["Yes", "No"])
            if translate_supers == "Yes":
                super_color = st.color_picker("Pick the color for the supers text", "#FFFFFF")
                super_size = st.selectbox("Choose the size of the supers text", ["Small", "Medium", "Large"])
            
            if selected_languages:
                if st.button("Start Translation"):
                    st.info("Translation process initiated. This may take a while...")
                    # Here you would typically start your translation process
                    # For now, we'll just show a placeholder message
                    st.success("Translation complete! (This is a placeholder message)")
                    
                    # Add a download button (this is a placeholder, you'd need to implement actual file generation)
                    st.download_button(
                        label="Download Translated Video",
                        data=b"Placeholder data",  # Replace with actual video data
                        file_name="translated_video.mp4",
                        mime="video/mp4"
                    )

# Placeholder for other pages
elif st.session_state.page == "About":
    st.title("About Anuvaad")
    st.write("Learn more about Anuvaad and our mission here.")
elif st.session_state.page == "Contact":
    st.title("Contact Us")
    st.write("Get in touch with our team for support or inquiries.")
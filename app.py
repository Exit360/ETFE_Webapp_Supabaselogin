import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from Home import main
from PIL import Image

load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def sign_up(email, password):
    try:
        user = supabase.auth.sign_up({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Registration failed: {e}")

def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")

def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state.user_email = None
        st.rerun()
    except Exception as e:
        st.error(f"Logout failed: {e}")

def main_app(user_email):
    st.title("🎉 Welcome Page")
    st.success(f"Welcome, {user_email}! 👋")
    main()
    if st.button("Logout"):
        sign_out()

def auth_screen():
    logo = Image.open('images/logo360_s.png')
    
        
    st.image(logo,
     caption='Project Management,Design,Marketing | fabrix360.com',
     use_container_width=150)
    st.title(" ETFE design tools")
    option = st.selectbox("Choose an action:", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    st.header('Tensile structure & ETFE skylight hub in Middle East')
    about = """ fabrix360, Middle East based, is wide scope expert composed of conglomerate of elite expats Engineers and Project Managers with vast experience in tensile structures and air filled cushions(ETFE), robust and real field experience with iconic projects undertaken in Middle East and Worldwide in the last 2 decades.

 fabrix360 aims to offer and extend such vast expertise directly to Fabricators, Clients, Developers, Architects and Consultants into most innovative and feasible way.

We bring to our clients reliable, immediate productive and experienced resources and we strive constantly to be a company that delivers an outstanding results with maximum satisfaction prior, during and after construction.



 """ 
    st.markdown(about,unsafe_allow_html=True)
    st.warning("Disclaimer:The contents of this web applications are for pure learning purposes and cannot be used commercially or firmly. If you seek firm information please contact us or contact your expert")
    web = '<span style="font-style: italic;color: #000080;"><h6><a href="https://www.fabrix360.com/contactus">Contact us</a></h6></span>'
    st.markdown(web,unsafe_allow_html=True)

    if option == "Sign Up" and st.button("Register"):
        user = sign_up(email, password)
        if user and user.user:
            st.success("Registration successful. Please log in.")

    if option == "Login" and st.button("Login"):
        user = sign_in(email, password)
        if user and user.user:
            st.session_state.user_email = user.user.email
            st.success(f"Welcome back, {email}!")
            st.rerun()

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if st.session_state.user_email:
    main_app(st.session_state.user_email)
else:
    auth_screen()
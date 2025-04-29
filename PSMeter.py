import re
import streamlit as st

st.set_page_config(page_title="PASSWORD STRENGTH METER BY MOIZ", page_icon="💪🔒", layout="centered", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton {width: 50%; background-colo #7cAF70; color: white; font-size: 18px; }
    .stButton:hover { background-color: #7cAF70;}
</style>
""", unsafe_allow_html=True)

st.title("Password Strength Meter")
st.write("Enter your password to check its strength")

def check_password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain both upper and lower case characters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit.")

    if re.search(r"\W", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character.")

    if score == 4:
        st.success("**Password is strong.")
    elif score == 3:
        st.info("** Password is medium, may change to strong.")
    else:
        st.error(" ** Weak password")
    
    if feedback:
        with st.expander(" **Improve your password** "):
            for item in feedback:
                st.write(item)
    
    password = st.text_input("Enter your password", type="password", help="Ensure your password is strong.")

    if st.button("Check Password Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("Please enter a password to check its strength.")

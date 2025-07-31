import streamlit as st
import string

def evaluate_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1

    if score <= 2:
        return "🔴 Weak"
    elif score == 3:
        return "🟠 Intermediate"
    else:
        return "🟢 Strong"

# 🎨 Streamlit UI
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:", type="password")

guidelines = """
• Use at least 8 characters.
• Include uppercase and lowercase letters.
• Add numbers and special characters (!@#$%^&*).
• Avoid using personal info (name, birthdate).
• Don’t reuse old passwords.
"""
st.text_area("🔍 Password Guidelines", guidelines, height=150)

if password:
    strength = evaluate_strength(password)
    st.markdown(f"**Strength:** {strength}")
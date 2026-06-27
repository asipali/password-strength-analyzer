import streamlit as st
import re
import math
import random
import string

st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Strength Analyzer")
st.write("Analyze your password security")

password = st.text_input(
    "Enter password",
    type="password"
)

def gen_pass(length=14):
    chars = (
        string.ascii_letters
        + string.digits
        + "!@#$%^&*"
    )

    return ''.join(
        random.choice(chars)
        for _ in range(length)
    )

if password:
    score = 0

    length_check = len(password) >= 8
    upper_check = bool(re.search(r"[A-Z]", password))
    lower_check = bool(re.search(r"[a-z]", password))
    num_check = bool(re.search(r"[0-9]", password))
    splchar_check = bool(
        re.search(
            r'[!@#$%^&*(),.?/:"{}|\\<>]',
            password
        )
    )

    checks = {
        "Length >= 8": length_check,
        "Uppercase letter": upper_check,
        "lowercase letter": lower_check,
        "numbers": num_check,
        "special characters": splchar_check
    }

    for value in checks.values():
        if value:
            score += 1

    charset = 0

    if lower_check:
        charset += 26
    if upper_check:
        charset += 26
    if num_check:
        charset += 10
    if splchar_check:
        charset += 32

    entropy = len(password) * math.log2(charset)

    st.subheader("Security Analysis")

    for check, result in checks.items():
        if result:
            st.success(check)
        else:
            st.error(check)

    progress = score * 20
    st.progress(progress)

    st.subheader("Strength Level")
    st.progress(progress)

    st.write(
        f"Entropy score: {entropy:.2f} bits"
    )

    if entropy < 40:
        st.error("🔴 Weak Password")

    elif entropy < 60:
        st.warning("🟡 Medium Password")

    elif entropy < 80:
        st.success("🟢 Strong Password")

    else:
        st.success("🟢 Excellent Password")
    
    st.subheader("Crack time estimation")

    if entropy < 40:
        st.error(
            "Can be cracked within minutes"
        )
    elif entropy < 60:
        st.warning(
            "Moderately secure"
        )
    else:
        st.success(
            "Very difficult to crack"
        )

    st.subheader("Recommended Strong Password")

    if st.button("Generate Strong Password"):
        st.code(gen_pass())

    if entropy < 60:
        missing = []

        if not length_check:
            missing.append("Increase the password length (minimum 8 characters).")

        if not upper_check:
            missing.append("Add at least one uppercase letter.")

        if not lower_check:
            missing.append("Add at least one lowercase letter.")

        if not num_check:
            missing.append("Include at least one number.")

        if not splchar_check:
            missing.append("Include at least one special character.")

        st.subheader("Suggestions to Improve Your Password")

        for item in missing:
            st.warning(item)

        st.info("""
    • Use at least 12 characters
    • Mix uppercase and lowercase letters
    • Include numbers and symbols
    • Avoid personal information
    • Don't reuse passwords
    """)

    else:
        st.success("🎉 Excellent! Your password follows all recommended security practices.")
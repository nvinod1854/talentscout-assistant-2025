import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import streamlit as st
import re
from email_validator import validate_email, EmailNotValidError
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.storage import Candidate, save_candidate

# -------------------------------
# Validation functions
# -------------------------------
def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def is_valid_phone(phone):
    return re.fullmatch(r"^\+?\d{10,15}$", phone) is not None


# -------------------------------
# Initialize session state
# -------------------------------
if "step" not in st.session_state:
    st.session_state.update({
        "step": "greeting",
        "answers": {},
        "tech_step": 0
    })

st.title("🤖 TalentScout - Hiring Assistant")

# Exit check
def check_exit(user_input: str):
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state["step"] = "end"
        st.rerun()

# -------------------------------
# Greeting
# -------------------------------
if st.session_state["step"] == "greeting":
    st.write("👋 Hello! I’m TalentScout Hiring Assistant. I’ll collect your details and ask some tech-specific questions.")
    st.write("Type **exit** anytime to leave the conversation.")
    if st.button("Start Interview"):
        st.session_state["step"] = "name"
        st.rerun()

# -------------------------------
# Step 1: Full Name
# -------------------------------
elif st.session_state["step"] == "name":
    name = st.text_input("👉 Please enter your full name:", key="name_input")
    if name:
        check_exit(name)
        if len(name.strip().split()) >= 2:
            st.session_state["full_name"] = name.strip()
            st.success("✅ Full Name recorded.")
            st.session_state["step"] = "email"
            st.rerun()
        else:
            st.warning("⚠️ Please enter both first and last name.")

# -------------------------------
# Step 2: Email
# -------------------------------
elif st.session_state["step"] == "email":
    email = st.text_input("👉 Please enter your email:", key="email_input")
    if email:
        check_exit(email)
        if is_valid_email(email.strip()):
            st.session_state["email"] = email.strip()
            st.success("✅ Email recorded.")
            st.session_state["step"] = "phone"
            st.rerun()
        else:
            st.warning("⚠️ Invalid email. Try again.")

# -------------------------------
# Step 3: Phone
# -------------------------------
elif st.session_state["step"] == "phone":
    phone = st.text_input("👉 Please enter your phone number (e.g., +91XXXXXXXXXX):", key="phone_input")
    if phone:
        check_exit(phone)
        if is_valid_phone(phone.strip()):
            st.session_state["phone"] = phone.strip()
            st.success("✅ Phone recorded.")
            st.session_state["step"] = "experience"
            st.rerun()
        else:
            st.warning("⚠️ Invalid phone number. Try again.")

# -------------------------------
# Step 4: Years of Experience
# -------------------------------
elif st.session_state["step"] == "experience":
    exp = st.text_input("👉 How many years of experience do you have?", key="exp_input")
    if exp:
        check_exit(exp)
        if exp.isdigit():
            st.session_state["years_experience"] = int(exp)
            st.success("✅ Experience recorded.")
            st.session_state["step"] = "position"
            st.rerun()
        else:
            st.warning("⚠️ Please enter a number (e.g., 3).")

# -------------------------------
# Step 5: Desired Positions
# -------------------------------
elif st.session_state["step"] == "position":
    pos = st.text_input("👉 Which position(s) are you applying for? (comma-separated)", key="pos_input")
    if pos:
        check_exit(pos)
        st.session_state["desired_positions"] = [p.strip() for p in pos.split(",")]
        st.success("✅ Position(s) recorded.")
        st.session_state["step"] = "location"
        st.rerun()

# -------------------------------
# Step 6: Current Location
# -------------------------------
elif st.session_state["step"] == "location":
    loc = st.text_input("👉 What is your current location?", key="loc_input")
    if loc:
        check_exit(loc)
        st.session_state["location"] = loc.strip()
        st.success("✅ Location recorded.")
        st.session_state["step"] = "techstack"
        st.rerun()

# -------------------------------
# Step 7: Tech Stack
# -------------------------------
elif st.session_state["step"] == "techstack":
    tech = st.text_input("👉 Please list your tech stack (comma-separated, e.g., Python, Django, SQL):", key="tech_input")
    if tech:
        check_exit(tech)
        st.session_state["tech_stack"] = [t.strip() for t in tech.split(",")]
        st.success("✅ Tech stack recorded.")
        st.session_state["step"] = "tech_questions"
        st.session_state["tech_step"] = 0
        st.rerun()

# -------------------------------
# Step 8: Dynamic Tech Questions
# -------------------------------
elif st.session_state["step"] == "tech_questions":
    tech_questions_map = {
        "python": ["What are Python decorators?", "Explain list comprehension in Python.", "What is the GIL in Python?"],
        "django": ["What is Django ORM?", "Explain Django middleware.", "What are Django signals?"],
        "sql": ["What is normalization?", "Difference between INNER JOIN and LEFT JOIN?", "What is an index in SQL?"],
        "java": ["What is the difference between abstract class and interface?", "Explain JVM.", "What is multithreading in Java?"]
    }

    idx = st.session_state["tech_step"]
    techs = st.session_state["tech_stack"]

    # Build dynamic question list
    all_questions = []
    for t in techs:
        t_lower = t.lower()
        if t_lower in tech_questions_map:
            all_questions.extend(tech_questions_map[t_lower][:2])  # take 2 per tech

    if idx < len(all_questions):
        st.subheader(all_questions[idx])
        ans = st.text_area("Your Answer:", key=f"q{idx}")
        if ans:
            st.session_state["answers"][all_questions[idx]] = ans.strip()
            st.session_state["tech_step"] += 1
            st.rerun()
    else:
        st.success("✅ All tech questions answered!")
        st.session_state["step"] = "save"
        st.rerun()

# -------------------------------
# Step 9: Save Candidate & End
# -------------------------------
elif st.session_state["step"] == "save":
    candidate = Candidate(
        full_name=st.session_state["full_name"],
        email=st.session_state["email"],
        phone=st.session_state["phone"],
        years_experience=st.session_state["years_experience"],
        desired_positions=st.session_state["desired_positions"],
        location=st.session_state["location"],
        tech_stack=st.session_state["tech_stack"],
        answers=st.session_state["answers"]
    )
    save_candidate(candidate)
    st.json(candidate.dict())
    st.success("🎯 Candidate data saved successfully!")
    st.write("🙏 Thank you for your time. Our team will review your answers and get back to you soon.")
    st.session_state["step"] = "end"

# -------------------------------
# End Conversation
# -------------------------------
elif st.session_state["step"] == "end":
    st.write("👋 Conversation ended. Have a great day!")
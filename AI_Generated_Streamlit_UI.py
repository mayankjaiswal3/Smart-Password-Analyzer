import string
import random
import streamlit as st

# --- CORE LOGIC ---
WEAK_PASSWORD_THRESHOLD = 4

def count_by_rule(password,rule):
    return sum(1 for i in password if rule(i))

def Password_analyzer(password):
    analysis ={
        "length":len(password),
        "upper_case":count_by_rule(password,str.isupper),
        "lower_case":count_by_rule(password,str.islower),
        "digits":count_by_rule(password,str.isdigit),
        "special":count_by_rule(password,lambda i : i in string.punctuation)
    }
    return analysis
    
def calculate_score(analysis):
    base_score=sum([
        analysis["length"]>= 8,
        analysis["upper_case"] >= 1,
        analysis["lower_case"] >= 1,
        analysis["digits"] >= 1,
        analysis["special"]>= 1
    ])

    bonus_score = sum([
        analysis["length"] >= 12,
        analysis["upper_case"] >= 2,
        analysis["lower_case"] >= 2,
        analysis["digits"] >= 2,
        analysis["special"] >= 2
    ])
    score=base_score+bonus_score
    return score

def security_level(score):
    strengths = [
        "Extremely Weak",
        "Very Weak",
        "Weak",
        "Poor",
        "Fair",
        "Average",
        "Moderate",
        "Good",
        "Strong",
        "Very Strong",
        "Excellent"
    ]
    return strengths[score] if 0 <= score <= 10 else "invalid score"
    
def gen_suggestion(score):
    if score <= WEAK_PASSWORD_THRESHOLD:
        alphalow=random.choices(string.ascii_lowercase,k=4)
        alphaup=random.choices(string.ascii_uppercase,k=3)
        num=random.choices(string.digits,k=3)
        sp_char=random.choices("!@#$%^&*?~",k=2)
        suggested_password=alphalow+alphaup+num+sp_char
        random.shuffle(suggested_password)
        return "".join(suggested_password)

# --- STREAMLIT UI SECTIONS ---

# Page Configuration
st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔒", layout="centered")

# Header
st.title("🔒 Password Strength Analyzer")
st.markdown("Enter your password to check its strength. If it is weak, the analyzer will suggest a stronger alternative for you!")

# User Input
password = st.text_input("Enter your password:", type="password", help="Type your password here to analyze it.")

# Analysis and Results Display
if password:
    main_analysis = Password_analyzer(password)
    score = calculate_score(main_analysis)
    level_of_security = security_level(score)
    suggestion = gen_suggestion(score)

    st.markdown("---")
    
    # Dynamic Color for Score
    if score <= 4:
        color = "red"
    elif score <= 7:
        color = "orange"
    else:
        color = "green"
        
    st.markdown(f"### Security Level: :{color}[{level_of_security}]")
    
    # Progress Bar (Score 0-10 normalized to 0.0-1.0)
    normalized_score = max(0.0, min(score / 10.0, 1.0))
    st.progress(normalized_score)
    st.caption(f"**Security Score:** {score}/10")

    # Metrics Display
    st.subheader("Password Details")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Length", main_analysis['length'])
    col2.metric("Uppercase", main_analysis['upper_case'])
    col3.metric("Lowercase", main_analysis['lower_case'])
    col4.metric("Digits", main_analysis['digits'])
    col5.metric("Special", main_analysis['special'])

    # Password Suggestion Logic
    st.markdown("---")
    if suggestion:
        st.error("⚠️ Your password is weak and can be easily cracked.")
        st.info(f"💡 **Try this suggested strong password instead:** `{suggestion}`")
    elif score >= 8:
        st.success("🎉 Excellent job! Your password is highly secure.")
    else:
        st.warning("Good, but it could be better. Try adding more characters or symbols.")
        
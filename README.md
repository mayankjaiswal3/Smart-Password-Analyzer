# 🔒 Smart Password Strength Analyzer

This project evaluates the strength of a password and suggests a cryptographically secure alternative if the current one falls below the security threshold. 

As a professional building real-world analytics and Python projects, I structured this repository to clearly separate my core backend logic from the frontend presentation.

**[🔗 Click Here to view the Live Web Demo](#)**

## 📂 Repository Structure

To maintain complete transparency, this project is divided into two distinct parts:

1. **`Smart Password Analyzer.py` (Core Logic):** 
   This is my original, pure Python code. It contains the fundamental algorithm I wrote from scratch to analyze password length, character types, calculate precise security scores, and handle the random generation logic.
   
2. **`AI_Generated_Streamlit_UI.py` (Frontend Demo):** 
   Since my primary expertise is in backend Python logic and data analysis rather than frontend development, I leveraged an AI assistant to wrap my original Python algorithm into an interactive Streamlit UI. This allows non-technical users to easily test the logic.

## 🚀 Features
- **Real-Time Analysis:** Analyzes length, uppercase, lowercase, digits, and special characters.
- **Dynamic Security Scoring:** Calculates a precise security score out of 10.
- **Smart Suggestions:** Automatically generates a randomized, highly secure password string if the user's input is weak.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** Streamlit (For UI Demonstration)
- **Libraries:** `string`, `random` (Standard Library)

## 💻 How to Run Locally

Run the following commands in your terminal to test the project:

```bash
# 1. Clone the repository
git clone https://github.com/mayankjaiswal3/Smart-Password-Analyzer.git (https://github.com/mayankjaiswal3/Smart-Password-Analyzer.git)

# 2. Navigate to the directory
cd Smart-Password-Analyzer

# 3. To run the core logic in your terminal
python "Smart Password Analyzer.py"

# 4. To run the Web UI locally (install requirements first)
pip install -r requirements.txt
streamlit run AI_Generated_Streamlit_UI.py

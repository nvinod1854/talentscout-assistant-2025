🤖 TalentScout – Hiring Assistant

An intelligent Hiring Assistant chatbot built with Streamlit + Python for TalentScout, a fictional recruitment agency.
The chatbot screens candidates by collecting their details and asking tech-stack–specific technical questions.

This project demonstrates skills in Prompt Engineering, LLM integration, and Python web app development.


---

✨ Features

Greeting & Exit Handling → Greets candidate, exits on keywords (exit, quit, bye).

Candidate Information Collection → Collects:

Full Name

Email Address

Phone Number

Years of Experience

Desired Position(s)

Current Location

Tech Stack


Dynamic Tech Questions → Generates 3–5 technical questions based on declared stack.

Example: If user enters Python, Django, chatbot asks Python + Django questions.


Input Validation → Ensures correct email, phone number, numeric years of experience.

Fallback Mechanism → Gives helpful message if input is invalid.

Context Handling → Maintains candidate responses step-by-step using st.session_state.

End Conversation → Thanks candidate & saves their responses.

Data Storage → Candidate info stored in a local JSON file (candidates.json) using Pydantic models.



---

📂 Project Structure

talentscout-assistant/
│
├── app/
│   └── main.py            # Streamlit chatbot UI & conversation flow
│
├── src/
│   ├── __init__.py
│   ├── storage.py         # Candidate model + save function
│   ├── logic.py           # (Optional) helper functions
│   └── tech_catalog.py    # Predefined tech question sets
│
├── tests/
│   └── test_logic_storage.py
│
├── candidates.json        # Saved candidate data (auto-created)
├── requirements.txt       # Project dependencies
├── README.md              # Documentation
└── .env.example           # Example environment variables 

⚙️ Installation

1. Clone the Repository

git clone https://github.com/nvinod1854/talentscout-assistant-2025.git
cd talentscout-assistant

2. Create a Virtual Environment

python -m venv .venv

3. Activate the Environment

Windows PowerShell

.venv\Scripts\activate

Linux / macOS

source .venv/bin/activate


4. Install Dependencies

pip install -r requirements.txt

5. Run the Application

streamlit run app/main.py


---

🧑‍💻 Usage Guide

1. Run the app → browser opens at http://localhost:8501/


2. Click Start Interview.


3. Enter candidate details step by step.


4. Declare tech stack → chatbot asks relevant technical questions.


5. At the end → candidate summary is saved in candidates.json.


6. Candidate can type exit anytime to stop the interview.




---

📖 Prompt Design

Greeting Prompt

> “Hello! I’m TalentScout Hiring Assistant. I’ll collect your details and ask some tech-specific questions.”



Information Prompts

Full Name → requires first + last name

Email → validated with email-validator

Phone → regex validation (+91XXXXXXXXXX)

Years of Experience → numeric

Desired Positions → comma-separated list

Location → free text

Tech Stack → comma-separated list


Tech Questions
Example input: Python, SQL
Example output questions:

What are Python decorators?

Explain the Global Interpreter Lock (GIL) in Python.

What is normalization in SQL?


Fallback Prompts

> “⚠️ Invalid input. Please try again.”



Exit Prompt

> “👋 Conversation ended. Thank you for your time.”





---

🔒 Data Handling

Candidate data stored in candidates.json.

Uses Pydantic models for validation.

Emails validated via email-validator.

Data is simulated / anonymized → no external storage, compliant with privacy guidelines.



---

🛠️ Tech Stack

Python 3.10+

Streamlit → frontend UI

Pydantic → schema validation

email-validator → robust email checks



---
## Demo Video

Local run:

streamlit run app/main.py

You can watch the full demo here:
[Demo Video] ([text](https://www.loom.com/share/43c1241ae61d406f9f8796ddb0f6a736?sid=57627c7c-8023-4cb5-8e51-792407bfb4f4))
---

Drive link [https://drive.google.com/file/d/1JUGLlURF5aaCFWe4OqwBRXXZ022ni5yb/view?usp=drivesdk]


---

📝 Challenges & Solutions

Issue: st.experimental_rerun deprecated.

✅ Fixed using st.rerun().


Issue: Pydantic ValidationError for missing fields.

✅ Extended chatbot flow to collect all required fields.


Issue: datetime not JSON serializable.

✅ Fixed using default=str in json.dumps().


Issue: Import error (Candidate not found).

✅ Created proper Candidate model in storage.py.




---

📌 Future Enhancements

🌍 Multilingual support (English, Hindi, Telugu, etc.)

😊 Sentiment analysis to gauge candidate confidence

🎨 Custom styling for better UX (progress bar, side panel summary)

☁️ Cloud deployment (AWS/GCP/Streamlit Cloud)




👨‍💻 Author

N Vinod Rathod
📧 [nvinod18542@gmail.com.com]
🔗 GitHub: [https://github.com/nvinod1854]

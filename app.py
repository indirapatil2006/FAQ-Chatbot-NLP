
import streamlit as st
from chatbot import FAQChatbot

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="College FAQ Assistant",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

/* Colour palette:
   Background: #F7F7F0
   Primary:    #55745B
   Dark green: #304D38
   Accent:     #DCE8D8
   Text:       #29352B
*/

/* Main application background */
.stApp {
    background: #F7F7F0;
    color: #29352B;
}

/* Main content container */
.block-container {
    max-width: 950px;
    width: 100%;
    padding: 2rem 2rem 3rem 2rem;
    margin-left: auto;
    margin-right: auto;
    box-sizing: border-box;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #E8EFE5;
    border-right: 1px solid #D4E1D1;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] li,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label {
    color: #304D38 !important;
}

/* Sidebar heading */
[data-testid="stSidebar"] h2 {
    font-size: 23px;
    font-weight: 700;
}

/* Sidebar dividers */
[data-testid="stSidebar"] hr {
    border-color: #CAD9C6;
}

/* Hero section */
.hero {
    background: linear-gradient(135deg, #FFFFFF, #EAF1E7);
    border: 1px solid #D8E4D4;
    border-radius: 22px;
    padding: 32px;
    margin-bottom: 28px;
    box-shadow: 0 8px 25px rgba(48, 77, 56, 0.07);
}

.hero h1 {
    color: #304D38;
    font-size: 34px;
    font-weight: 750;
    margin: 0;
}

.hero p {
    color: #687B69;
    font-size: 16px;
    margin-top: 12px;
    margin-bottom: 0;
}

/* Section headings */
h2, h3 {
    color: #304D38 !important;
}

/* Chat message containers */
[data-testid="stChatMessage"] {
    background: #FFFFFF;
    border: 1px solid #E0E8DC;
    border-radius: 17px;
    padding: 14px;
    margin-bottom: 12px;
    box-shadow: 0 3px 12px rgba(48, 77, 56, 0.04);
}

/* Chat message text */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li {
    color: #29352B !important;
    line-height: 1.65;
}

/* Suggested question buttons */
.stButton > button {
    width: 100%;
    min-height: 48px;
    background: #FFFFFF;
    color: #405E45;
    border: 1px solid #C9D9C5;
    border-radius: 13px;
    font-weight: 500;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #DCE8D8;
    color: #304D38;
    border-color: #829D80;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: #FFFFFF;
    border: 1px solid #C9D9C5;
    border-radius: 16px;
}

[data-testid="stChatInput"] textarea {
    color: #29352B !important;
}

/* Sidebar clear button */
[data-testid="stSidebar"] .stButton > button {
    background: #55745B;
    color: #FFFFFF !important;
    border: none;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #405E45;
    color: #FFFFFF !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #82917F;
    font-size: 13px;
    padding-top: 30px;
}

/* Responsive layout */
@media (max-width: 650px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 22px;
    }

    .hero h1 {
        font-size: 25px;
    }
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD CHATBOT
# --------------------------------------------------

@st.cache_resource
def load_chatbot():
    return FAQChatbot()


chatbot = load_chatbot()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 Welcome to your College FAQ Assistant. "
                "I can help you with admissions, courses, fees, "
                "library facilities, attendance, scholarships and more. "
                "What would you like to know?"
            )
        }
    ]


# --------------------------------------------------
# CHAT FUNCTION
# --------------------------------------------------

def submit_question(question):

    response, score = chatbot.get_response(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🌿 College Assistant")

    st.write(
        "Your friendly digital assistant for "
        "college-related information."
    )

    st.divider()

    st.markdown("### What can I help with?")

    st.markdown("""
    - 🎓 Admissions
    - 📚 Courses and library
    - 💰 Fees and scholarships
    - 🏫 Hostel facilities
    - 📅 Attendance and exams
    - 💼 Placements and internships
    """)

    st.divider()

    st.markdown("### About this project")

    st.caption(
        "Built using Python, Natural Language Processing, "
        "TF-IDF and cosine similarity."
    )

    if st.button("🗑️ Clear conversation",
                 use_container_width=True):

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello again! 👋 How can I help you today?"
                )
            }
        ]

        st.rerun()


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <h1>🌿 College FAQ Assistant</h1>
    <p>
        Your smart companion for quick and reliable
        college-related answers.
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SUGGESTED QUESTIONS
# --------------------------------------------------

if len(st.session_state.messages) == 1:

    st.markdown("### ✨ Try asking me")

    suggestions = [
        "What are the college timings?",
        "How can I get admission?",
        "What facilities are available in the hostel?",
        "How do I apply for scholarships?"
    ]

    col1, col2 = st.columns(2)

    for index, question in enumerate(suggestions):

        target_col = col1 if index % 2 == 0 else col2

        with target_col:

            if st.button(
                question,
                key=f"suggestion_{index}",
                use_container_width=True
            ):

                submit_question(question)
                st.rerun()


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🌿"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_question = st.chat_input(
    "Ask me anything about your college..."
)

if user_question:

    submit_question(user_question)
    st.rerun()


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    Made with 🌿 using Python and Streamlit
</div>
""", unsafe_allow_html=True)

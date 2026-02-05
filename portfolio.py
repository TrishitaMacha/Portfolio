import streamlit as st
import plotly.express as px
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trishita Macha | Data Analyst & GenAI",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    background-color: #0e1117;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: #ffffff;
}
.hero-sub {
    font-size: 22px;
    color: #a5b4fc;
}
.hero-desc {
    font-size: 18px;
    color: #d1d5db;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 20px;
}

.card {
    background: linear-gradient(145deg, #1f2933, #111827);
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.35);
    transition: transform 0.3s ease;
}
.card:hover {
    transform: translateY(-8px);
}

.stDownloadButton button {
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    border-radius: 12px;
    padding: 10px 22px;
    font-size: 16px;
}
.project-link {
    text-decoration: none;
    color: inherit;
}

.project-link:hover {
    text-decoration: none;
    color: inherit;
    cursor: pointer;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([2,1])

with col1:
    st.markdown("<div class='hero-title'>Hi, I’m Trishita 👋</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Data Analyst • GenAI </div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='hero-desc'>
    B.Tech (ECE) graduate with strong expertise in Python, Data Analysis,
    Streamlit, Power BI, and Generative AI. Passionate about building
    intelligent, data-driven applications and clean analytical dashboards.
    </div>
    """, unsafe_allow_html=True)


# ---------------- NAVIGATION ----------------
tabs = st.tabs(["🏠 About", "📊 Projects", "🛠 Skills", "🎓 Experience", "📄 Resume", "📬 Contact"])

# ---------------- ABOUT ----------------
with tabs[0]:
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <p>
    I am a highly motivated and detail-oriented graduate with hands-on experience
    in data analysis, dashboard development, automation workflows, and AI-powered applications.
    I enjoy working with real-world data, solving problems, and delivering insights
    that improve decision-making.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
with tabs[1]:
    st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # ---- Project 1 ----
    with col1:
        st.markdown("""
        <a href="https://github.com/TrishitaMacha/Career-Guidance-AI-Agent"
           target="_blank"
           class="project-link">
        <div class="card">
        <h3>🤖 Career Guidance AI Agent</h3>
        <p><b>Tech:</b> LangChain, Streamlit, Generative AI</p>
        <ul>
            <li>AI-powered career mentoring & skill recommendations</li>
            <li>Prompt engineering, memory & conversation flow</li>
            <li>Interactive Streamlit UI</li>
        </ul>
        <p><i>Click to view on GitHub →</i></p>
        </div>
        </a>
        """, unsafe_allow_html=True)

    # ---- Project 2 ----
    with col2:
        st.markdown("""
        <a href="https://github.com/TrishitaMacha/Streamlit_projects_with_genai"
           target="_blank"
           class="project-link">
        <div class="card">
        <h3>📄 AI Resume Checker (ATS)</h3>
        <p><b>Tech:</b> Python, Streamlit, Generative AI</p>
        <ul>
            <li>ATS-style resume scoring</li>
            <li>Skill gap & keyword analysis</li>
            <li>Resume improvement suggestions</li>
        </ul>
        <p><i>Click to view on GitHub →</i></p>
        </div>
        </a>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    # ---- Project 3 ----
    with col3:
        st.markdown("""
        <a href="https://github.com/TrishitaMacha/Streamlit_projects_with_genai"
           target="_blank"
           class="project-link">
        <div class="card">
        <h3>📚 Study Companion Chatbot</h3>
        <p><b>Tech:</b> Streamlit, GenAI</p>
        <ul>
            <li>AI-powered study assistant</li>
            <li>Persistent chat interface</li>
            <li>Fast & accurate responses</li>
        </ul>
        <p><i>Click to view on GitHub →</i></p>
        </div>
        </a>
        """, unsafe_allow_html=True)

    # ---- Project 4 ----
    with col4:
        st.markdown("""
        <a href="https://github.com/TrishitaMacha/Ecommerce_Sales_EDA"
           target="_blank"
           class="project-link">
        <div class="card">
        <h3>🛒 E-Commerce Sales Analysis (EDA)</h3>
        <p><b>Tech:</b> Python, Pandas, Matplotlib</p>
        <ul>
            <li>10K+ records analyzed</li>
            <li>Category & region insights</li>
            <li>Profit vs discount analysis</li>
        </ul>
        <p><i>Click to view on GitHub →</i></p>
        </div>
        </a>
        """, unsafe_allow_html=True)


# ---------------- SKILLS ----------------
with tabs[2]:
    st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
        <h4>Technical Skills</h4>
        <ul>
            <li>Python, Java (Basics)</li>
            <li>SQL, Pandas, NumPy, Excel</li>
            <li>Power BI, Tableau</li>
            <li>Streamlit</li>
            <li>LangChain & Generative AI</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h4>Professional Skills</h4>
        <ul>
            <li>Problem Solving</li>
            <li>Communication & Teamwork</li>
            <li>Time Management</li>
            <li>Adaptability & Quick Learning</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------- EXPERIENCE ----------------
with tabs[3]:
    st.markdown("<div class='section-title'>Internship Experience</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>Mastercard Cybersecurity Program – Forage</h4>
    <p>Virtual Internship (Dec 2024 – Jan 2025)</p>
    <ul>
        <li>Designed phishing simulation</li>
        <li>Analyzed cybersecurity threats</li>
        <li>Recommended mitigation strategies</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h4>CITD – VLSI Intern</h4>
    <p>Aug 2024 – Sep 2024</p>
    <ul>
        <li>Designed 16-bit CSLA using BEC</li>
        <li>Gate-level design using Cadence tools</li>
        <li>Timing & delay optimization</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------- RESUME ----------------
with tabs[4]:
    st.markdown("<div class='section-title'>Resume</div>", unsafe_allow_html=True)
    st.download_button(
        "⬇ Download Resume",
        open("TRISHITA_MACHA_Resume.pdf", "rb"),
        file_name="Trishita_Macha_Resume.pdf"
    )

# ---------------- CONTACT ----------------
with tabs[5]:
    st.markdown("<div class='section-title'>Contact</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    📧 Email: machatrishita244@gmail.com  
    📞 Phone: +91 8688751576  
    🔗 LinkedIn: https://www.linkedin.com/in/trish-trishita  
    💻 GitHub: https://github.com/TrishitaMacha
    </div>
    """, unsafe_allow_html=True)


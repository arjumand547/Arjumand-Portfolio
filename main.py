
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Arjumand | Software & AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------- THEME --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
    --bg: #151713;
    --panel: #20231D;
    --lime: #D6FF62;
    --cream: #F3F0E6;
    --muted: #ADB3A3;
    --border: #414735;
}

.stApp {
    background: var(--bg);
    color: var(--cream);
    font-family: 'Space Grotesk', sans-serif;
}

#MainMenu, footer, header {visibility: hidden;}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4, p, label {
    font-family: 'Space Grotesk', sans-serif !important;
}

h1, h2, h3, h4, p, label {
    color: var(--cream);
}

a {color: var(--lime) !important;}

@keyframes rise {
    from {opacity: 0; transform: translateY(22px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes floatPhoto {
    0%, 100% {transform: translateY(0) rotate(0deg);}
    50% {transform: translateY(-10px) rotate(0.5deg);}
}

@keyframes glowPhoto {
    0%, 100% {
        filter: drop-shadow(0 0 8px rgba(214,255,98,.10));
    }
    50% {
        filter: drop-shadow(0 0 24px rgba(214,255,98,.32));
    }
}

@keyframes ringSpin {
    from {transform: rotate(0deg);}
    to {transform: rotate(360deg);}
}

@keyframes ticker {
    from {transform: translateX(0);}
    to {transform: translateX(-50%);}
}

@keyframes pulse {
    0%, 100% {opacity: 1;}
    50% {opacity: .35;}
}

.hero {
    background:
        radial-gradient(ellipse at top right,
        rgba(214,255,98,.08), transparent 48%),
        linear-gradient(145deg, #25291F, #1C201A);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: clamp(24px, 4vw, 44px);
    min-height: 390px;
    animation: rise .8s ease both;
}

.eyebrow, .section-label, .project-type {
    color: var(--lime) !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 11px;
    letter-spacing: 1.5px;
}

.hero-title {
    font-size: clamp(35px, 4.3vw, 60px);
    line-height: 1.08;
    letter-spacing: -2px;
    font-weight: 700;
    margin: 20px 0;
}

.lime {color: var(--lime) !important;}
.muted {color: var(--muted) !important;}

.status-dot {
    display: inline-block;
    height: 8px;
    width: 8px;
    border-radius: 50%;
    background: var(--lime);
    margin-right: 8px;
    animation: pulse 1.6s infinite;
}

/* PHOTO: floating motion, glow and border */
div[data-testid="stImage"] {
    position: relative;
    animation: floatPhoto 4s ease-in-out infinite;
    padding: 9px;
    border: 1px solid rgba(214,255,98,.75);
    border-radius: 22px;
    background: linear-gradient(145deg, #303827, #191C17);
    box-shadow: 0 15px 40px rgba(0,0,0,.25);
    transition: border-color .3s ease, box-shadow .3s ease;
}

div[data-testid="stImage"]::before {
    content: "";
    position: absolute;
    inset: -5px;
    border: 1px dashed rgba(214,255,98,.55);
    border-radius: 26px;
    pointer-events: none;
    animation: ringSpin 22s linear infinite;
}

div[data-testid="stImage"] img {
    border-radius: 15px;
    animation: glowPhoto 4s ease-in-out infinite;
}

/* Section headings */
.section-heading {
    font-size: clamp(28px, 3.7vw, 40px);
    font-weight: 700;
    letter-spacing: -1px;
    margin-bottom: 20px;
}

.section-label {
    margin-top: 12px;
}

/* Animated project and information cards */
.project, .info-card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 17px;
    padding: 23px;
    margin-bottom: 12px;
    transition: transform .25s ease, border-color .25s ease,
                box-shadow .25s ease;
    animation: rise .7s ease both;
}

.project {min-height: 300px;}

.project:hover, .info-card:hover {
    transform: translateY(-5px);
    border-color: var(--lime);
    box-shadow: 0 12px 30px rgba(0,0,0,.20);
}

.project p, .info-card p {
    color: var(--muted);
    line-height: 1.65;
}

.metric {
    background: var(--panel);
    border-top: 2px solid var(--lime);
    border-radius: 5px 5px 13px 13px;
    padding: 18px 7px;
    text-align: center;
    transition: transform .25s ease;
}

.metric:hover {transform: translateY(-5px);}

.metric strong {
    display: block;
    color: var(--lime);
    font-size: 27px;
}

.metric span {
    color: var(--muted);
    font-size: 10px;
    letter-spacing: .5px;
}

.tag {
    display: inline-block;
    padding: 8px 12px;
    margin: 4px;
    border-radius: 8px;
    background: #292E23;
    border: 1px solid #424B35;
    color: var(--cream);
    font-size: 13px;
    transition: .2s ease;
}

.tag:hover {
    color: var(--lime);
    border-color: var(--lime);
    transform: translateY(-3px);
}

.ticker {
    overflow: hidden;
    white-space: nowrap;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    padding: 16px 0;
    margin: 28px 0;
}

.ticker-track {
    display: inline-block;
    color: var(--lime);
    font: 12px 'DM Mono', monospace;
    letter-spacing: 2px;
    animation: ticker 32s linear infinite;
}

.ticker:hover .ticker-track {animation-play-state: paused;}

hr {border-color: var(--border) !important;}

/* Highly visible buttons */
div[data-testid="stLinkButton"] a {
    background: var(--lime) !important;
    color: #151713 !important;
    border: 1px solid var(--lime) !important;
    border-radius: 10px !important;
    min-height: 45px;
    font-weight: 700 !important;
    transition: .25s ease !important;
}

div[data-testid="stLinkButton"] a * {
    color: #151713 !important;
}

div[data-testid="stLinkButton"] a:hover {
    background: var(--cream) !important;
    border-color: var(--cream) !important;
    transform: translateY(-3px);
}

div.stButton > button {
    background: #292E23 !important;
    color: var(--lime) !important;
    border: 1px solid #596447 !important;
    border-radius: 10px !important;
    min-height: 44px;
    font-weight: 700 !important;
}

div.stButton > button:hover {
    border-color: var(--lime) !important;
    background: #353C2B !important;
}

@media (max-width: 700px) {
    .hero-title {letter-spacing: -1px;}
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .project {min-height: auto;}
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: .01ms !important;
    }
}
</style>
""", unsafe_allow_html=True)


# -------------------- TOP BAR --------------------
st.markdown("""
<div style="display:flex;justify-content:space-between;
align-items:center;gap:12px;flex-wrap:wrap;padding:8px 0 25px;">
    <div style="font-size:25px;font-weight:700;">
        ARJUMAND<span style="color:#D6FF62;">®</span>
    </div>
    <div style="font:11px 'DM Mono',monospace;color:#ADB3A3;">
        PAKISTAN / SOFTWARE & AI
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------- HERO --------------------
text_col, photo_col = st.columns([1.55, 0.8], gap="large")

with text_col:
    st.markdown("""
    <div class="hero">
        <p class="eyebrow">✳ SOFTWARE DEVELOPER / PROBLEM SOLVER</p>
        <h1 class="hero-title">
            I THINK IN<br>
            <span class="lime">ALGORITHMS.</span><br>
            I BUILD SOLUTIONS.
        </h1>
        <p style="font-size:16px;line-height:1.8;">
            I'm <b>Syed Arjumand Haider Shah</b>, a BS Artificial
            Intelligence student at BZU. I've built web applications
            and real-world software solutions that address practical
            business problems.
        </p>
        <p style="font-size:15px;color:#ADB3A3;">
            I break problems into algorithms and use AI-assisted
            development to turn ideas into working software.
        </p>
        <p style="font-size:12px;color:#ADB3A3;">
            <span class="status-dot"></span>
            OPEN TO FREELANCE PROJECTS & COLLABORATION
        </p>
    </div>
    """, unsafe_allow_html=True)

with photo_col:
    photo = Path(__file__).parent / "profile.jpg"

    if photo.exists():
        st.image(str(photo), use_container_width=True)
        st.markdown("""
        <p style="text-align:center;color:#ADB3A3;font-size:11px;
        font-family:'DM Mono',monospace;">
            SYED ARJUMAND HAIDER SHAH
        </p>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-card" style="text-align:center;padding:50px 15px;">
            <div style="font-size:65px;color:#D6FF62;">✳</div>
            <h3>Your photo goes here</h3>
            <p>Save your picture as profile.jpg beside main.py.</p>
        </div>
        """, unsafe_allow_html=True)


# -------------------- CONTACT BUTTONS --------------------
a, b, c = st.columns(3)

with a:
    st.link_button("GITHUB PROFILE ↗",
                   "https://github.com/arjumand547",
                   use_container_width=True)

with b:
    st.link_button("WHATSAPP ↗",
                   "https://wa.me/923467124890",
                   use_container_width=True)

with c:
    st.link_button("EMAIL ME ↗",
                   "mailto:haiderarjumand14@gmail.com",
                   use_container_width=True)


# -------------------- SKILL TICKER --------------------
st.markdown("""
<div class="ticker">
  <div class="ticker-track">
    PYTHON ✳ PROBLEM SOLVING ✳ DATA ANALYTICS ✳
    ARTIFICIAL INTELLIGENCE ✳ SOFTWARE DEVELOPMENT ✳ SQL ✳
    PYTHON ✳ PROBLEM SOLVING ✳ DATA ANALYTICS ✳
    ARTIFICIAL INTELLIGENCE ✳ SOFTWARE DEVELOPMENT ✳ SQL ✳
  </div>
</div>
""", unsafe_allow_html=True)


# -------------------- SNAPSHOT WIDGETS --------------------
st.markdown('<p class="section-label">01 / THE SNAPSHOT</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">What I bring to the table.</div>',
            unsafe_allow_html=True)

columns = st.columns(4)
for col, number, label in zip(
    columns,
    ["02", "AI +", "SQL", "∞"],
    ["FEATURED WEB APPS", "AI-ASSISTED WORKFLOW",
     "DATABASE SOLUTIONS", "PROBLEM-SOLVING MINDSET"]
):
    with col:
        st.markdown(
            f'<div class="metric"><strong>{number}</strong>'
            f'<span>{label}</span></div>',
            unsafe_allow_html=True
        )

st.markdown("---")


# -------------------- PROJECTS --------------------
st.markdown('<p class="section-label">02 / SELECTED WORK</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Built to solve problems.</div>',
            unsafe_allow_html=True)

p1, p2 = st.columns(2, gap="large")

with p1:
    st.markdown("""
    <div class="project">
        <p class="project-type">01 — BUSINESS ANALYTICS</p>
        <h3>◈ InsightFlow</h3>
        <p>Transforms uploaded CSV datasets into useful business insights.</p>
        <p>✳ Interactive charts, filters and search</p>
        <p>✳ KPI cards and downloadable reports</p>
        <p>✳ SQLite storage and theme switching</p>
        <p style="color:#D6FF62;">PYTHON · STREAMLIT · PANDAS · PLOTLY · SQLITE</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("LIVE DEMO ↗",
                   "https://arjumand547-insightflow.streamlit.app/",
                   use_container_width=True)
    st.link_button("SOURCE CODE ↗",
                   "https://github.com/arjumand547/InsightFlow",
                   use_container_width=True)

with p2:
    st.markdown("""
    <div class="project">
        <p class="project-type">02 — ORGANIZATIONAL SOFTWARE</p>
        <h3>◈ Employee Management System</h3>
        <p>Manages employee information across organizational departments.</p>
        <p>✳ Complete create, read, update and delete operations</p>
        <p>✳ Search and filtering</p>
        <p>✳ Interactive charts and reports</p>
        <p style="color:#D6FF62;">PYTHON · STREAMLIT · PANDAS · SQLITE · PLOTLY</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("LIVE DEMO ↗",
                   "https://employee-management-system-arjumand547.streamlit.app/",
                   use_container_width=True)
    st.link_button("SOURCE CODE ↗",
                   "https://github.com/arjumand547/Employee_Management_System",
                   use_container_width=True)

st.markdown("---")


# -------------------- EXPERIENCE --------------------
st.markdown('<p class="section-label">03 / EXPERIENCE</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Beyond the classroom.</div>',
            unsafe_allow_html=True)

experience = [
    ("01 / BUSINESS SOFTWARE", "🌱 Fertilizer Company Inventory System",
     "Developed inventory management software for a Lahore-based fertilizer company."),
    ("02 / FREELANCE", "↗ Fiverr & Client-Oriented Work",
     "Worked on Fiverr and gained experience with practical software requirements."),
    ("03 / ACADEMIC PROJECTS", "⌘ University Software Projects",
     "Built university projects while strengthening programming and database skills.")
]

for label, title, description in experience:
    st.markdown(f"""
    <div class="info-card">
        <p class="eyebrow">{label}</p>
        <h3>{title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")


# -------------------- SKILLS --------------------
st.markdown('<p class="section-label">04 / MY TOOLKIT</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Tools are useful. Thinking is essential.</div>',
            unsafe_allow_html=True)

groups = {
    "PROGRAMMING": ["Python", "C++", "OOP", "Problem Solving", "Algorithms"],
    "DATA & VISUALIZATION": ["Pandas", "Plotly", "Data Analysis"],
    "DATABASES": ["MySQL", "SQLite3", "SQL"],
    "DEVELOPMENT": ["Streamlit", "Web Applications", "AI-Assisted Development"],
    "COMPUTER SCIENCE": ["Machine Learning Basics", "Computer Networks"]
}

for heading, skills in groups.items():
    st.markdown(f'<p class="eyebrow">{heading}</p>',
                unsafe_allow_html=True)
    tags = "".join(f'<span class="tag">{skill}</span>' for skill in skills)
    st.markdown(tags, unsafe_allow_html=True)

st.markdown("---")


# -------------------- EDUCATION --------------------
st.markdown('<p class="section-label">05 / EDUCATION</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Always learning.</div>',
            unsafe_allow_html=True)

e1, e2 = st.columns(2, gap="large")

with e1:
    st.markdown("""
    <div class="info-card">
        <p class="eyebrow">UNIVERSITY</p>
        <h3>🎓 BS Artificial Intelligence</h3>
        <p><b>Bahauddin Zakariya University (BZU)</b></p>
        <p>Currently pursuing an undergraduate degree.</p>
    </div>
    """, unsafe_allow_html=True)

with e2:
    st.markdown("""
    <div class="info-card">
        <p class="eyebrow">ONLINE LEARNING</p>
        <h3>🤖 Machine Learning — Kaggle</h3>
        <p>Completed a Kaggle machine learning course as part of independent learning.</p>
    </div>
    """, unsafe_allow_html=True)

st.link_button("EXPLORE KAGGLE LEARN ↗",
               "https://www.kaggle.com/learn",
               use_container_width=True)

st.markdown("---")


# -------------------- CONTACT --------------------
st.markdown('<p class="section-label">06 / CONTACT</p>',
            unsafe_allow_html=True)
st.markdown('<div class="section-heading">Have a problem? Let’s solve it.</div>',
            unsafe_allow_html=True)
st.markdown('<p class="muted">Software projects, collaboration and freelance inquiries.</p>',
            unsafe_allow_html=True)

c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown("""
    <div class="info-card">
        <h3>WhatsApp</h3>
        <p>Message me directly.</p>
        <p style="color:#D6FF62;">0346 7124890</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("MESSAGE ON WHATSAPP ↗",
                   "https://wa.me/923467124890",
                   use_container_width=True)

with c2:
    st.markdown("""
    <div class="info-card">
        <h3>Email</h3>
        <p>Send a project inquiry.</p>
        <p style="color:#D6FF62;overflow-wrap:anywhere;">
            haiderarjumand14@gmail.com
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("SEND AN EMAIL ↗",
                   "mailto:haiderarjumand14@gmail.com",
                   use_container_width=True)

with c3:
    st.markdown("""
    <div class="info-card">
        <h3>GitHub</h3>
        <p>Explore my code and projects.</p>
        <p style="color:#D6FF62;">@arjumand547</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("VISIT MY GITHUB ↗",
                   "https://github.com/arjumand547",
                   use_container_width=True)


# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("""
<div style="text-align:center;padding:20px 0;">
    <p style="color:#D6FF62;font:12px 'DM Mono',monospace;">
        THINK CLEARLY. SOLVE PROBLEMS. BUILD USEFUL THINGS.
    </p>
    <p style="color:#ADB3A3;font-size:12px;">
        © 2026 Syed Arjumand Haider Shah · Built with Python & Streamlit
    </p>
</div>
""", unsafe_allow_html=True)

import os
import streamlit as st
import time
import re
import urllib.request
import urllib.parse

# --- PROFESSIONAL EDITORIAL THEME ---
os.makedirs(".streamlit", exist_ok=True)
config_path = ".streamlit/config.toml"
with open(config_path, "w") as f:
    f.write("""
[theme]
primaryColor = "#287C78"
backgroundColor = "#F5F6F3"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#1F2937"
font = "sans serif"
    """)

# --- PAGE SETUP ---
st.set_page_config(page_title="AI Agent Architecture", page_icon="🌌", layout="wide")

# --- REFINED PROFESSIONAL UI STYLING ---
st.markdown("""
<style>
    :root {
        --ink: #1F2937;
        --muted: #667085;
        --teal: #287C78;
        --teal-soft: #E8F2F0;
        --paper: #F5F6F3;
        --surface: #FFFFFF;
        --line: #E3E8E5;
        --gold: #B68A4A;
    }

    .stApp {
        background: #F5F6F3;
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(245,246,243,0.92);
    }

    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid var(--line);
    }

    .fade-in {
        animation: fadeUp 0.55s ease-out both;
    }

    .delay-1 { animation-delay: 0.08s; }
    .delay-2 { animation-delay: 0.16s; }
    .delay-3 { animation-delay: 0.24s; }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(12px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* HERO SECTION */
    .hero-container {
        text-align: center;
        margin-top: 7vh;
        padding: 44px 36px;
    }

    .hero-title {
        font-size: clamp(2.8rem, 6vw, 4.4rem);
        font-weight: 800;
        letter-spacing: -2px;
        color: #1F2937;
        margin-bottom: 12px;
        line-height: 1.12;
    }

    .hero-subtitle {
        font-size: 1.35rem;
        color: #287C78;
        font-weight: 600;
        margin-bottom: 24px;
        letter-spacing: 0.2px;
    }

    .hero-text {
        font-size: 1.05rem;
        color: #667085;
        max-width: 700px;
        margin: 0 auto 42px auto;
        line-height: 1.8;
    }

    /* CONCEPT CARDS */
    .concept-card {
        background: #FFFFFF;
        color: #1F2937;
        padding: 25px;
        border-radius: 14px;
        border: 1px solid #E3E8E5;
        border-top: 3px solid #287C78;
        margin-bottom: 22px;
        box-shadow: 0 5px 18px rgba(31,41,55,0.045);
        transition: transform 0.22s ease, box-shadow 0.22s ease;
    }

    .concept-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 26px rgba(31,41,55,0.09);
    }

    .concept-card h3 {
        margin-top: 0;
        color: #246D69;
        font-size: 1.25rem;
        font-weight: 700;
    }

    .concept-card p {
        color: #526071;
        font-size: 1.02rem;
        line-height: 1.7;
    }

    /* DEVELOPER TERMINAL */
    .mac-window {
        border-radius: 12px;
        border: 1px solid #26394B;
        background: #172536;
        overflow: hidden;
        margin-bottom: 20px;
        box-shadow: 0 10px 24px rgba(31,41,55,0.12);
    }

    .mac-header {
        background: #213449;
        padding: 12px 15px;
        display: flex;
        gap: 8px;
        align-items: center;
        border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .mac-dot {
        width: 11px;
        height: 11px;
        border-radius: 50%;
    }

    .dot-red { background-color: #D97770; }
    .dot-yel { background-color: #D6A85F; }
    .dot-grn { background-color: #6EAA8A; }

    .terminal-body {
        padding: 20px;
        color: #D6E2EA;
        font-family: 'SFMono-Regular', Consolas, monospace;
        font-size: 0.92rem;
        line-height: 1.75;
    }

    /* BUTTONS */
    .stButton > button {
        border-radius: 9px !important;
        padding: 0.68rem 1.1rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        border: 1px solid #D5DEDA !important;
    }

    .stButton > button[kind="primary"] {
        background: #287C78 !important;
        color: #FFFFFF !important;
        border: 1px solid #287C78 !important;
        box-shadow: 0 3px 8px rgba(40,124,120,0.16) !important;
    }

    .stButton > button[kind="primary"]:hover {
        background: #216965 !important;
        border-color: #216965 !important;
        transform: translateY(-1px);
        box-shadow: 0 6px 14px rgba(40,124,120,0.2) !important;
    }

    .stButton > button[kind="secondary"] {
        background: #FFFFFF !important;
        color: #344054 !important;
        border: 1px solid #D5DEDA !important;
    }

    .stButton > button[kind="secondary"]:hover {
        border-color: #287C78 !important;
        color: #246D69 !important;
        background: #F7FBF9 !important;
    }

    /* QUIZ OPTIONS */
    div[role="radiogroup"] {
        gap: 10px;
        margin-top: 14px;
        margin-bottom: 26px;
    }

    div[role="radiogroup"] label {
        background: #FFFFFF !important;
        border: 1px solid #E0E6E2 !important;
        border-radius: 10px !important;
        padding: 16px 20px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
    }

    div[role="radiogroup"] div[data-testid="stMarkdownContainer"] p {
        font-size: 1.04rem !important;
        color: #344054 !important;
        font-weight: 500 !important;
        margin: 0 !important;
    }

    div[role="radiogroup"] label:hover {
        border-color: #287C78 !important;
        background: #F3F8F6 !important;
        box-shadow: 0 4px 12px rgba(40,124,120,0.08) !important;
    }

    /* PROGRESS BAR */
    [data-testid="stProgress"] > div > div > div {
        background: #287C78 !important;
    }

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E3E8E5;
        border-radius: 12px;
        padding: 14px;
    }

    /* STATUS COLORS */
    .log-success {
        color: #8DD1AD;
        font-weight: bold;
    }

    .log-error {
        color: #F2A6A0;
        font-weight: bold;
    }

    .log-action {
        color: #D9B477;
        font-weight: bold;
    }

    /* NAVIGATION */
    .nav-spacer {
        margin: 42px 0;
        border-top: 1px solid #E0E6E2;
        padding-top: 28px;
    }

    h1, h2, h3, h4 {
        color: #1F2937;
        letter-spacing: -0.3px;
    }

    p, li {
        line-height: 1.65;
    }

    code {
        color: #246D69 !important;
        background: #EAF2EF !important;
        border-radius: 4px;
        padding: 0.12em 0.3em;
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after {
            animation-duration: 0.01ms !important;
            transition-duration: 0.01ms !important;
        }
    }
</style>
""", unsafe_allow_html=True)


# --- STATE ROUTING & MEMORY ---

if "current_phase" not in st.session_state:
    st.session_state.current_phase = 0

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 1

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0


def set_phase(phase_num):
    st.session_state.current_phase = phase_num
    if phase_num == 3:
        st.session_state.quiz_step = 1
        st.session_state.quiz_score = 0


def advance_quiz(is_correct):
    if is_correct:
        st.session_state.quiz_score += 1
    st.session_state.quiz_step += 1


# --- DYNAMIC HEADER & PROGRESS ---

if st.session_state.current_phase > 0:
    st.markdown(
        "<h1 style='font-weight:800; background: linear-gradient(to right, #287C78, #B68A4A); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🌌 AI Agent Architecture</h1>",
        unsafe_allow_html=True
    )
    progress_map = {1: 33, 2: 66, 3: 100}
    st.progress(
        progress_map[st.session_state.current_phase],
        text=f"Masterclass Phase {st.session_state.current_phase} of 3"
    )
    st.divider()


# ==========================================
# PHASE 0: THE HERO LANDING PAGE
# ==========================================

if st.session_state.current_phase == 0:
    st.markdown("""
    <div class='hero-container fade-in'>
        <div class='hero-title'>AI Agent Architect</div>
        <div class='hero-subtitle'>Interactive Developer Masterclass</div>
        <div class='hero-text'>
            Generative AI is just the beginning. True enterprise engineering requires systems that can reason, act, and interface securely with live data pipelines.
            Enter the masterclass to build your first autonomous ReAct loop.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        st.markdown("<div class='fade-in delay-2'>", unsafe_allow_html=True)
        st.button(
            "Initialize Environment",
            type="primary",
            use_container_width=True,
            on_click=set_phase,
            args=(1,)
        )
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# PHASE 1: EXPANDED THEORY
# ==========================================

elif st.session_state.current_phase == 1:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("Phase 1: Deconstructing the Engine")
    st.write(
        "To build enterprise-grade AI, we must bridge the gap between predictive text and executable Python code."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("""
        <div class='concept-card fade-in delay-1'>
            <h3>1. The Hallucination Barrier</h3>
            <p>LLMs are mathematical text predictors. If you ask it to compute <code>4,582 * 9,912</code>, it predicts the next likely token based on training data. It does not calculate. This guarantees hallucinations in production environments.</p>
        </div>

        <div class='concept-card fade-in delay-2'>
            <h3>2. Tool Binding & JSON Routing</h3>
            <p>We bypass this by giving the AI <b>Tools</b> (Python scripts). We alter the System Prompt: <i>"For exact data, output a JSON block like <code>{'action': 'calculator', 'input': '4582*9912'}</code>."</i> Our backend intercepts this, executes the code, and feeds the result back.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='concept-card fade-in delay-1'>
            <h3>3. The ReAct Cognitive Loop</h3>
            <p>To prevent chaotic behavior, we enforce a strict 4-step execution trace:</p>
            <ul style="color:#526071;">
                <li>🧠 <b>Thought:</b> Analyze the query.</li>
                <li>🛠️ <b>Action:</b> Trigger the JSON tool.</li>
                <li>👀 <b>Observation:</b> Read backend output.</li>
                <li>🗣️ <b>Final Answer:</b> Summarize to user.</li>
            </ul>
        </div>

        <div class='concept-card fade-in delay-2'>
            <h3>4. Security & Guardrails</h3>
            <p>In production, letting AI execute code is dangerous. We must <b>sanitize</b> the JSON output. If the AI hallucinates a tool that doesn't exist, our routing engine must gracefully catch the error instead of crashing the server.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='fade-in delay-3'>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='color:#1F2937; margin-top:20px;'>Live Data Pipeline Visualization</h3>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='mac-window'>
        <div class='mac-header'>
            <div class='mac-dot dot-red'></div>
            <div class='mac-dot dot-yel'></div>
            <div class='mac-dot dot-grn'></div>
            <span style='color:#94A3B8; margin-left:10px; font-size:0.8rem;'>pipeline.log</span>
        </div>
        <div class='terminal-body'>> <b>USER:</b> "What is the weather?"<br>
        > <span class='log-action'>AGENT (Thought):</span> Live data required. Formulating JSON.<br>
        > <span class='log-action'>AGENT (Action):</span> {"tool": "weather_api", "target": "local"}<br>
        > <b>PYTHON (Execution):</b> requests.get('https://wttr.in') ... <span class='log-success'>[200 OK]</span><br>
        > <b>PYTHON (Observation):</b> "Sunny, 32C"<br>
        > <b>AGENT (Final Answer):</b> "It is currently Sunny and 32C."</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='nav-spacer fade-in delay-3'></div>", unsafe_allow_html=True)

    _, col_nav = st.columns([5, 1])
    with col_nav:
        st.button(
            "Proceed to Phase 2 ➡️",
            type="primary",
            use_container_width=True,
            on_click=set_phase,
            args=(2,)
        )


# ==========================================
# PHASE 2: STRUCTURED INTERACTIVE LAB
# ==========================================

elif st.session_state.current_phase == 2:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("Phase 2: The X-Ray Sandbox")
    st.markdown(
        "**Experimentation Protocol:** Turn tools on and off to simulate system failures, or leave them on to watch the AI successfully scrape live internet data."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    lab_col1, lab_col2 = st.columns([1, 1.2], gap="large")

    with lab_col1:
        st.markdown("<div class='fade-in delay-1'>", unsafe_allow_html=True)
        st.markdown(
            "<h4 style='color:#1F2937; margin-bottom:10px;'>🎛️ Engine Controls</h4>",
            unsafe_allow_html=True
        )

        calc_on = st.toggle("🧮 Local Calculator Tool", value=True)
        weather_on = st.toggle("☁️ Live Internet API Tool", value=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='fade-in delay-2'>", unsafe_allow_html=True)
        st.markdown(
            "<h4 style='color:#1F2937; margin-bottom:10px;'>💻 Server Execution Logs</h4>",
            unsafe_allow_html=True
        )

        terminal_ui = st.empty()
        terminal_ui.markdown("""
        <div class='mac-window'>
            <div class='mac-header'>
                <div class='mac-dot dot-red'></div>
                <div class='mac-dot dot-yel'></div>
                <div class='mac-dot dot-grn'></div>
                <span style='color:#94A3B8; margin-left:10px; font-size:0.8rem;'>server_trace.sh</span>
            </div>
            <div class='terminal-body'>System Idle. Awaiting ReAct trigger...</div>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            "🧹 Flush Logs",
            type="secondary",
            use_container_width=True,
            on_click=lambda: st.session_state.chat_log.clear() or st.rerun()
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with lab_col2:
        st.markdown("<div class='fade-in delay-3'>", unsafe_allow_html=True)
        st.markdown(
            "<h4 style='color:#1F2937; margin-bottom:10px;'>📱 Client Interface</h4>",
            unsafe_allow_html=True
        )

        chat_container = st.container(height=500, border=True)
        with chat_container:
            for msg in st.session_state.chat_log:
                with st.chat_message(msg["role"]):
                    st.write(msg["content"])

        user_input = st.chat_input(
            "Ask: 'Multiply 850 by 12' or 'Weather in Tokyo'"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        if user_input:
            st.session_state.chat_log.append(
                {"role": "user", "content": user_input}
            )
            st.rerun()

        if (
            len(st.session_state.chat_log) > 0
            and st.session_state.chat_log[-1]["role"] == "user"
        ):
            latest_input = st.session_state.chat_log[-1]["content"]

            with chat_container:
                with st.chat_message("assistant"):
                    numbers = re.findall(r'\d+', latest_input)

                    if (
                        "multiply" in latest_input.lower()
                        or "*" in latest_input.lower()
                        or len(numbers) >= 2
                    ):
                        if calc_on:
                            terminal_ui.markdown(
                                f"<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'>[TRACE INIT]<br>> THOUGHT: Math required.<br>> <span class='log-action'>ACTION: trigger_calc()</span><br>> INPUT: {numbers[0]} * {numbers[1]}</div></div>",
                                unsafe_allow_html=True
                            )
                            with st.spinner("Processing ReAct Loop..."):
                                time.sleep(1)
                                ans = int(numbers[0]) * int(numbers[1])
                                terminal_ui.markdown(
                                    f"<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'>[TRACE INIT]<br>> THOUGHT: Math required.<br>> <span class='log-action'>ACTION: trigger_calc()</span><br>> INPUT: {numbers[0]} * {numbers[1]}<br><span class='log-success'>> OBSERVATION: {ans}</span><br>> FINAL_ANSWER GENERATED.</div></div>",
                                    unsafe_allow_html=True
                                )
                                final_text = f"Routed to Calculator Engine. Answer: **{ans:,}**."
                                st.write(final_text)
                                st.session_state.chat_log.append(
                                    {"role": "assistant", "content": final_text}
                                )
                        else:
                            terminal_ui.markdown(
                                "<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'><span class='log-error'>[FATAL ERROR]</span><br>> THOUGHT: Math required.<br>> <span class='log-action'>ACTION: trigger_calc()</span><br><span class='log-error'>> EXCEPTION: Tool Offline!</span></div></div>",
                                unsafe_allow_html=True
                            )
                            with st.spinner("Attempting calculation..."):
                                time.sleep(1)
                                final_text = "❌ **Error:** Calculator Engine is disabled in the control panel."
                                st.error(final_text)
                                st.session_state.chat_log.append(
                                    {"role": "assistant", "content": final_text}
                                )

                    elif "weather" in latest_input.lower():
                        if weather_on:
                            location = "Chennai"
                            if " in " in latest_input.lower():
                                location = (
                                    latest_input.lower()
                                    .split(" in ")[-1]
                                    .replace("?", "")
                                    .strip()
                                    .title()
                                )

                            terminal_ui.markdown(
                                f"<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'>[TRACE INIT]<br>> THOUGHT: Live data required.<br>> <span class='log-action'>ACTION: live_web_scraper()</span><br>> TARGET: '{location}'</div></div>",
                                unsafe_allow_html=True
                            )
                            with st.spinner(f"Scraping live internet for {location}..."):
                                try:
                                    safe_loc = urllib.parse.quote(location)
                                    url = f"https://wttr.in/{safe_loc}?format=%C,+%t"
                                    req = urllib.request.Request(
                                        url,
                                        headers={'User-Agent': 'curl'}
                                    )
                                    response = urllib.request.urlopen(req, timeout=4)
                                    live_data = response.read().decode('utf-8').strip()

                                    terminal_ui.markdown(
                                        f"<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'>[TRACE INIT]<br>> THOUGHT: Live data required.<br>> <span class='log-action'>ACTION: live_web_scraper()</span><br>> TARGET: '{location}'<br><span class='log-success'>> OBSERVATION: 200 OK ({live_data})</span><br>> FINAL_ANSWER GENERATED.</div></div>",
                                        unsafe_allow_html=True
                                    )
                                    final_text = f"Live internet scrape successful. Weather in **{location}** is {live_data}."
                                    st.write(final_text)
                                    st.session_state.chat_log.append(
                                        {"role": "assistant", "content": final_text}
                                    )
                                except Exception:
                                    terminal_ui.markdown(
                                        f"<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'><span class='log-error'>[NETWORK TIMEOUT]</span><br>> THOUGHT: Live data required.<br>> <span class='log-action'>ACTION: live_web_scraper()</span><br><span class='log-error'>> EXCEPTION: Request Failed.</span></div></div>",
                                        unsafe_allow_html=True
                                    )
                                    final_text = "❌ **Error:** Web request timed out."
                                    st.error(final_text)
                                    st.session_state.chat_log.append(
                                        {"role": "assistant", "content": final_text}
                                    )
                    else:
                        terminal_ui.markdown(
                            "<div class='mac-window'><div class='mac-header'><div class='mac-dot dot-red'></div><div class='mac-dot dot-yel'></div><div class='mac-dot dot-grn'></div></div><div class='terminal-body'>[TRACE LOG]<br>> THOUGHT: General chat.<br>> ACTION: None.<br>> FINAL_ANSWER GENERATED.</div></div>",
                            unsafe_allow_html=True
                        )
                        final_text = "I am a ReAct AI Agent. Ask me to calculate numbers or check live weather!"
                        st.write(final_text)
                        st.session_state.chat_log.append(
                            {"role": "assistant", "content": final_text}
                        )

    # NAVIGATION
    st.markdown(
        "<div class='nav-spacer fade-in delay-3'></div>",
        unsafe_allow_html=True
    )
    col_prev, _, col_next = st.columns([1, 4, 1])
    with col_prev:
        st.button(
            "⬅️ Back",
            type="secondary",
            use_container_width=True,
            on_click=set_phase,
            args=(1,)
        )
    with col_next:
        st.button(
            "Phase 3 ➡️",
            type="primary",
            use_container_width=True,
            on_click=set_phase,
            args=(3,)
        )


# ==========================================
# PHASE 3: PROGRESSIVE GAMIFIED EXAM
# ==========================================

elif st.session_state.current_phase == 3:
    st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
    st.header("Phase 3: Certification Exam")
    st.write(
        "Answer the questions below. The system evaluates your logic step-by-step."
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # QUESTION 1
    if st.session_state.quiz_step == 1:
        st.markdown(
            "<div class='concept-card fade-in delay-1'><h3>Question 1: The Core Loop</h3><p style='color:#526071;'>What is the strict execution order required to prevent infinite loops in an AI Agent?</p></div>",
            unsafe_allow_html=True
        )
        st.markdown("<div class='fade-in delay-2'>", unsafe_allow_html=True)
        q1 = st.radio(
            "q1",
            [
                "Act ➡️ Reason ➡️ Guess",
                "Thought ➡️ Action ➡️ Observation ➡️ Final Answer",
                "JSON ➡️ Python ➡️ Crash"
            ],
            index=None,
            key="q1",
            label_visibility="collapsed"
        )
        if st.button("Lock Answer & Proceed", type="primary"):
            if q1:
                with st.spinner("Analyzing logic..."):
                    time.sleep(0.8)
                    advance_quiz(
                        q1 == "Thought ➡️ Action ➡️ Observation ➡️ Final Answer"
                    )
                    st.rerun()
            else:
                st.warning("Please select an answer.")
        st.markdown("</div>", unsafe_allow_html=True)

    # QUESTION 2
    elif st.session_state.quiz_step == 2:
        st.markdown(
            "<div class='concept-card fade-in'><h3>Question 2: Secure Communication</h3><p style='color:#526071;'>How does Generative AI (text) trigger a specific Python backend function securely?</p></div>",
            unsafe_allow_html=True
        )
        st.markdown("<div class='fade-in delay-1'>", unsafe_allow_html=True)
        q2 = st.radio(
            "q2",
            [
                "By outputting a structured JSON payload that Python parses.",
                "By directly running Python code inside the chat window.",
                "By guessing the answer internally."
            ],
            index=None,
            key="q2",
            label_visibility="collapsed"
        )
        if st.button("Lock Answer & Proceed", type="primary"):
            if q2:
                with st.spinner("Analyzing logic..."):
                    time.sleep(0.8)
                    advance_quiz(
                        q2 == "By outputting a structured JSON payload that Python parses."
                    )
                    st.rerun()
            else:
                st.warning("Please select an answer.")
        st.markdown("</div>", unsafe_allow_html=True)

    # QUESTION 3
    elif st.session_state.quiz_step == 3:
        st.markdown(
            "<div class='concept-card fade-in'><h3>Question 3: Practical Debugging & Guardrails</h3><p style='color:#526071;'>In the Sandbox, what happens if the AI attempts to use a disabled tool?</p></div>",
            unsafe_allow_html=True
        )
        st.markdown("<div class='fade-in delay-1'>", unsafe_allow_html=True)
        q3 = st.radio(
            "q3",
            [
                "The AI rewrites its own code to bypass the lock.",
                "The system catches the JSON request, realizes the tool is offline, and returns an error.",
                "The AI hallucinates fake data to satisfy the user."
            ],
            index=None,
            key="q3",
            label_visibility="collapsed"
        )
        if st.button("Lock Final Answer & Submit", type="primary"):
            if q3:
                with st.spinner("Compiling Final Score..."):
                    time.sleep(1.5)
                    advance_quiz(
                        q3 == "The system catches the JSON request, realizes the tool is offline, and returns an error."
                    )
                    st.rerun()
            else:
                st.warning("Please select an answer.")
        st.markdown("</div>", unsafe_allow_html=True)

    # FINAL RESULTS
    elif st.session_state.quiz_step == 4:
        score = st.session_state.quiz_score
        st.markdown("<div class='fade-in'>", unsafe_allow_html=True)
        if score == 3:
            st.balloons()
            st.markdown("""
            <div style='background:#FFFFFF; padding:50px; border-radius:20px; text-align:center; box-shadow:0 12px 30px rgba(31,41,55,0.08); border:1px solid #DCE8E2;'>
                <h1 style='margin:0; font-size:2.5rem; text-transform:uppercase; color:#287C78;'>🏆 CERTIFIED AI ARCHITECT</h1>
                <p style='font-size:1.1rem; margin-top:20px; color:#526071;'>Passed with a Perfect Score (3/3). You have demonstrated mastery of Tool Binding, JSON Routing, and ReAct Execution Loops.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(f"⚠️ **Final Score: {score}/3.**")
            st.write(
                "In enterprise engineering, perfection is required. Please review Phase 1 and try again."
            )
            if st.button("🔄 Retake Exam", type="secondary"):
                st.session_state.quiz_step = 1
                st.session_state.quiz_score = 0
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # NAVIGATION
    st.markdown(
        "<div class='nav-spacer fade-in delay-2'></div>",
        unsafe_allow_html=True
    )
    if st.session_state.quiz_step < 4:
        col_prev, _ = st.columns([1, 5])
        with col_prev:
            st.button(
                "⬅️ Back",
                type="secondary",
                use_container_width=True,
                on_click=set_phase,
                args=(2,)
            )
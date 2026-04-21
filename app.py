import streamlit as st

# ── Page Config ────────────────────────────────────────
st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

# ── Load CSS ───────────────────────────────────────────
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

# ── Session State ──────────────────────────────────────
if "expr" not in st.session_state:
    st.session_state.expr = ""
if "history" not in st.session_state:
    st.session_state.history = ""

# ── Helper Functions ───────────────────────────────────
def press(val):
    st.session_state.expr += str(val)

def clear_all():
    st.session_state.expr = ""
    st.session_state.history = ""

def backspace():
    st.session_state.expr = st.session_state.expr[:-1]

def calculate():
    try:
        expr = st.session_state.expr.replace("×", "*").replace("÷", "/")
        result = eval(expr)
        st.session_state.history = st.session_state.expr + " ="
        if isinstance(result, float) and result.is_integer():
            st.session_state.expr = str(int(result))
        else:
            st.session_state.expr = str(round(result, 8))
    except:
        st.session_state.history = st.session_state.expr
        st.session_state.expr = "Error ❌"

# ── Title ──────────────────────────────────────────────
st.markdown('<div class="title-text">🧮 CALCULATOR</div>', unsafe_allow_html=True)

# ── History ────────────────────────────────────────────
st.markdown(f'<div class="history-box">{st.session_state.history}</div>', unsafe_allow_html=True)

# ── Display Screen ─────────────────────────────────────
display_val = st.session_state.expr if st.session_state.expr else "0"
st.markdown(f'<div class="display-box">{display_val}</div>', unsafe_allow_html=True)

st.markdown("")

# ── Row 1: C  ⌫  %  ÷ ─────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C", key="c", use_container_width=True):
        clear_all(); st.rerun()
with col2:
    if st.button("⌫", key="bk", use_container_width=True):
        backspace(); st.rerun()
with col3:
    if st.button("%", key="pct", use_container_width=True):
        press("%"); st.rerun()
with col4:
    if st.button("÷", key="div", use_container_width=True):
        press("/"); st.rerun()

# ── Row 2: 7  8  9  × ─────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7", key="7", use_container_width=True):
        press("7"); st.rerun()
with col2:
    if st.button("8", key="8", use_container_width=True):
        press("8"); st.rerun()
with col3:
    if st.button("9", key="9", use_container_width=True):
        press("9"); st.rerun()
with col4:
    if st.button("×", key="mul", use_container_width=True):
        press("*"); st.rerun()

# ── Row 3: 4  5  6  − ─────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4", key="4", use_container_width=True):
        press("4"); st.rerun()
with col2:
    if st.button("5", key="5", use_container_width=True):
        press("5"); st.rerun()
with col3:
    if st.button("6", key="6", use_container_width=True):
        press("6"); st.rerun()
with col4:
    if st.button("−", key="sub", use_container_width=True):
        press("-"); st.rerun()

# ── Row 4: 1  2  3  + ─────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1", key="1", use_container_width=True):
        press("1"); st.rerun()
with col2:
    if st.button("2", key="2", use_container_width=True):
        press("2"); st.rerun()
with col3:
    if st.button("3", key="3", use_container_width=True):
        press("3"); st.rerun()
with col4:
    if st.button("+", key="add", use_container_width=True):
        press("+"); st.rerun()

# ── Row 5: 00  0  .  = ────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("00", key="00", use_container_width=True):
        press("00"); st.rerun()
with col2:
    if st.button("0", key="0", use_container_width=True):
        press("0"); st.rerun()
with col3:
    if st.button(".", key="dot", use_container_width=True):
        press("."); st.rerun()
with col4:
    if st.button("=", key="eq", type="primary", use_container_width=True):
        calculate(); st.rerun()

# ── Footer ─────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="footer-text">STREAMLIT CALCULATOR v2.0</p>', unsafe_allow_html=True)



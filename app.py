import streamlit as st
import math

# ---------------------- APP CONFIGURATION ----------------------
st.set_page_config(page_title="Advanced Scientific Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Advanced Scientific Calculator")
st.markdown("Perform **basic arithmetic** and **advanced scientific** calculations easily.")

# ---------------------- INPUT SECTION ----------------------
st.markdown("### Enter or Build Your Expression")
expression = st.text_input("Expression", value="", key="expression")

# ---------------------- BUTTON LAYOUT ----------------------

# --- Basic Number Buttons ---
st.markdown("### Basic Operations")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7"): expression += "7"
    if st.button("4"): expression += "4"
    if st.button("1"): expression += "1"
    if st.button("0"): expression += "0"
with col2:
    if st.button("8"): expression += "8"
    if st.button("5"): expression += "5"
    if st.button("2"): expression += "2"
    if st.button("."): expression += "."
with col3:
    if st.button("9"): expression += "9"
    if st.button("6"): expression += "6"
    if st.button("3"): expression += "3"
    if st.button("%"): expression += "%"
with col4:
    if st.button("+"): expression += "+"
    if st.button("-"): expression += "-"
    if st.button("×"): expression += "*"
    if st.button("÷"): expression += "/"

# --- Scientific Functions ---
st.markdown("### Scientific Functions")
sci1, sci2, sci3, sci4, sci5 = st.columns(5)

with sci1:
    if st.button("sin"): expression += "math.sin("
    if st.button("cos"): expression += "math.cos("
    if st.button("tan"): expression += "math.tan("
    if st.button("π"): expression += "math.pi"
    if st.button("e"): expression += "math.e"

with sci2:
    if st.button("log"): expression += "math.log("
    if st.button("√"): expression += "math.sqrt("
    if st.button("^"): expression += "**"
    if st.button("!"): expression += "math.factorial("
    if st.button("abs"): expression += "abs("

with sci3:
    if st.button("exp"): expression += "math.exp("
    if st.button("round"): expression += "round("
    if st.button("("): expression += "("
    if st.button(")"): expression += ")"
    if st.button("pow"): expression += "pow("

with sci4:
    if st.button("deg→rad"): expression += "math.radians("
    if st.button("rad→deg"): expression += "math.degrees("
    if st.button("floor"): expression += "math.floor("
    if st.button("ceil"): expression += "math.ceil("
    if st.button("mod"): expression += "%"

with sci5:
    if st.button("x²"): expression += "**2"
    if st.button("x³"): expression += "**3"
    if st.button("C"): expression = ""
    if st.button("⌫"): expression = expression[:-1]
    if st.button("ANS"):
        if "result" in st.session_state:
            expression += str(st.session_state["result"])

# ---------------------- DISPLAY CURRENT EXPRESSION ----------------------
st.text_area("Current Expression:", value=expression, height=80)

# ---------------------- CALCULATE BUTTON ----------------------
if st.button("Calculate"):
    try:
        result = eval(expression)
        st.session_state["result"] = result
        st.success(f"✅ Result: {result}")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------------------- FOOTER ----------------------
st.markdown("---")
st.caption("Developed by Maria 💻 | Powered by Streamlit & Python 🧠")


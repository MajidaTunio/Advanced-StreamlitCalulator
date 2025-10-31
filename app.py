import streamlit as st
import math

# --- App Configuration ---
st.set_page_config(page_title="Advanced Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Advanced Scientific Calculator")
st.markdown("A modern Streamlit-based calculator with scientific and trigonometric functions.")

# --- Input Section ---
expression = st.text_input("Enter your mathematical expression:", "")

# --- Scientific Buttons ---
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("sin"):
        expression += "math.sin("
    if st.button("cos"):
        expression += "math.cos("
    if st.button("tan"):
        expression += "math.tan("
    if st.button("log"):
        expression += "math.log("
    if st.button("√"):
        expression += "math.sqrt("

with col2:
    if st.button("π"):
        expression += "math.pi"
    if st.button("e"):
        expression += "math.e"
    if st.button("exp"):
        expression += "math.exp("
    if st.button("abs"):
        expression += "abs("
    if st.button("! (factorial)"):
        expression += "math.factorial("

with col3:
    if st.button("^"):
        expression += "**"
    if st.button("("):
        expression += "("
    if st.button(")"):
        expression += ")"
    if st.button("mod"):
        expression += "%"
    if st.button("round"):
        expression += "round("

with col4:
    if st.button("deg→rad"):
        expression += "math.radians("
    if st.button("rad→deg"):
        expression += "math.degrees("
    if st.button("floor"):
        expression += "math.floor("
    if st.button("ceil"):
        expression += "math.ceil("
    if st.button("pow"):
        expression += "pow("

with col5:
    if st.button("C"):
        expression = ""
    if st.button("⌫"):
        expression = expression[:-1]
    if st.button("x²"):
        expression += "**2"
    if st.button("x³"):
        expression += "**3"
    if st.button("/"):
        expression += "/"

# --- Display Current Expression ---
st.text_area("Current Expression:", value=expression, height=100)

# --- Evaluation Section ---
if st.button("Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.markdown("---")
st.caption("Developed by Maria 💻 | Powered by Streamlit & Python 🧠")

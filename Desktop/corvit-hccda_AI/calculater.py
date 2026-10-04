import streamlit as st
import math

# Page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Scientific Calculator")

# Initialize session state for expression if not already set
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Helper function to append text from button clicks
def append_to_expression(value):
    st.session_state.expression += str(value)

def clear_expression():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

# Safe Evaluation Function
def calculate_result(expr):
    if not expr.strip():
        return ""
    
    # Define safe mathematical context for evaluation
    allowed_names = {
        "sin": lambda x: math.sin(math.radians(x)),  # Deg input support
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "asin": lambda x: math.degrees(math.asin(x)),
        "acos": lambda x: math.degrees(math.acos(x)),
        "atan": lambda x: math.degrees(math.atan(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi,
        "e": math.e,
        "abs": abs,
        "pow": pow,
        "radians": math.radians,
        "degrees": math.degrees
    }

    # Replace display symbols with Python syntax
    clean_expr = (
        expr.replace("^", "**")
            .replace("÷", "/")
            .replace("×", "*")
            .replace("π", "pi")
    )

    try:
        # Evaluate safely within limited globals scope
        result = eval(clean_expr, {"__builtins__": None}, allowed_names)
        # Format floating-point results neatly
        if isinstance(result, float):
            result = round(result, 8)
            if result.is_integer():
                result = int(result)
        return str(result)
    except Exception as e:
        return "Error"

def evaluate():
    st.session_state.expression = calculate_result(st.session_state.expression)

# -------------------------------------------------------------
# Input Display (Supports Typing / Keyboard Input Directly)
# -------------------------------------------------------------
st.text_input(
    "Type an expression or press buttons (Press Enter to evaluate):",
    key="expression",
    on_change=evaluate,
    placeholder="e.g. sin(30) + sqrt(16) * 5"
)

# -------------------------------------------------------------
# Calculator Button Layout (Mouse Click Events)
# -------------------------------------------------------------

# Row 1: Scientific Functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("sin", use_container_width=True, on_click=append_to_expression, args=("sin(",))
with col2:
    st.button("cos", use_container_width=True, on_click=append_to_expression, args=("cos(",))
with col3:
    st.button("tan", use_container_width=True, on_click=append_to_expression, args=("tan(",))
with col4:
    st.button("log", use_container_width=True, on_click=append_to_expression, args=("log(",))
with col5:
    st.button("ln", use_container_width=True, on_click=append_to_expression, args=("ln(",))

# Row 2: Constants & Scientific Operators
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("√ (sqrt)", use_container_width=True, on_click=append_to_expression, args=("sqrt(",))
with col2:
    st.button("^ (pow)", use_container_width=True, on_click=append_to_expression, args=("^",))
with col3:
    st.button("π", use_container_width=True, on_click=append_to_expression, args=("π",))
with col4:
    st.button("e", use_container_width=True, on_click=append_to_expression, args=("e",))
with col5:
    st.button("(", use_container_width=True, on_click=append_to_expression, args=("(",))

# Row 3: Standard Numbers & Controls
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("7", use_container_width=True, on_click=append_to_expression, args=("7",))
with col2:
    st.button("8", use_container_width=True, on_click=append_to_expression, args=("8",))
with col3:
    st.button("9", use_container_width=True, on_click=append_to_expression, args=("9",))
with col4:
    st.button("÷", use_container_width=True, on_click=append_to_expression, args=("÷",))
with col5:
    st.button(")", use_container_width=True, on_click=append_to_expression, args=(")",))

# Row 4: Standard Numbers & Controls
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("4", use_container_width=True, on_click=append_to_expression, args=("4",))
with col2:
    st.button("5", use_container_width=True, on_click=append_to_expression, args=("5",))
with col3:
    st.button("6", use_container_width=True, on_click=append_to_expression, args=("6",))
with col4:
    st.button("×", use_container_width=True, on_click=append_to_expression, args=("×",))
with col5:
    st.button("⌫ Del", use_container_width=True, on_click=backspace)

# Row 5: Numbers & Basic Operators
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("1", use_container_width=True, on_click=append_to_expression, args=("1",))
with col2:
    st.button("2", use_container_width=True, on_click=append_to_expression, args=("2",))
with col3:
    st.button("3", use_container_width=True, on_click=append_to_expression, args=("3",))
with col4:
    st.button("-", use_container_width=True, on_click=append_to_expression, args=("-",))
with col5:
    st.button("C (Clear)", use_container_width=True, on_click=clear_expression)

# Row 6: Zero, Decimal, Addition & Equal
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("0", use_container_width=True, on_click=append_to_expression, args=("0",))
with col2:
    st.button(".", use_container_width=True, on_click=append_to_expression, args=(".",))
with col3:
    st.button("00", use_container_width=True, on_click=append_to_expression, args=("00",))
with col4:
    st.button("+", use_container_width=True, on_click=append_to_expression, args=("+",))
with col5:
    st.button("=", type="primary", use_container_width=True, on_click=evaluate)

# Usage Instructions
st.markdown("---")
st.caption("""
**How to use:**
- **Mouse Event:** Click any button on the screen to append values and click `=` to solve.
- **Keyboard Event:** Click on the input field above to type any formula (e.g., `sin(45) + sqrt(16)` or `2^3`) and hit **Enter**.
""")
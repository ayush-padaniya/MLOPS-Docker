import streamlit as st


def calculate(a: float, b: float, op: str) -> float:
    """Perform a basic arithmetic operation."""
    if op == "Add":
        return a + b
    if op == "Subtract":
        return a - b
    if op == "Multiply":
        return a * b
    if op == "Divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError(f"Unsupported operation: {op}")


def main() -> None:
    st.set_page_config(page_title="Streamlit Calculator", page_icon="🧮")
    st.title("🧮 Streamlit Calculator")
    st.write("Enter two numbers, choose an operation, and hit **Calculate**.")

    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("First number", value=0.0, format="%.6f")
    with col2:
        num2 = st.number_input("Second number", value=0.0, format="%.6f")

    operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])

    if st.button("Calculate", type="primary"):
        try:
            result = calculate(num1, num2, operation)
        except ZeroDivisionError as exc:
            st.error(str(exc))
        except Exception as exc:  # pragma: no cover - defensive
            st.error(f"Something went wrong: {exc}")
        else:
            st.success(f"Result: {result}")


if __name__ == "__main__":
    main()

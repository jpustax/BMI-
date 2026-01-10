import streamlit as st

# ======================
# Page Config
# ======================
st.set_page_config(
    page_title="BMI 계산기",
    layout="centered"
)

# ======================
# Title
# ======================
st.title("체질량지수(BMI) 계산기")
st.write("키와 체중을 입력하시면 BMI를 계산해드립니다.")

# ======================
# Input Section
# ======================
with st.expander("신체 정보 입력", expanded=True):

    height_cm = st.number_input(
        "키 (cm)",
        min_value=100.0,
        max_value=250.0,
        value=170.0,
        step=0.1
    )

    weight_kg = st.number_input(
        "체중 (kg)",
        min_value=30.0,
        max_value=200.0,
        value=65.0,
        step=0.1
    )

# ======================
# Calculate Button
# ======================
if st.button("BMI 계산하기"):

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        result = "저체중"
        msg = "체중이 부족한 상태입니다."
    elif bmi < 25:
        result = "정상"
        msg = "건강한 체중 범위입니다."
    elif bmi < 30:
        result = "과체중"
        msg = "체중 관리가 필요합니다."
    else:
        result = "비만"
        msg = "의학적 관리가 권장됩니다."

    # ======================
    # Output Section
    # ======================
    with st.expander("BMI 계산 결과", expanded=True):

        st.metric("BMI 수치", f"{bmi:.2f}")
        st.write(f"판정: {result}")
        st.info(msg)

import streamlit as st

# Tiêu đề
st.title("Ứng dụng tính tiền gửi tiết kiệm")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng gửi",
    min_value=1,
    value=12
)

# Tính toán
if st.button("Tính toán"):

    lai_suat = i / 100

    An = C * (1 + lai_suat * n / 12)

    st.success(
        f"Tổng số tiền nhận được: {An:,.2f} triệu đồng"
    )

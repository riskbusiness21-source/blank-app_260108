import streamlit as st

# 초등학교 곱셈 학습 앱
# 1) 사용자가 두 숫자를 입력 (행 x 열 또는 피연산자 두 개)
# 2) 사용자가 선택한 그림(이모지)으로 곱셈 결과를 시각화
# 3) 시각화가 완료되면 정답을 입력하는 칸을 보여주고 정답 여부를 판단

st.set_page_config(page_title="초등 곱셈 학습 앱", layout="centered")

st.title("🧮 초등 곱셈 학습 앱")
st.write("아래에서 두 숫자를 입력하고 그림을 선택한 뒤 '시각화' 버튼을 눌러보세요.")

# --- 입력 영역 ---
# 두 수는 0~12 범위로 제한 (초등 수준)
col_a, col_b = st.columns(2)
with col_a:
    a = st.number_input("첫 번째 수 (행)", min_value=0, max_value=12, value=3, step=1)
with col_b:
    b = st.number_input("두 번째 수 (열)", min_value=0, max_value=12, value=4, step=1)

# 사용자가 선택할 수 있는 그림 목록 (이모지 사용, 이미지 URL 대신 이모지를 사용하면 별도 파일 불필요)
emoji_options = {
    "사과 🍎": "🍎",
    "별 ⭐": "⭐",
    "강아지 🐶": "🐶",
    "쿠키 🍪": "🍪"
}
choice_label = st.selectbox("시각화에 사용할 그림을 선택하세요", list(emoji_options.keys()))
emoji = emoji_options[choice_label]

# 시각화 버튼: 눌러야 시각화와 정답 입력란이 등장하도록 함
if "visualized" not in st.session_state:
    st.session_state.visualized = False

if st.button("시각화"):
    # 시각화 버튼을 누르면 상태를 True로 설정하고 화면에 그림을 그리도록 함
    st.session_state.visualized = True
    st.session_state.last_a = int(a)
    st.session_state.last_b = int(b)
    st.session_state.emoji = emoji

# '다시하기' 버튼: 세션 상태 초기화
if st.session_state.get("visualized", False):
    if st.button("다시하기"):
        st.session_state.visualized = False

# --- 시각화 영역 ---
if st.session_state.get("visualized", False):
    rows = st.session_state.last_a
    cols = st.session_state.last_b
    symbol = st.session_state.emoji

    st.markdown(f"### {rows} x {cols} = ? (그림으로 확인해보세요)")

    # 행(row) 단위로 컬럼을 생성해 그림을 배치
    # 주의: 너무 큰 수일 경우(예: 12x12) 컬럼 생성으로 레이아웃이 복잡해질 수 있음
    for i in range(rows):
        row_cols = st.columns(cols if cols>0 else 1)
        for j, rc in enumerate(row_cols):
            # 각 칸에 이모지를 크게 표시 (HTML 사용)
            rc.markdown(f"<div style='font-size:36px; text-align:center;'>{symbol}</div>", unsafe_allow_html=True)

    # 곱셈 결과를 사용자가 입력하도록 함
    st.write("")
    st.markdown("**이제 아래에 곱셈 결과(정답)를 입력하고 제출하세요.**")
    answer = st.number_input("곱셈 결과를 입력하세요", min_value=0, max_value=144, step=1, key="answer_input")
    if st.button("제출"):
        correct = rows * cols
        if answer == correct:
            st.success(f"정답입니다! {rows} x {cols} = {correct}")
        else:
            st.error(f"틀렸습니다. 다시 확인해보세요. (입력: {answer})")

else:
    st.info("시각화 버튼을 눌러 선택한 그림으로 결과를 확인하세요.")

# 학습 보조: 정답을 바로 확인하고 싶을 때 보여주는 토글 (교사용 힌트)
with st.expander("교사용 힌트(정답 보기)"):
    st.write("정답을 바로 확인하려면 아래 버튼을 누르세요.")
    if st.button("정답 보기 (교사용)"):
        st.warning("정답을 표시합니다: ")
        st.write(f"{a} × {b} = {int(a)*int(b)}")



import streamlit as st
import pandas as pd
import numpy as np
import datetime

# 한 페이지에 Streamlit 주요 요소들을 모아 보여주는 데모 앱
# 각 블록 위에 한국어 주석(각주)을 달아, 공부할 수 있도록 구성했습니다.

st.set_page_config(page_title="Streamlit 요소 데모", layout="wide")

st.title("📚 Streamlit 한 페이지 요소 모음")

# 간단한 텍스트 요소
st.header("텍스트 요소")
st.subheader("기본 텍스트와 마크다운")
st.write("`st.write()`는 거의 모든 타입을 렌더링합니다 — 문자열, 숫자, 데이터프레임 등.")
st.markdown("**Markdown**을 사용해 더 풍부한 텍스트를 표시할 수 있습니다.")
st.caption("이것은 캡션 텍스트입니다. 도움말이나 출처 표시에 유용합니다.")

# 코드, 라텍스
st.subheader("코드와 수식")
code_example = """def hello(name):\n    return f'Hello {name}'"""
st.code(code_example, language="python")  # 코드 블록 표시
st.latex(r"E = mc^2")  # 수식 표시 (KaTeX 사용)

# 미디어
st.header("미디어")
st.image("https://static.streamlit.io/examples/dog.jpg", caption="예시 이미지")
st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/BabyElephantWalk60.wav")

# 입력 위젯
st.header("입력 위젯")
with st.expander("입력 위젯 모음 (펼치기)"):
    # 체크박스: 단순한 on/off
    cb = st.checkbox("동의합니다")
    # 라디오 버튼: 단일 선택
    choice = st.radio("옵션 선택:", ("옵션 A", "옵션 B", "옵션 C"))
    # 셀렉트박스: 드롭다운 단일 선택
    sel = st.selectbox("과일 선택", ["사과", "바나나", "체리"])
    # 멀티셀렉트: 다중 선택
    multi = st.multiselect("여러 항목 선택", ["파이썬", "자바스크립트", "Go", "Rust"], default=["파이썬"]) 
    # 슬라이더: 범위 또는 단일 값
    val = st.slider("값 선택", 0, 100, 25)
    # 숫자 입력
    n = st.number_input("숫자 입력", min_value=0, max_value=1000, value=10)
    # 텍스트 입력 / 텍스트 영역
    txt = st.text_input("한 줄 텍스트", "안녕하세요")
    ta = st.text_area("여러 줄 텍스트", "여기에 메모를 입력하세요.")
    # 날짜/시간 입력
    d = st.date_input("날짜 선택", datetime.date.today())
    t = st.time_input("시간 선택", datetime.time(12, 30))
    # 색상 선택
    c = st.color_picker("색 선택", "#00f900")
    # 파일 업로더
    fu = st.file_uploader("파일 업로드", type=["png", "jpg", "csv", "txt"]) 

# 버튼과 액션
st.header("버튼과 상호작용")
if st.button("클릭하세요"):
    st.success("버튼이 클릭되었습니다!")

if st.button("임시 로딩 시연"):
    with st.spinner("처리중..."):
        import time
        time.sleep(1)
    st.info("처리 완료")

# 데이터 표시
st.header("데이터 표시")
df = pd.DataFrame(np.random.randn(10, 3), columns=["a", "b", "c"])  # 예시 데이터
st.dataframe(df)  # 상호작용 가능한 데이터프레임
st.table(df.head())  # 정적 테이블
st.json({"name": "streamlit", "type": "demo"})  # JSON 표시

# 차트 예제
st.header("차트와 지도")
st.line_chart(df)  # 간단한 라인 차트
st.area_chart(df)  # 에어리어 차트
st.bar_chart(df.abs())  # 바 차트

# 지도: 위도/경도 데이터가 필요
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)

# 고급 위젯 및 배치
st.header("레이아웃: 칼럼과 익스팬더")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("온도", "23°C", "+1.2°C")  # KPI 형태의 메트릭
with col2:
    st.selectbox("도시", ["Seoul", "Busan", "Daegu"])  # 컬럼 내 위젯
with col3:
    st.button("열 버튼")

with st.expander("추가 설명 (펼쳐보기)"):
    st.write("이 패널에 더 많은 설명이나 문서 링크를 넣을 수 있습니다.")

# 다운로드 버튼: 문자열/바이트/파일 다운로드 제공
st.header("다운로드")
st.download_button("텍스트 다운로드", data="Hello Streamlit", file_name="hello.txt")

# 상태/알림
st.header("상태 표시")
st.success("성공 메시지 예시")
st.info("정보 메시지 예시")
st.warning("경고 메시지 예시")
st.error("에러 메시지 예시")

# 사이드바 예시: 페이지와 분리된 입력 영역
st.sidebar.header("사이드바")
st.sidebar.write("사이드바에는 설정이나 필터를 두는 것이 일반적입니다.")
sb = st.sidebar.slider("사이드바 슬라이더", 0, 10, 3)

# 팁: 코드 학습용 주석
# 각 함수의 문법과 인자, 반환형은 공식 문서를 참고하세요: https://docs.streamlit.io/

st.write("---")
st.caption("예제 페이지 끝 — 위젯을 직접 클릭/조작해 보세요.")

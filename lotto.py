import random
import streamlit as st

st.title("🎱 로또 번호 생성기")

if "number_sets" not in st.session_state:
    st.session_state.number_sets = []

if st.button("로또번호 생성"):
    if len(st.session_state.number_sets) < 5:
        numbers = sorted(random.sample(range(1, 46), 6))
        st.session_state.number_sets.append(numbers)
    else:
        st.warning("최대 5세트까지 만들 수 있어요. 초기화해 주세요.")

if st.button("초기화"):
    st.session_state.number_sets = []

for index, numbers in enumerate(st.session_state.number_sets, start=1):
    st.write(f"{index}세트: {'  ·  '.join(map(str, numbers))}")
import streamlit as st
from leetcoder.main import Run
from code_editor import code_editor
import time

def stream_data(des):
    for word in des.split(" "):
        yield word + " "
        time.sleep(0.05)
st. set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: red; text-shadow: 2px 20px 20px maroon; font-size: 60px;'>Leet<span style='color: lightgreen'>CODER</span></h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: lavender;'>Enter Problem Number</h3>", unsafe_allow_html=True)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] > .main {
    background: linear-gradient(90deg, #0b1142, black, #5d1111);
    background-size: 400% 400%;
    animation: gradient 8s ease infinite;
    height: 100vh;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
col1, col2 = st.columns(2)
r = Run()

buff, col, buff2 = st.columns([3,1,3.1])
q = col.number_input('dummy',min_value = 1, max_value = 3000, step = 1, help = 'enter the problem number', label_visibility='hidden', value=None)

if q:
    with st.spinner('Just wait for it 😏'):
        code, explanation = r.run(q)
    st.balloons()
    with col1:
        if not r.prm:
            code_editor(code.raw, lang='python')
        else:
            code_editor(code)
    with col2:
        if not r.prm:
            st.write_stream(stream_data(explanation.raw))
        else:
            st.write_stream(stream_data(explanation))
else:
    pass

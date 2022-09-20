import streamlit as st
from senpy.sqt.parser import read_file

st.title("Protein Inference")

input_sqt_files = st.file_uploader("SQT File", type=['.sqt'], accept_multiple_files=True)

if st.button("Run"):

    if input_sqt_files is None:
        st.warning('Upload SQT file')
        st.stop()

    s_lines = []
    for input_sqt_file in input_sqt_files:
        _, lines = read_file(input_sqt_file.readlines())
        s_lines.extend(lines)

    for line in s_lines:
        line.
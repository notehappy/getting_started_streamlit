import streamlit as st
import pandas as pd

with st.echo():
    st.title('Getting Started Stramlit')
    st.write('This is introduction of streamlit')

    st.markdown('## Code ')
    code = '''
    def hello():
        print('Hello , Stramlit!)'''

    show_btn = st.button('show code!')
    if show_btn:
        st.code(code, language='Python')

    cols = st.columns(2)
    with cols[0]:
        age_inp = st.number_input('Input your age')
        st.markdown(f'Your age is {age_inp}')


    with cols[1]:
        text_inp = st.text_input('Input your text')
        word_tokenize = '|'.join(text_inp.split())
        st.markdown(f'{word_tokenize}')

    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
    st.dataframe(df)
    show_chart_btn = st.button('Show Chart!!')
    if show_chart_btn:
        st.line_chart(df)
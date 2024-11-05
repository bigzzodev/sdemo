import streamlit as st
import numpy as np
import pandas as pd
import json
# from streamlit_echarts import st_echarts
from analytics import ST_ANALYTICS

# ------------------------------------------------------------------------------------------------------------------------
def main():
    # st.title("뉴스기사 분석")
    # st.header("뉴스기사 분석")
    # st.subheader("뉴스기사 분석")
    # st.write('뉴스기사 **분석** 내용')

    with st.sidebar:
        st.subheader("뉴스기사 분석 시스템")
        # 가수별
        singer_opt = list(ST_ANALYTICS.keys())
        selected_singer = st.selectbox(label="회사를 선택하세요", options=singer_opt,)
        func, year_opt = ST_ANALYTICS[selected_singer]
        # selected_year = st.selectbox(label="확인할 년도를 선택하세요", options=year_opt,)
        # st.write("You selected:", selected_year)

    # func(selected_singer, selected_year)
    func(selected_singer)
# ------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # page_icon=":chart_with_upwards_trend:
    st.set_page_config(page_icon = ':sparkles:', page_title = 'sdemo', layout = 'wide',)



    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        #GithubIcon {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)



    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    main()

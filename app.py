import streamlit as st
from analytics import ST_ANALYTICS

# ------------------------------------------------------------------------------------------------------------------------
def main():
    with st.sidebar:
        st.subheader("뉴스기사 분석 시스템")
        singer_opt = list(ST_ANALYTICS.keys())
        selected_company = st.selectbox(label="회사를 선택하세요", options=singer_opt,)
        func, year_opt = ST_ANALYTICS[selected_company]
    func(selected_company)

# ------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # page_icon=":chart_with_upwards_trend:
    st.set_page_config(page_icon = ':sparkles:', page_title = 'sdemo', layout = 'wide',)

    # hide_streamlit_style = """
    #     <style>
    #     #MainMenu {visibility: hidden;}
    #     #GithubIcon {visibility: hidden;}
    #     footer {visibility: hidden;}
    #     </style>
    #     """
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    # st.markdown(
    #     """
    #     <style>
    #     .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    #     .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    #     .viewerBadge_text__1JaDK {
    #         display: none;
    #     }
    #     </style>
    #     """,
    #     unsafe_allow_html=True
    # )

    hide_streamlit_style = """
                <style>
                [data-testid="stToolbar"] {visibility: hidden !important;}
                footer {visibility: hidden !important;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    #----------------------Hide Streamlit footer----------------------------
    hide_st_style = """

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    #--------------------------------------------------------------------



    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    main()

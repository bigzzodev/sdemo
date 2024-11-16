import streamlit as st
from analytics import ST_ANALYTICS

# ------------------------------------------------------------------------------------------------------------------------
def main1():
    with st.sidebar:
        st.subheader("뉴스 기사 :blue[통계 분석]")
        singer_opt = list(ST_ANALYTICS.keys())
        selected_company = st.selectbox(label="분석할 회사를 선택하세요", options=singer_opt, key="main_button1")
        func, year_opt = ST_ANALYTICS[selected_company]
    func(selected_company)

# ------------------------------------------------------------------------------------------------------------------------
def main2():
    with st.sidebar:
        st.divider()
        st.subheader("자동 분석 리포팅 생성")
        st.caption("아래 리포팅은 사람의 개입없이 매일 동일한시간에 자동으로 :blue[주가챠트 화면을 캡쳐]하여 :blue[기술적 분석 리포팅 생성] 하는 예제 입니다")
        pdf_file_path = "./sdemo_sample.pdf"
        # PDF 파일을 바이너리로 읽기
        with open(pdf_file_path, "rb") as f:
            pdf_content = f.read()
        st.download_button(
            label="Download PDF",
            data=pdf_content,
            file_name="sdemo_sample.pdf",
            mime="application/pdf"
        )

# ------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # page_icon=":chart_with_upwards_trend:
    st.set_page_config(page_icon = ':sparkles:', page_title = 'sdemo', layout = 'wide',)

    hide_streamlit_style = """
        <style>
        [data-testid="stToolbar"] {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    main1()
    
    main2()
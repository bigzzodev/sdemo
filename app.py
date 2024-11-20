import streamlit as st
from analytics import ST_ANALYTICS

def _fnumber(num):
    return "{:,}".format(num)
# ------------------------------------------------------------------------------------------------------------------------
def main1():

    st.subheader(f'뉴스 분석 시스템')

    with st.sidebar:
        st.subheader("뉴스 기사 분석 시스템")
        singer_opt = list(ST_ANALYTICS.keys())
        selected_company = st.selectbox(label="회사를 선택하세요", options=singer_opt, key="main_button1")
        func, year_opt = ST_ANALYTICS[selected_company]


    tab1, tab2, tab3 = st.tabs(["전체 뉴스 통계", "시스템에 대한 설명", "분류기준 설명"])
    with tab1:
        col_a , _ = st.columns(2)
        col_a.metric("총 뉴스 기사수 ( 2020.01.01 ~ 2024.11.04 ) ", _fnumber(149279) + " 개", "")
        col1, col2, col3, col4, col5,= st.columns(5)
        col1.metric("INSURANCE 관련기사", _fnumber(11213) + " 개", "")
        col2.metric("BUSINESS 관련기사", _fnumber(15658) + " 개", "")
        col3.metric("ESG 관련기사", _fnumber(9374) + " 개", "")
        col4.metric("COMPLIANCE 관련기사", _fnumber(16917) + " 개", "")
        col5.metric("ORGANIZATION 관련기사", _fnumber(8903) + " 개", "")
        col6, col7, col8, col9, col10 = st.columns(5)
        col6.metric("MARKET 관련기사", _fnumber(10903) + " 개", "")
        col7.metric("TECHINNOV 관련기사", _fnumber(4016) + " 개", "")
        col8.metric("SPORTS 관련기사", _fnumber(51282) + " 개", "")
        col9.metric("AD 관련기사", _fnumber(820) + " 개", "")
        col10.metric("NO 관련기사", _fnumber(20193) + " 개", "")
    with tab2:
        st.markdown(f"<h4><span style='font-size:20px; color:gray;'>시스템 설명</span></h4>", unsafe_allow_html=True)
        st.write('지원자: 김동주 (KIM DONGJOO)')
        st.write('이메일: encert@naver.com')
        st.write('')
        # st.write('국내 언론에서 "삼성생명" 의 기사를 파악하여, 인사이트 도출과 전략수립, 리스크관리 그리고 경쟁사 비교등에 사용할수 있도록 데모를 만들어 보았습니다.')
        # st.write('2020.01.01 부터 2024.11.04 까지의 "삼성생명"에 대한 국내 언론뉴스를 ""빠짐없이 모두"" 수집하여,')
        # st.write('llm (AI) 을 통한 카테코리 분류, 요약, 키워드 추출, 통계, 분석을 수행하는 시스템 입니다.')

        st.caption('국내 언론에서 "삼성생명" 의 기사를 파악하여, 인사이트 도출과 전략수립, 리스크 관리 그리고 경쟁사 비교등에 사용할수 있도록 데모를 만들어 보았습니다.')
        st.caption('2020.01.01 부터 2024.11.04 까지의 "삼성생명"에 대한 국내 언론뉴스를 ""빠짐없이 모두"" 수집하여, llm (AI) 을 통한 카테코리 분류, 요약, 키워드 추출, 통계, 분석을 수행하는 시스템 입니다.')

        st.write('- **Brand monitoring** : 미디어에서 브랜드가 어떻게 다루어지고 있는지 추적 및 분석.')
        st.write('- **Competitor analysis** : 경쟁사의 활동과 전략을 모니터링.')
        st.write('- **Market research** : 소비자 트렌드와 시장 심리에 대한 데이터 수집.')
        st.write('- **News aggregation** : 기업의 뉴스기반 지식 데이터 수집.')
        st.write('- **Data analysis** : 정치, 경제, 사회 문제 등 다양한 주제에 대한 연구 기반 구축.')


    with tab3:
        st.markdown(f"<h4><span style='font-size:20px; color:gray;'>분류기준</span></h4>", unsafe_allow_html=True)
        st.write('- **INSURANCE** : 삼성생명의 금융 상품이나 보험 상품에 관한 내용')
        st.write('- **BUSINESS** : 삼성생명의 경영 활동이나 실적과 관련된 내용')
        st.write('- **ESG** : 삼성생명의 사회적 책임 활동이나 ESG(환경, 사회, 지배구조)와 관련된 내용')
        st.write('- **COMPLIANCE** : 삼성생명과 관련된 법적 문제나 규제 이슈에 대한 내용')
        st.write('- **ORGANIZATION** : 삼성생명의 인사 이동이나 조직 개편과 관련된 내용')
        st.write('- **MARKET** : 삼성생명의 보험 및 금융 시장에서의 위치나 경쟁 상황과 관련된 내용')
        st.write('- **TECHINNOV** : 삼성생명의 기술 혁신이나 디지털 전환과 관련된 내용')
        st.write('- **SPORTS** : 삼성생명 소속 스포츠 구단이나, 스포츠 육성 및 저변확대에 관련된 내용')
        st.write('- **AD** : 삼성생명의 광고 캠페인이나 홍보 활동과 관련된 내용')
        st.write('- **NO** : 삼성생명과 관련된 특정 카테고리에 포함되지 않는 내용')
    st.divider()




    # func(selected_company)

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
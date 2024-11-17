import os
import json
import streamlit as st
from streamlit_echarts import st_echarts
from .chart_options import year_company_option, year_series, month_company_option, month_series, all_company_option, all_series
from annotated_text import annotated_text, annotation, parameters
from collections import defaultdict
SX_CLASS_NAME = ["INSURANCE", "BUSINESS", "ESG", "COMPLIANCE", "ORGANIZATION", "MARKET", "TECHINNOV", "SPORTS", "AD", "NO"]
os.environ["STREAMLIT_THEME_BASE"] = "dark"

def _fnumber(num):
    return "{:,}".format(num)

# ------------------------------------------------------------------------------------------------------------------------
def _generate_data_list(json_data):
    class_names = ["class_INSURANCE", "class_BUSINESS", "class_ESG", "class_COMPLIANCE", 
                   "class_ORGANIZATION", "class_MARKET", "class_TECHINNOV", "class_SPORTS", "class_AD", "class_NO"]
    data_list = []
    for class_name in class_names:
        year_values = []
        for year_data in json_data:
            year_key = list(year_data.keys())[0]
            class_counts = year_data[year_key].get("class_counts", {})
            year_values.append(class_counts.get(class_name, 0))
        data_list.append(year_values)
    return data_list

# ------------------------------------------------------------------------------------------------------------------------
def _extract_year_data(_year, _data):
    class_keys = ["class_INSURANCE", "class_BUSINESS", "class_ESG", "class_COMPLIANCE", "class_ORGANIZATION", "class_MARKET", "class_TECHINNOV", "class_SPORTS", "class_AD", "class_NO"]
    year_data = {class_name: [0] * 12 for class_name in class_keys}
    for entry in _data:
        for month, info in entry.items():
            entry_year, entry_month = month.split("-")
            if entry_year == _year:
                month_index = int(entry_month) - 1
                for class_name in class_keys:
                    year_data[class_name][month_index] = info["class_counts"].get(class_name, 0)
    data_list = [year_data[class_name][::-1] for class_name in class_keys]
    return data_list

# ------------------------------------------------------------------------------------------------------------------------
def _get_total_articles(json_data, target_month):
    for month_data in json_data:
        if target_month in month_data:
            return month_data[target_month].get("total_articles", 0)
    return 0

# ------------------------------------------------------------------------------------------------------------------------
def _get_all_articles(json_data, target_year):
    for year_data in json_data:
        if target_year in year_data:
            return year_data[target_year].get("total_articles", 0)
    return 0

# ------------------------------------------------------------------------------------------------------------------------
def _extract_monthly_data(_year_month, _json_data):
    class_keys = ["class_INSURANCE", "class_BUSINESS", "class_ESG", "class_COMPLIANCE", "class_ORGANIZATION", 
                  "class_MARKET", "class_TECHINNOV", "class_SPORTS", "class_AD", "class_NO"]
    class_data = {class_name: [0] * 31 for class_name in class_keys}
    for month_data in _json_data:
        for date, day_data in month_data.items():
            if date.startswith(_year_month):  # "년-월"에 해당하는 날짜만 추출
                day = int(date.split("-")[2]) - 1  # 일별 인덱스 (0부터 시작)
                for class_type, count in day_data["class_counts"].items():
                    if class_type in class_keys:  # 클래스 키에 해당하는 데이터만 업데이트
                        class_data[class_type][day] = count  # 해당 일에 카운트 데이터 추가

    # data_list 생성 (클래스명과 날짜 레이블 없이 일별 카운트만 포함)
    data_list = [class_data[class_type] for class_type in class_keys]
    return data_list

# ------------------------------------------------------------------------------------------------------------------------
def _get_total(json_data, target_date):
    for month_data in json_data:
        if target_date in month_data:
            total = month_data[target_date].get("total_articles", 0) 
            return total
    return 0

# ------------------------------------------------------------------------------------------------------------------------
def _get_news_agencies(json_data, target_date):
    for month_data in json_data:
        if target_date in month_data:
            news_agencies = month_data[target_date].get("news_agencies", {})
            sorted_news_agencies = dict(sorted(news_agencies.items(), key=lambda x: x[1], reverse=True))
            return sorted_news_agencies
    return {}

# ------------------------------------------------------------------------------------------------------------------------
def _get_bullets(json_data, target_date, class_type):
    for month_data in json_data:
        if target_date in month_data:
            summaries = month_data[target_date].get("summary_per_class", {})
            if class_type in summaries:
                return summaries[class_type][0].get("bullet", [])
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _get_urls(json_data, target_date, class_type):
    for month_data in json_data:
        if target_date in month_data:
            urls = month_data[target_date].get("url_per_class", {})
            if class_type in urls:
                return urls[class_type]
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _get_reasons(json_data, target_date, class_type):
    for month_data in json_data:
        if target_date in month_data:
            reasons = month_data[target_date].get("reason_per_class", {})
            if class_type in reasons:
                return reasons[class_type]
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _get_hashtags(json_data, target_date, class_type):
    if class_type == 'class_MENTION':
        return []
    for month_data in json_data:
        if target_date in month_data:
            entities = month_data[target_date].get("entities_per_class", {})
            if class_type in entities:
                sorted_entities = dict(sorted(entities[class_type].items(), key=lambda x: x[1], reverse=True))
                return sorted_entities
    return []

# ------------------------------------------------------------------------------------------------------------------------
def _is_skip_date(_json_data, _target):
    for month_data in _json_data:
        if _target in month_data:
            return True
    return False

# ------------------------------------------------------------------------------------------------------------------------
def _is_skip_class(_json_data, _target, _class):
    for month_data in _json_data:
        if _target in month_data:
            urls = month_data[_target].get("class_counts", {})
            if _class in urls:
                return True, urls[_class]
    return False, None

# ------------------------------------------------------------------------------------------------------------------------
def all_dashboard_company(_company):
    st.subheader(f'분석할 회사 : {_company}')
    st.divider()
    # tab1, tab2, tab3 = st.tabs(["전체 뉴스 통계", "시스템에 대한 설명", "분류기준 설명"])
    # with tab1:
    #     col_a , _ = st.columns(2)
    #     col_a.metric("총 뉴스 기사수 ( 2020.01.01 ~ 2024.11.04 ) ", _fnumber(149279) + " 개", "")
    #     col1, col2, col3, col4, col5,= st.columns(5)
    #     col1.metric("INSURANCE 관련기사", _fnumber(11213) + " 개", "")
    #     col2.metric("BUSINESS 관련기사", _fnumber(15658) + " 개", "")
    #     col3.metric("ESG 관련기사", _fnumber(9374) + " 개", "")
    #     col4.metric("COMPLIANCE 관련기사", _fnumber(16917) + " 개", "")
    #     col5.metric("ORGANIZATION 관련기사", _fnumber(8903) + " 개", "")
    #     col6, col7, col8, col9, col10 = st.columns(5)
    #     col6.metric("MARKET 관련기사", _fnumber(10903) + " 개", "")
    #     col7.metric("TECHINNOV 관련기사", _fnumber(4016) + " 개", "")
    #     col8.metric("SPORTS 관련기사", _fnumber(51282) + " 개", "")
    #     col9.metric("AD 관련기사", _fnumber(820) + " 개", "")
    #     col10.metric("NO 관련기사", _fnumber(20193) + " 개", "")
    # with tab2:
    #     st.markdown(f"<h4><span style='font-size:20px; color:gray;'>시스템 설명</span></h4>", unsafe_allow_html=True)
    #     st.write('지원자: 김동주 (KIM DONGJOO)')
    #     st.write('이메일: encert@naver.com')
    #     st.write('')
    #     # st.write('국내 언론에서 "삼성생명" 의 기사를 파악하여, 인사이트 도출과 전략수립, 리스크관리 그리고 경쟁사 비교등에 사용할수 있도록 데모를 만들어 보았습니다.')
    #     # st.write('2020.01.01 부터 2024.11.04 까지의 "삼성생명"에 대한 국내 언론뉴스를 ""빠짐없이 모두"" 수집하여,')
    #     # st.write('llm (AI) 을 통한 카테코리 분류, 요약, 키워드 추출, 통계, 분석을 수행하는 시스템 입니다.')

    #     st.caption('국내 언론에서 "삼성생명" 의 기사를 파악하여, 인사이트 도출과 전략수립, 리스크 관리 그리고 경쟁사 비교등에 사용할수 있도록 데모를 만들어 보았습니다.')
    #     st.caption('2020.01.01 부터 2024.11.04 까지의 "삼성생명"에 대한 국내 언론뉴스를 ""빠짐없이 모두"" 수집하여, llm (AI) 을 통한 카테코리 분류, 요약, 키워드 추출, 통계, 분석을 수행하는 시스템 입니다.')


    # with tab3:
    #     st.markdown(f"<h4><span style='font-size:20px; color:gray;'>분류기준</span></h4>", unsafe_allow_html=True)
    #     st.write('- **INSURANCE** : 삼성생명의 금융 상품이나 보험 상품에 관한 내용')
    #     st.write('- **BUSINESS** : 삼성생명의 경영 활동이나 실적과 관련된 내용')
    #     st.write('- **ESG** : 삼성생명의 사회적 책임 활동이나 ESG(환경, 사회, 지배구조)와 관련된 내용')
    #     st.write('- **COMPLIANCE** : 삼성생명과 관련된 법적 문제나 규제 이슈에 대한 내용')
    #     st.write('- **ORGANIZATION** : 삼성생명의 인사 이동이나 조직 개편과 관련된 내용')
    #     st.write('- **MARKET** : 삼성생명의 보험 및 금융 시장에서의 위치나 경쟁 상황과 관련된 내용')
    #     st.write('- **TECHINNOV** : 삼성생명의 기술 혁신이나 디지털 전환과 관련된 내용')
    #     st.write('- **SPORTS** : 삼성생명 소속 스포츠 구단이나, 스포츠 육성 및 저변확대에 관련된 내용')
    #     st.write('- **AD** : 삼성생명의 광고 캠페인이나 홍보 활동과 관련된 내용')
    #     st.write('- **NO** : 삼성생명과 관련된 특정 카테고리에 포함되지 않는 내용')
    # st.divider()

    fmname = f'./jsondata/year_{_company}.json'
    with open(fmname, "r", encoding="utf-8") as file:
        year_data = json.load(file)

    data_list = _generate_data_list(year_data)
    names = SX_CLASS_NAME
    series = all_series(names, data_list)
    options = all_company_option(series)

    if 'legend_selected' not in st.session_state:
        st.session_state['legend_selected'] = {name: True for name in names}
    options['legend']['selected'] = st.session_state['legend_selected']
    options['legend']['textStyle'] = {
        'color': 'gray',
        'fontSize': 14,
        # 'fontWeight': 'bold',
    }
    events = {
        "click": "function(params) { return [params.type, params.name, params.value, "
                 "params.componentType, params.seriesType, params.seriesIndex, params.seriesName, "
                 "params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
        "legendselectchanged": "function(params) { return ['legendselectchanged', params.selected]; }",
    }
    st.success('자세히 보기를 원하는 "년도"를 클릭하세요', icon="📌")
    spacer_col, clear_col, all_col = st.columns([0.43, 0.05, 0.52], gap="small")
    with all_col:
        if st.button("clear", key="key_all_button11"):
            options['legend']['selected'] = {name: False for name in names}
            st.session_state['legend_selected'] = options['legend']['selected']
            st.session_state['show_main_dashboard'] = False
    with clear_col:
        if st.button("all", key="key_all_button1"):
            options['legend']['selected'] = {name: True for name in names}
            st.session_state['legend_selected'] = options['legend']['selected']
            st.session_state['show_main_dashboard'] = False

    s = st_echarts(options=options, events=events, height="500px", key="key_all_dashboard")
    st.divider()
    if s is not None:
        if s[0] == 'legendselectchanged':
            st.session_state['legend_selected'] = s[1]
            st.session_state['show_main_dashboard'] = False
        else:
            xx = s[1].replace("년", "").strip()
            susu = _get_all_articles(year_data, xx)
            year_dashboard(_company, xx, susu)
    else:
        st.session_state['legend_selected'] = options['legend']['selected']

# ------------------------------------------------------------------------------------------------------------------------
def year_dashboard(_company, _selected_year, susu):
    head = f'{_selected_year}년'
    st.markdown(f"<h3>{head} - <span style='font-size:20px;'>( 전체 기사수 {_fnumber(susu)} 개 )</span></h3>", unsafe_allow_html=True)
    names = SX_CLASS_NAME
    fmname = f'./jsondata/month_{_company}.json'
    with open(fmname, "r", encoding="utf-8") as file:
        month_data = json.load(file)

    data_list = _extract_year_data(_selected_year, month_data)
    series = year_series(names, data_list)
    options = year_company_option(series)

    options['legend']['selected'] = st.session_state.get('legend_selected', {name: True for name in names})
    options['legend']['textStyle'] = {
        'color': 'gray',
        'fontSize': 14,
        # 'fontWeight': 'bold',
    }
    events = {
        "click": "function(params) { return [params.type, params.name, params.value, "
                 "params.componentType, params.seriesType, params.seriesIndex, params.seriesName, "
                 "params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
        "legendselectchanged": "function(params) { return ['legendselectchanged', params.selected]; }",
    }

    st.success('자세히 보기를 원하는 "월"을 클릭하세요', icon="📌")
    s = st_echarts(options=options, events=events, height="500px", key="key_year_dashboard")
    st.divider()

    if s is not None:
        if s[0] == 'legendselectchanged':
            st.session_state['legend_selected'] = s[1]
            st.session_state['show_main_dashboard'] = False
        else:
            xx = s[1].replace("월", "").strip()
            susu = _get_total_articles(month_data, f'{_selected_year}-{xx}')
            month_dashboard(_company, susu, _selected_year, s[1])
    else:
        st.session_state['legend_selected'] = options['legend']['selected']

# ------------------------------------------------------------------------------------------------------------------------
def month_dashboard(_company, susu, _selected_year, _month):
    head = f'{_selected_year}년 {_month}'
    st.markdown(f"<h3>{head} - <span style='font-size:20px;'>( 전체 기사수 {_fnumber(susu)} 개 )</span></h3>", unsafe_allow_html=True)
    names = SX_CLASS_NAME
    fdname = f'./jsondata/day_{_company}_{_selected_year}.json'
    with open(fdname, "r", encoding="utf-8") as file:
        day_data = json.load(file)
    ynname = head.replace("년 ", "-").replace("월", "").strip()
    data_list = _extract_monthly_data(ynname, day_data)
    series = month_series(names, data_list)
    options = month_company_option(series)
    options['legend']['selected'] = st.session_state.get('legend_selected', {name: True for name in names})
    options['legend']['textStyle'] = {
        'color': 'gray',
        'fontSize': 14,
        # 'fontWeight': 'bold',
    }
    eventsx = {
        "click": "function(params) { return [params.type, params.name, params.value, "
                 "params.componentType, params.seriesType, params.seriesIndex, params.seriesName, "
                 "params.dataIndex, params.dataType, params.data, params.color, params.info ]}",
        "legendselectchanged": "function(params) { return ['legendselectchanged', params.selected]; }",
    }

    st.success('자세히 보기를 원하는 "날짜"를 클릭하세요', icon="📌")
    s = st_echarts(options=options, events=eventsx, height="500px", key="key_month_dashboard")
    st.divider()

    if 'show_main_dashboard' not in st.session_state:
        st.session_state['show_main_dashboard'] = False

    if s is not None:
        if s[0] == 'legendselectchanged':
            st.session_state['legend_selected'] = s[1]
            st.session_state['show_main_dashboard'] = False
        else:
            head = f'{head} {s[1]}'
            st.session_state['day_head'] = head
            st.session_state['company'] = _company
            st.session_state['day_data'] = day_data
            st.session_state['show_main_dashboard'] = True
    else:
        st.session_state['legend_selected'] = options['legend']['selected']

    if st.session_state.get('show_main_dashboard', False):
        st.subheader(st.session_state['day_head'])
        day_dashboard(st.session_state['company'], st.session_state['day_data'], st.session_state['day_head'])

# ------------------------------------------------------------------------------------------------------------------------
def day_dashboard(_company, day_data, _head):
    dname = _head.replace("년 ", "-").replace("월 ", "-").replace("일", "").strip()
    if not _is_skip_date(day_data, dname):
        return
    except_mention = [name for name in SX_CLASS_NAME if name != "MENTION"]
    class_counts = []
    for _cidx in except_mention:
        is_skip, class_count = _is_skip_class(day_data, dname, f'class_{_cidx}')
        if is_skip:
            class_counts.append((_cidx, class_count))

    selected_classes = [name for name, selected in st.session_state.get('legend_selected', {}).items() if selected]
    sorted_classes = sorted(
        [item for item in class_counts if item[0] in selected_classes],
        key=lambda x: x[1], reverse=True
    )
    for _cidx, class_count in sorted_classes:
        class_dashboard(day_data, dname, _cidx)

    if "MENTION" in selected_classes:
        class_dashboard(day_data, dname, "MENTION")

    st.error('NEWS AGENCIES', icon="📄")
    agency_list = _get_news_agencies(day_data, dname)
    with st.expander(f"\"{_head}\" 에 위 기사들을 게재한 언론사 리스트:"):
        for key, value in agency_list.items():
            st.write(f'{key} ({value})')
    st.divider()

# ------------------------------------------------------------------------------------------------------------------------
def class_dashboard(day_data, _dname, _class):
    is_skip, class_count = _is_skip_class(day_data, _dname, f'class_{_class}')
    if not is_skip:
        return

    total = _get_total(day_data, _dname)
    st.info(f'**{_class}** ( {class_count} 개 / 총기사수 {total} 개)')

    hashtags = _get_hashtags(day_data, _dname, f'class_{_class}')
    if hashtags:
        def generate_annotated_text(_data):
            annotations = []
            for key, value in _data.items():
                annotations.append(annotation(key, f"({value})", font_family="Comic Sans MS", border="2px red"))
                annotations.append("  ")
            if annotations:
                annotations.pop()
            annotated_text(*annotations)
        generate_annotated_text(hashtags)

    summary_list = _get_bullets(day_data, _dname, f'class_{_class}')
    with st.expander("SUMMARY:"):
        for _idx in summary_list:
            st.code(_idx)

    url_list = _get_urls(day_data, _dname, f'class_{_class}')
    reason_list = _get_reasons(day_data, _dname, f'class_{_class}')
    with st.expander("URLS:"):
        for idx, url in enumerate(url_list):
            key = f"url_{_class}_{_dname}_{idx}"
            if key not in st.session_state:
                st.session_state[key] = False
            cols = st.columns([0.85, 0.15])
            with cols[0]:
                st.write(url)
            with cols[1]:
                if st.button("요약 정리", key=f"show_button_{_class}_{_dname}_{idx}"):
                    st.session_state[key] = not st.session_state[key]
            if st.session_state[key]:
                st.write(reason_list[idx])
    st.divider()

# ------------------------------------------------------------------------------------------------------------------------
def ready_dashboard_company(_company):
    st.subheader(f'분석할 회사 : {_company}')
    st.write('예시 페이지 입니다.')

# eof

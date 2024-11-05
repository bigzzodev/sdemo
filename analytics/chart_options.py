# ------------------------------------------------------------------------------------------------------------------------
def all_news_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["MENTION", "BAD", "GOOD", "MUSIC", "ENT", 'CONTRACT', 'AD', 'RIP', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["2020년", "2021년", "2022년", "2023년", "2024년"],
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def all_company_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["INSURANCE", "BUSINESS", "ESG", "COMPLIANCE", "ORGANIZATION", 'MARKET', 'TECHINNOV', 'SPORTS', 'AD', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["2020년", "2021년", "2022년", "2023년", "2024년"],
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def all_series(_names, _data_list):
    series = []
    for name, data in zip(_names, _data_list):
        item = {
            "name": name,
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": data
        }
        series.append(item)
    return series

# ------------------------------------------------------------------------------------------------------------------------
def year_news_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["MENTION", "BAD", "GOOD", "MUSIC", "ENT", 'CONTRACT', 'AD', 'RIP', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["12월", "11월", "10월", "09월", "08월", "07월", "06월", "05월", "04월", "03월", "02월", "01월"],
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def year_company_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["INSURANCE", "BUSINESS", "ESG", "COMPLIANCE", "ORGANIZATION", 'MARKET', 'TECHINNOV', 'SPORTS', 'AD', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "xAxis": {"type": "value"},
        "yAxis": {
            "type": "category",
            "data": ["12월", "11월", "10월", "09월", "08월", "07월", "06월", "05월", "04월", "03월", "02월", "01월"],
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def year_series(_names, _data_list):
    series = []
    for name, data in zip(_names, _data_list):
        item = {
            "name": name,
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": data
        }
        series.append(item)
    return series

# ------------------------------------------------------------------------------------------------------------------------
def month_news_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["MENTION", "BAD", "GOOD", "MUSIC", "ENT", 'CONTRACT', 'AD', 'RIP', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "yAxis": {"type": "value"},
        "xAxis": {
            "type": "category",
            "data": ["01일", "02일", "03일", "04일", "05일", "06일", "07일", "08일", "09일", "10일", "11일", "12일", "13일", "14일", "15일", "16일", "17일", "18일", "19일", "20일", "21일", "22일", "23일", "24일", "25일", "26일", "27일", "28일", "29일", "30일", "31일"]
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def month_company_option(_series):
    options = {
        "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
        "legend": {
            "data": ["INSURANCE", "BUSINESS", "ESG", "COMPLIANCE", "ORGANIZATION", 'MARKET', 'TECHINNOV', 'SPORTS', 'AD', 'NO'],
            "textStyle": {"color": "white"},
        },
        "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
        "yAxis": {"type": "value"},
        "xAxis": {
            "type": "category",
            "data": ["01일", "02일", "03일", "04일", "05일", "06일", "07일", "08일", "09일", "10일", "11일", "12일", "13일", "14일", "15일", "16일", "17일", "18일", "19일", "20일", "21일", "22일", "23일", "24일", "25일", "26일", "27일", "28일", "29일", "30일", "31일"]
        }
    }
    options["series"] = _series
    return options

# ------------------------------------------------------------------------------------------------------------------------
def month_series(_names, _data_list):
    series = []
    for name, data in zip(_names, _data_list):
        item = {
            "name": name,
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": data
        }
        series.append(item)
    return series

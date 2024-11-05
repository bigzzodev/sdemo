from .dashboard_company import all_dashboard_company, ready_dashboard_company

ST_COMPANY = {
    "삼성생명": (
        all_dashboard_company,
        ["2020", "2021", "2022", "2023", "2024"],
    ),
    "교보생명": (
        ready_dashboard_company,
        ["2020", "2021", "2022", "2023", "2024"],
    ),
    "한화생명": (
        ready_dashboard_company,
        ["2020", "2021", "2022", "2023", "2024"],
    ),
}
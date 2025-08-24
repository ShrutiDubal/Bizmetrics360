"""
BizMetrics360 - Dashboard Configuration
Easy customization settings for the KPI dashboard
"""

# Dashboard Settings
DASHBOARD_TITLE = "BizMetrics360 - KPI Intelligence Platform"
DASHBOARD_SUBTITLE = "Simplified Financial & Operational Metrics Dashboard"
PAGE_ICON = "📊"

# Data Settings
DATA_DIRECTORY = "data"
SAMPLE_DATA_FILES = {
    'revenue': 'revenue.csv',
    'customers': 'customers.csv', 
    'marketing': 'marketing.csv',
    'costs': 'costs.csv'
}

# KPI Thresholds (for alerts and color coding)
KPI_THRESHOLDS = {
    'revenue_growth_min': 5.0,      # Minimum acceptable revenue growth %
    'clv_cac_ratio_min': 3.0,       # Minimum CLV:CAC ratio
    'retention_rate_min': 80.0,     # Minimum retention rate %
    'gross_margin_min': 60.0,       # Minimum gross margin %
    'churn_rate_max': 15.0          # Maximum acceptable churn rate %
}

# Chart Colors
CHART_COLORS = {
    'primary': '#1f77b4',           # Blue
    'success': '#2ca02c',           # Green  
    'warning': '#ff7f0e',           # Orange
    'danger': '#d62728',            # Red
    'secondary': '#7f7f7f'          # Gray
}

# Date Range Options
DEFAULT_DATE_RANGE_DAYS = 30
DATE_FORMAT = "%Y-%m-%d"

# Export Settings
EXPORT_FORMATS = ['CSV', 'Excel']
DEFAULT_EXPORT_FORMAT = 'CSV'

# Display Settings
METRICS_DECIMAL_PLACES = 1
CURRENCY_SYMBOL = '$'
PERCENTAGE_SYMBOL = '%'

# Company Information
COMPANY_NAME = "Your Company Name"
COMPANY_LOGO = None  # Path to logo file if available
CONTACT_EMAIL = "analytics@yourcompany.com"

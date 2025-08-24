#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BizMetrics360 - Professional Business Intelligence Platform
A modern, high-end dashboard designed for enterprise use and resume impact.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# Page configuration - MUST BE FIRST
st.set_page_config(
    page_title='BizMetrics360 - Enterprise BI Platform',
    page_icon='📊',
    layout='wide',
    initial_sidebar_state='expanded'
)

# ============================== CSS ==============================
st.markdown("""
<style>
/* ---------- Global text color ---------- */
.stApp, .main, h1, h2, h3, h4, h5, h6, p, label, div, span, small {
  color: white !important;
}

/* Backgrounds */
.main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }

/* ---------- Header ---------- */
.header-container {
  background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
  padding: 30px;
  border-radius: 0 0 20px 20px;
  margin-bottom: 30px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
.header-title { color: white !important; font-size: 2.5rem; font-weight: 700; text-align: center; }
.header-subtitle { color: rgba(255,255,255,0.9) !important; text-align: center; font-size: 1.1rem; }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
  color: white !important;
}
[data-testid="stSidebar"] * { color: white !important; }

/* Inputs (date/text/number) */
[data-testid="stSidebar"] .stDateInput input,
[data-testid="stSidebar"] .stTextInput input,
[data-testid="stSidebar"] .stNumberInput input {
  background-color: rgba(0,0,0,0.35) !important;
  color: #ffffff !important;
  border: 1px solid rgba(255,255,255,0.35) !important;
  border-radius: 10px !important;
  caret-color: #ffffff !important;
}

/* Selectbox visible control surface */
[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
  background-color: rgba(0,0,0,0.35) !important;
  border: 1px solid rgba(255,255,255,0.35) !important;
  border-radius: 10px !important;
}

/* Placeholders + selected text */
[data-testid="stSidebar"] input::placeholder,
[data-testid="stSidebar"] textarea::placeholder,
[data-testid="stSidebar"] [data-baseweb="select"] span {
  color: #ffffff !important; opacity: 1 !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] div { color: #ffffff !important; }
[data-testid="stSidebar"] [data-baseweb="select"] svg { fill: #ffffff !important; }

/* ---------- BaseWeb dropdown menu (portal) — FORCE DARK EVERYWHERE ---------- */
/* Menu root containers */
[data-baseweb="popover"] [data-baseweb="menu"],
[data-baseweb="popover"] [role="listbox"],
div[data-baseweb="menu"],
div[role="listbox"],
ul[role="listbox"] {
  background-color: #1f2a36 !important;    /* dark surface */
  color: #ffffff !important;
  border: 1px solid rgba(255,255,255,0.25) !important;
  box-shadow: 0 10px 24px rgba(0,0,0,0.4) !important;
}

/* Make sure any inner wrappers also inherit dark background */
[data-baseweb="popover"] [data-baseweb="menu"] *,
[data-baseweb="popover"] [role="listbox"] *,
div[data-baseweb="menu"] *,
div[role="listbox"] *,
ul[role="listbox"] * {
  color: #ffffff !important;
  background-color: transparent !important;
}

/* Options (li/div) default, hover, selected, disabled */
[role="option"] { background-color: transparent !important; color: #ffffff !important; }
[role="option"]:hover,
[role="option"][aria-selected="true"] {
  background-color: #33485e !important;
  color: #ffffff !important;
}
[role="option"][aria-disabled="true"] {
  color: rgba(255,255,255,0.45) !important;
}

/* Date picker popover (calendar) */
div[role="dialog"], div[role="tooltip"] {
  background-color: #2f3e4d !important;
  color: #ffffff !important;
  border: 1px solid rgba(255,255,255,0.25) !important;
}

/* ---------- Metric cards ---------- */
.metric-card {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 15px;
  padding: 20px;
  margin: 10px 0;
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
}
.metric-value { font-size: 2.5rem; font-weight: 700; color: white !important; text-align: center; }
.metric-label { font-size: 0.9rem; color: white !important; text-align: center; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }
.metric-delta { font-size: 0.8rem; color: white !important; text-align: center; margin-top: 5px; }

/* Buttons */
.stButton > button {
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  color: white !important;
  border: none; border-radius: 25px; padding: 10px 25px;
  font-weight: 600; transition: all 0.3s ease;
}
.stButton > button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }

/* Dataframes */
.stDataFrame, .stTable, .dataframe { color: white !important; }

/* Responsive */
@media (max-width: 768px) {
  .header-title { font-size: 2rem; }
  .metric-value { font-size: 2rem; }
}
</style>
""", unsafe_allow_html=True)

# ============================== Data ==============================
@st.cache_data
def generate_enterprise_data():
    """Generate enterprise-grade sample data"""
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')

    revenue_data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.uniform(500000, 2000000, len(dates)) + np.sin(np.arange(len(dates))*0.5)*200000,
        'region': np.random.choice(['North America', 'Europe', 'Asia Pacific', 'Latin America'], len(dates)),
        'channel': np.random.choice(['Direct Sales', 'Online Platform', 'Partner Network', 'Enterprise'], len(dates)),
        'product_line': np.random.choice(['Software Licenses', 'Cloud Services', 'Consulting', 'Support'], len(dates))
    })

    customer_data = pd.DataFrame({
        'customer_id': range(1, 2001),
        'total_spent': np.random.uniform(5000, 50000, 2000),
        'purchase_count': np.random.randint(1, 50, 2000),
        'customer_lifespan_days': np.random.randint(90, 1825, 2000),
        'is_new_customer': np.random.choice([True, False], 2000, p=[0.2, 0.8]),
        'is_active': np.random.choice([True, False], 2000, p=[0.85, 0.15]),
        'churned': np.random.choice([True, False], 2000, p=[0.12, 0.88]),
        'region': np.random.choice(['North America', 'Europe', 'Asia Pacific', 'Latin America'], 2000),
        'company_size': np.random.choice(['Startup', 'SMB', 'Enterprise', 'Government'], 2000),
        'signup_date': np.random.choice(dates, 2000)
    })

    marketing_data = pd.DataFrame({
        'date': dates,
        'spend': np.random.uniform(50000, 300000, len(dates)),
        'channel': np.random.choice(['Google Ads', 'LinkedIn', 'Facebook', 'Trade Shows', 'Content Marketing'], len(dates)),
        'campaign': np.random.choice(['Brand Awareness', 'Lead Generation', 'Product Launch', 'Retargeting', 'Thought Leadership'], len(dates)),
        'impressions': np.random.randint(100000, 5000000, len(dates)),
        'clicks': np.random.randint(1000, 50000, len(dates)),
        'conversions': np.random.randint(50, 2000, len(dates))
    })

    cost_data = pd.DataFrame({
        'date': dates,
        'cost': revenue_data['revenue'] * np.random.uniform(0.4, 0.7, len(dates)),
        'cost_type': np.random.choice(['COGS', 'Operating Expenses', 'Marketing', 'R&D', 'Administrative'], len(dates)),
        'department': np.random.choice(['Sales', 'Marketing', 'Engineering', 'Support', 'Finance'], len(dates))
    })

    return {'revenue': revenue_data, 'customers': customer_data, 'marketing': marketing_data, 'costs': cost_data}

# ============================== KPIs ==============================
def calculate_enterprise_kpis(data):
    revenue_data = data['revenue']
    customer_data = data['customers']
    marketing_data = data['marketing']
    cost_data = data['costs']

    revenue_data['date'] = pd.to_datetime(revenue_data['date'])
    monthly_revenue = revenue_data.groupby(revenue_data['date'].dt.to_period('M'))['revenue'].sum()

    if len(monthly_revenue) > 1:
        mom_growth = ((monthly_revenue.iloc[-1] - monthly_revenue.iloc[-2]) / monthly_revenue.iloc[-2] * 100)
        yoy_growth = ((monthly_revenue.iloc[-1] - monthly_revenue.iloc[-13]) / monthly_revenue.iloc[-13] * 100) if len(monthly_revenue) > 12 else 0
    else:
        mom_growth = yoy_growth = 0

    total_marketing_spend = marketing_data['spend'].sum()
    new_customers = (customer_data['is_new_customer'] == True).sum()
    cac = total_marketing_spend / new_customers if new_customers > 0 else 0

    avg_order_value = customer_data['total_spent'].mean()
    avg_purchase_frequency = customer_data['purchase_count'].mean()
    avg_customer_lifespan = customer_data['customer_lifespan_days'].mean() / 365
    clv = avg_order_value * avg_purchase_frequency * avg_customer_lifespan
    clv_cac_ratio = clv / cac if cac > 0 else 0

    total_customers = len(customer_data)
    active_customers = (customer_data['is_active'] == True).sum()
    retention_rate = (active_customers / total_customers) * 100 if total_customers > 0 else 0

    churned_customers = (customer_data['churned'] == True).sum()
    churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0

    total_revenue = revenue_data['revenue'].sum()
    total_costs = cost_data['cost'].sum()
    gross_margin = ((total_revenue - total_costs) / total_revenue) * 100 if total_revenue > 0 else 0
    net_margin = gross_margin - 15

    total_conversions = marketing_data['conversions'].sum()
    total_clicks = marketing_data['clicks'].sum()
    conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0
    cpc = total_marketing_spend / total_clicks if total_clicks > 0 else 0

    return {
        'mom_growth': mom_growth, 'yoy_growth': yoy_growth,
        'cac': cac, 'clv': clv, 'clv_cac_ratio': clv_cac_ratio,
        'retention_rate': retention_rate, 'churn_rate': churn_rate,
        'gross_margin': gross_margin, 'net_margin': net_margin,
        'conversion_rate': conversion_rate, 'cpc': cpc,
        'total_revenue': total_revenue, 'total_costs': total_costs,
        'active_customers': active_customers, 'total_customers': total_customers,
        'total_marketing_spend': total_marketing_spend
    }

# ============================== UI Helpers ==============================
def render_header():
    st.markdown("""
    <div class="header-container">
        <h1 class="header-title">BizMetrics360</h1>
        <p class="header-subtitle">Enterprise Business Intelligence Platform</p>
    </div>
    """, unsafe_allow_html=True)

def render_metric_card(label, value, delta=None, format_type="number"):
    if format_type == "currency":
        display_value = f"${value:,.0f}"
    elif format_type == "percentage":
        display_value = f"{value:.1f}%"
    elif format_type == "ratio":
        display_value = f"{value:.1f}x"
    else:
        display_value = f"{value:,.0f}"

    delta_html = f'<div class="metric-delta">{"+" if delta and delta>0 else ""}{delta:.1f}%</div>' if delta is not None else ""

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{display_value}</div>
        <div class="metric-label">{label}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def style_plotly_white(fig, height=400):
    fig.update_layout(
        font=dict(color="white", size=12),
        title_font=dict(color="white"),
        xaxis=dict(color="white", title_font=dict(color="white"), tickfont=dict(color="white")),
        yaxis=dict(color="white", title_font=dict(color="white"), tickfont=dict(color="white")),
        legend=dict(font=dict(color="white")),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=height
    )
    return fig

# ============================== Main ==============================
def main():
    render_header()

    data = generate_enterprise_data()
    kpis = calculate_enterprise_kpis(data)

    # Sidebar controls
    st.sidebar.markdown("## 🎛️ Dashboard Controls")
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📅 Select Analysis Period")
    st.sidebar.date_input(
        'Select Analysis Period',
        value=(datetime.now() - timedelta(days=90), datetime.now()),
        max_value=datetime.now()
    )
    regions = ['Global'] + list(data['revenue']['region'].unique())
    selected_region = st.sidebar.selectbox('🌍 Region', regions)
    company_sizes = ['All Sizes'] + list(data['customers']['company_size'].unique())
    selected_size = st.sidebar.selectbox('🏢 Company Size', company_sizes)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Executive Summary", "💰 Financial Metrics", "👥 Customer Analytics", "📈 Marketing Performance"])

    with tab1:
        st.markdown("## 📊 Executive Summary")
        st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            render_metric_card("Revenue Growth (MoM)", kpis['mom_growth'], kpis['mom_growth'] - 5, "percentage")
        with col2:
            render_metric_card("CLV:CAC Ratio", kpis['clv_cac_ratio'], kpis['clv_cac_ratio'] - 3, "ratio")
        with col3:
            render_metric_card("Customer Retention", kpis['retention_rate'], kpis['retention_rate'] - 85, "percentage")
        with col4:
            render_metric_card("Gross Margin", kpis['gross_margin'], kpis['gross_margin'] - 65, "percentage")

        st.markdown("### 💰 Monthly Revenue Trend")
        revenue_trend = data['revenue'].groupby('date')['revenue'].sum().reset_index()
        fig_revenue = px.line(revenue_trend, x='date', y='revenue', title='Monthly Revenue Trend', template='plotly_white')
        st.plotly_chart(style_plotly_white(fig_revenue), use_container_width=True)

    with tab2:
        st.markdown("## 💰 Financial Metrics")
        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            render_metric_card("Total Revenue", kpis['total_revenue'], None, "currency")
            render_metric_card("Net Margin", kpis['net_margin'], None, "percentage")
        with col2:
            render_metric_card("Total Costs", kpis['total_costs'], None, "currency")
            render_metric_card("YoY Growth", kpis['yoy_growth'], None, "percentage")

        st.markdown("### 📈 Revenue vs Costs")
        fig_profit = go.Figure()
        fig_profit.add_trace(go.Bar(name='Revenue', x=['Total Revenue'], y=[kpis['total_revenue']], marker_color='#2ecc71'))
        fig_profit.add_trace(go.Bar(name='Costs', x=['Total Costs'], y=[kpis['total_costs']], marker_color='#e74c3c'))
        fig_profit.update_layout(title='Revenue vs Costs', template='plotly_white')
        st.plotly_chart(style_plotly_white(fig_profit), use_container_width=True)

    with tab3:
        st.markdown("## 👥 Customer Analytics")
        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            render_metric_card("Customer Acquisition Cost", kpis['cac'], None, "currency")
            render_metric_card("Customer Lifetime Value", kpis['clv'], None, "currency")
        with col2:
            render_metric_card("Active Customers", kpis['active_customers'], None, "number")
            render_metric_card("Churn Rate", kpis['churn_rate'], None, "percentage")

        st.markdown("### 👥 Customer Status Distribution")
        customer_metrics = pd.DataFrame({
            'Status': ['Active Customers', 'Churned Customers'],
            'Count': [kpis['active_customers'], kpis['total_customers'] - kpis['active_customomers']] if False else {
                'dummy': 0}  # prevent lint warning
        })
        customer_metrics = pd.DataFrame({
            'Status': ['Active Customers', 'Churned Customers'],
            'Count': [kpis['active_customers'], kpis['total_customers'] - kpis['active_customers']]
        })
        fig_customers = px.pie(customer_metrics, values='Count', names='Status', title='Customer Status Distribution', template='plotly_white')
        st.plotly_chart(style_plotly_white(fig_customers), use_container_width=True)

    with tab4:
        st.markdown("## 📈 Marketing Performance")
        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            render_metric_card("Conversion Rate", kpis['conversion_rate'], None, "percentage")
            render_metric_card("Cost Per Click", kpis['cpc'], None, "currency")
        with col2:
            render_metric_card("Total Marketing Spend", kpis['total_marketing_spend'], None, "currency")
            render_metric_card("Marketing ROI", (kpis['clv_cac_ratio'] - 1) * 100, None, "percentage")

        st.markdown("### 📊 Marketing ROI by Channel")
        channel_perf = data['marketing'].groupby('channel').agg({'spend': 'sum', 'conversions': 'sum', 'clicks': 'sum'}).reset_index()
        channel_perf['roi'] = np.random.uniform(2, 8, len(channel_perf))
        fig_channels = px.bar(channel_perf, x='channel', y='roi', title='Marketing ROI by Channel', template='plotly_white')
        st.plotly_chart(style_plotly_white(fig_channels), use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #ffffff; padding: 20px;">
        <p><strong>BizMetrics360</strong> - Enterprise Business Intelligence Platform</p>
        <p>Built with modern technologies for professional business analytics</p>
    </div>
    """, unsafe_allow_html=True)

# Run
if __name__ == '__main__':
    main()

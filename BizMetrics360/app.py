#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BizMetrics360 - Simplified Financial & Operational KPI Intelligence Platform
A streamlined version focusing on core KPIs with minimal complexity.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title='BizMetrics360 - KPI Dashboard',
    page_icon='📊',
    layout='wide'
)

# Sample data generation (in real app, this would come from your data sources)
@st.cache_data
def generate_sample_data():
    """Generate sample data for demonstration"""
    np.random.seed(42)
    
    # Revenue data
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='ME')
    revenue_data = pd.DataFrame({
        'date': dates,
        'revenue': np.random.uniform(50000, 150000, len(dates)),
        'region': np.random.choice(['North', 'South', 'East', 'West'], len(dates)),
        'channel': np.random.choice(['Direct', 'Online', 'Partners'], len(dates))
    })
    
    # Customer data
    customer_data = pd.DataFrame({
        'customer_id': range(1, 1001),
        'total_spent': np.random.uniform(100, 5000, 1000),
        'purchase_count': np.random.randint(1, 20, 1000),
        'customer_lifespan_days': np.random.randint(30, 1095, 1000),
        'is_new_customer': np.random.choice([True, False], 1000, p=[0.3, 0.7]),
        'is_active': np.random.choice([True, False], 1000, p=[0.8, 0.2]),
        'churned': np.random.choice([True, False], 1000, p=[0.15, 0.85])
    })
    
    # Marketing spend data
    marketing_data = pd.DataFrame({
        'date': dates,
        'spend': np.random.uniform(5000, 25000, len(dates)),
        'channel': np.random.choice(['Google Ads', 'Facebook', 'LinkedIn'], len(dates))
    })
    
    # Cost data
    cost_data = pd.DataFrame({
        'date': dates,
        'cost': revenue_data['revenue'] * np.random.uniform(0.3, 0.7, len(dates))
    })
    
    return {
        'revenue': revenue_data,
        'customers': customer_data,
        'marketing': marketing_data,
        'costs': cost_data
    }

# KPI Calculations
def calculate_kpis(data):
    """Calculate key performance indicators"""
    revenue_data = data['revenue']
    customer_data = data['customers']
    marketing_data = data['marketing']
    cost_data = data['costs']
    
    # Revenue Growth Rate
    revenue_data['date'] = pd.to_datetime(revenue_data['date'])
    monthly_revenue = revenue_data.groupby(revenue_data['date'].dt.to_period('M'))['revenue'].sum()
    revenue_growth = ((monthly_revenue.iloc[-1] - monthly_revenue.iloc[-2]) / monthly_revenue.iloc[-2] * 100) if len(monthly_revenue) > 1 else 0
    
    # CAC & CLV
    total_marketing_spend = marketing_data['spend'].sum()
    new_customers = len(customer_data[customer_data['is_new_customer'] == True])
    cac = total_marketing_spend / new_customers if new_customers > 0 else 0
    
    avg_order_value = customer_data['total_spent'].mean()
    avg_purchase_frequency = customer_data['purchase_count'].mean()
    avg_customer_lifespan = customer_data['customer_lifespan_days'].mean() / 365
    clv = avg_order_value * avg_purchase_frequency * avg_customer_lifespan
    clv_cac_ratio = clv / cac if cac > 0 else 0
    
    # Retention & Churn
    total_customers = len(customer_data)
    active_customers = len(customer_data[customer_data['is_active'] == True])
    retention_rate = (active_customers / total_customers) * 100 if total_customers > 0 else 0
    
    churned_customers = len(customer_data[customer_data['churned'] == True])
    churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0
    
    # Gross Margin
    total_revenue = revenue_data['revenue'].sum()
    total_costs = cost_data['cost'].sum()
    gross_margin = ((total_revenue - total_costs) / total_revenue) * 100 if total_revenue > 0 else 0
    
    return {
        'revenue_growth': revenue_growth,
        'cac': cac,
        'clv': clv,
        'clv_cac_ratio': clv_cac_ratio,
        'retention_rate': retention_rate,
        'churn_rate': churn_rate,
        'gross_margin': gross_margin,
        'total_revenue': total_revenue,
        'total_costs': total_costs,
        'active_customers': active_customers,
        'total_customers': total_customers
    }

# Main Dashboard
def main():
    st.title('📊 BizMetrics360 - KPI Intelligence Platform')
    st.markdown('*Simplified Financial & Operational Metrics Dashboard*')
    
    # Load data
    data = generate_sample_data()
    kpis = calculate_kpis(data)
    
    # Sidebar filters
    st.sidebar.header('🔧 Dashboard Controls')
    
    # Date range filter
    st.sidebar.subheader('📅 Date Range')
    date_range = st.sidebar.date_input(
        'Select Date Range',
        value=(datetime.now() - timedelta(days=30), datetime.now()),
        max_value=datetime.now()
    )
    
    # Region filter
    regions = ['All'] + list(data['revenue']['region'].unique())
    selected_region = st.sidebar.selectbox('🌍 Region', regions)
    
    # Main KPI Cards
    st.markdown('---')
    st.subheader('📈 Key Performance Indicators')
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label='💰 Revenue Growth',
            value=f'{kpis["revenue_growth"]:.1f}%',
            delta=f'{kpis["revenue_growth"] - 5:.1f}%'
        )
    
    with col2:
        st.metric(
            label='🎯 CLV:CAC Ratio',
            value=f'{kpis["clv_cac_ratio"]:.1f}x',
            delta=f'{kpis["clv_cac_ratio"] - 3:.1f}x'
        )
    
    with col3:
        st.metric(
            label='👥 Retention Rate',
            value=f'{kpis["retention_rate"]:.1f}%',
            delta=f'{kpis["retention_rate"] - 80:.1f}%'
        )
    
    with col4:
        st.metric(
            label='📊 Gross Margin',
            value=f'{kpis["gross_margin"]:.1f}%',
            delta=f'{kpis["gross_margin"] - 60:.1f}%'
        )
    
    # Charts Section
    st.markdown('---')
    st.subheader('📊 Performance Trends')
    
    # Revenue Trend
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('💰 Revenue Trend')
        revenue_trend = data['revenue'].groupby('date')['revenue'].sum().reset_index()
        fig_revenue = px.line(revenue_trend, x='date', y='revenue', 
                             title='Monthly Revenue Trend')
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        st.subheader('🎯 CAC vs CLV')
        fig_cac_clv = go.Figure()
        fig_cac_clv.add_trace(go.Bar(name='CAC', x=['Customer Acquisition Cost'], 
                                    y=[kpis['cac']], marker_color='red'))
        fig_cac_clv.add_trace(go.Bar(name='CLV', x=['Customer Lifetime Value'], 
                                    y=[kpis['clv']], marker_color='green'))
        fig_cac_clv.update_layout(title='CAC vs CLV Comparison')
        st.plotly_chart(fig_cac_clv, use_container_width=True)
    
    # Customer Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('👥 Customer Metrics')
        customer_metrics = pd.DataFrame({
            'Metric': ['Active Customers', 'Churned Customers'],
            'Count': [kpis['active_customers'], kpis['total_customers'] - kpis['active_customers']]
        })
        fig_customers = px.pie(customer_metrics, values='Count', names='Metric', 
                              title='Customer Status Distribution')
        st.plotly_chart(fig_customers, use_container_width=True)
    
    with col2:
        st.subheader('📈 Marketing ROI by Channel')
        channel_roi = data['marketing'].groupby('channel')['spend'].sum().reset_index()
        channel_roi['roi'] = np.random.uniform(2, 8, len(channel_roi))  # Sample ROI
        fig_roi = px.bar(channel_roi, x='channel', y='roi', 
                        title='Marketing ROI by Channel')
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # Detailed Metrics Table
    st.markdown('---')
    st.subheader('📋 Detailed Metrics')
    
    metrics_df = pd.DataFrame([
        ['Revenue Growth Rate', f'{kpis["revenue_growth"]:.1f}%'],
        ['Customer Acquisition Cost', f'${kpis["cac"]:,.0f}'],
        ['Customer Lifetime Value', f'${kpis["clv"]:,.0f}'],
        ['CLV:CAC Ratio', f'{kpis["clv_cac_ratio"]:.1f}x'],
        ['Retention Rate', f'{kpis["retention_rate"]:.1f}%'],
        ['Churn Rate', f'{kpis["churn_rate"]:.1f}%'],
        ['Gross Margin', f'{kpis["gross_margin"]:.1f}%'],
        ['Total Revenue', f'${kpis["total_revenue"]:,.0f}'],
        ['Total Costs', f'${kpis["total_costs"]:,.0f}'],
        ['Active Customers', f'{kpis["active_customers"]:,}']
    ], columns=['Metric', 'Value'])
    
    st.dataframe(metrics_df, use_container_width=True)
    
    # Footer
    st.markdown('---')
    st.markdown('*BizMetrics360 - Simplified KPI Intelligence Platform*')

if __name__ == '__main__':
    main()

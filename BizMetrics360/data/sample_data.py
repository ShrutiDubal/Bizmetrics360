"""
BizMetrics360 - Simple Data Generator
Creates sample CSV files for the simplified KPI dashboard
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def create_sample_csv_files():
    """Create sample CSV files for the dashboard"""
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    np.random.seed(42)
    
    # Generate dates
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='D')
    
    # 1. Revenue Data
    revenue_data = pd.DataFrame({
        'date': np.random.choice(dates, 1000),
        'revenue': np.random.uniform(1000, 10000, 1000),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
        'channel': np.random.choice(['Direct', 'Online', 'Partners'], 1000),
        'product_category': np.random.choice(['Software', 'Services', 'Hardware'], 1000)
    })
    revenue_data.to_csv('data/revenue.csv', index=False)
    
    # 2. Customer Data
    customer_data = pd.DataFrame({
        'customer_id': range(1, 1001),
        'total_spent': np.random.uniform(100, 5000, 1000),
        'purchase_count': np.random.randint(1, 20, 1000),
        'customer_lifespan_days': np.random.randint(30, 1095, 1000),
        'is_new_customer': np.random.choice([True, False], 1000, p=[0.3, 0.7]),
        'is_active': np.random.choice([True, False], 1000, p=[0.8, 0.2]),
        'churned': np.random.choice([True, False], 1000, p=[0.15, 0.85]),
        'region': np.random.choice(['North', 'South', 'East', 'West'], 1000),
        'signup_date': np.random.choice(dates, 1000)
    })
    customer_data.to_csv('data/customers.csv', index=False)
    
    # 3. Marketing Spend Data
    marketing_data = pd.DataFrame({
        'date': np.random.choice(dates, 500),
        'spend': np.random.uniform(100, 5000, 500),
        'channel': np.random.choice(['Google Ads', 'Facebook', 'LinkedIn', 'Email'], 500),
        'campaign': np.random.choice(['Brand Awareness', 'Lead Generation', 'Retargeting'], 500),
        'impressions': np.random.randint(1000, 100000, 500),
        'clicks': np.random.randint(10, 1000, 500)
    })
    marketing_data.to_csv('data/marketing.csv', index=False)
    
    # 4. Cost Data
    cost_data = pd.DataFrame({
        'date': np.random.choice(dates, 800),
        'cost': np.random.uniform(500, 8000, 800),
        'cost_type': np.random.choice(['COGS', 'Operating', 'Marketing', 'Admin'], 800),
        'department': np.random.choice(['Sales', 'Marketing', 'Engineering', 'Support'], 800)
    })
    cost_data.to_csv('data/costs.csv', index=False)
    
    print("✅ Sample CSV files created successfully!")
    print("📁 Files created in 'data/' directory:")
    print("   - revenue.csv")
    print("   - customers.csv") 
    print("   - marketing.csv")
    print("   - costs.csv")

if __name__ == '__main__':
    create_sample_csv_files()

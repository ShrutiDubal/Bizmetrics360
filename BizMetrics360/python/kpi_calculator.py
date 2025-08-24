# BizMetrics360 - KPI Calculator Module
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import logging

class KPICalculator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def calculate_revenue_growth_rate(self, revenue_data: pd.DataFrame, period: str = 'monthly') -> Dict[str, float]:
        try:
            revenue_data['date'] = pd.to_datetime(revenue_data['date'])
            revenue_data = revenue_data.sort_values('date')
            
            if period == 'monthly':
                revenue_data['period'] = revenue_data['date'].dt.to_period('M')
            elif period == 'quarterly':
                revenue_data['period'] = revenue_data['date'].dt.to_period('Q')
            else:
                revenue_data['period'] = revenue_data['date'].dt.to_period('Y')
            
            period_revenue = revenue_data.groupby('period')['revenue'].sum().reset_index()
            period_revenue['growth_rate'] = period_revenue['revenue'].pct_change() * 100
            
            latest = period_revenue.iloc[-1]
            previous = period_revenue.iloc[-2] if len(period_revenue) > 1 else latest
            
            return {
                'current_revenue': float(latest['revenue']),
                'previous_revenue': float(previous['revenue']),
                'growth_rate': float(latest['growth_rate']) if not pd.isna(latest['growth_rate']) else 0.0,
                'avg_growth_rate': float(period_revenue['growth_rate'].mean()) if len(period_revenue) > 1 else 0.0
            }
        except Exception as e:
            self.logger.error(f'Error calculating revenue growth rate: {e}')
            return {}
    
    def calculate_cac_clv_metrics(self, customer_data: pd.DataFrame, marketing_data: pd.DataFrame) -> Dict[str, float]:
        try:
            total_marketing_spend = marketing_data['spend'].sum()
            new_customers = len(customer_data[customer_data['is_new_customer'] == True])
            cac = total_marketing_spend / new_customers if new_customers > 0 else 0
            
            avg_order_value = customer_data['total_spent'].mean()
            avg_purchase_frequency = customer_data['purchase_count'].mean()
            avg_customer_lifespan = customer_data['customer_lifespan_days'].mean() / 365
            
            clv = avg_order_value * avg_purchase_frequency * avg_customer_lifespan
            clv_cac_ratio = clv / cac if cac > 0 else 0
            
            return {
                'cac': float(cac),
                'clv': float(clv),
                'clv_cac_ratio': float(clv_cac_ratio),
                'avg_order_value': float(avg_order_value),
                'avg_purchase_frequency': float(avg_purchase_frequency),
                'avg_customer_lifespan': float(avg_customer_lifespan),
                'total_marketing_spend': float(total_marketing_spend),
                'new_customers': int(new_customers)
            }
        except Exception as e:
            self.logger.error(f'Error calculating CAC/CLV metrics: {e}')
            return {}
    
    def calculate_retention_churn_metrics(self, customer_data: pd.DataFrame) -> Dict[str, float]:
        try:
            total_customers = len(customer_data)
            active_customers = len(customer_data[customer_data['is_active'] == True])
            retention_rate = (active_customers / total_customers) * 100 if total_customers > 0 else 0
            
            churned_customers = len(customer_data[customer_data['churned'] == True])
            churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0
            
            return {
                'retention_rate': float(retention_rate),
                'churn_rate': float(churn_rate),
                'total_customers': int(total_customers),
                'active_customers': int(active_customers),
                'churned_customers': int(churned_customers)
            }
        except Exception as e:
            self.logger.error(f'Error calculating retention/churn metrics: {e}')
            return {}
    
    def calculate_gross_margin(self, revenue_data: pd.DataFrame, cost_data: pd.DataFrame) -> Dict[str, float]:
        try:
            total_revenue = revenue_data['revenue'].sum()
            total_costs = cost_data['cost'].sum()
            
            gross_margin = ((total_revenue - total_costs) / total_revenue) * 100 if total_revenue > 0 else 0
            gross_profit = total_revenue - total_costs
            
            return {
                'gross_margin': float(gross_margin),
                'gross_profit': float(gross_profit),
                'total_revenue': float(total_revenue),
                'total_costs': float(total_costs)
            }
        except Exception as e:
            self.logger.error(f'Error calculating gross margin: {e}')
            return {}
    
    def calculate_roi_by_channel(self, marketing_data: pd.DataFrame, revenue_data: pd.DataFrame) -> Dict[str, Dict[str, float]]:
        try:
            roi_data = marketing_data.merge(revenue_data, on='channel', how='left')
            roi_data['roi'] = ((roi_data['revenue'] - roi_data['spend']) / roi_data['spend']) * 100
            roi_data['roas'] = roi_data['revenue'] / roi_data['spend']
            
            channel_metrics = {}
            for _, row in roi_data.iterrows():
                channel_metrics[row['channel']] = {
                    'spend': float(row['spend']),
                    'revenue': float(row['revenue']),
                    'roi': float(row['roi']),
                    'roas': float(row['roas']),
                    'profit': float(row['revenue'] - row['spend'])
                }
            
            total_spend = roi_data['spend'].sum()
            total_revenue = roi_data['revenue'].sum()
            overall_roi = ((total_revenue - total_spend) / total_spend) * 100 if total_spend > 0 else 0
            
            return {
                'channels': channel_metrics,
                'overall': {
                    'total_spend': float(total_spend),
                    'total_revenue': float(total_revenue),
                    'overall_roi': float(overall_roi),
                    'avg_roi': float(roi_data['roi'].mean())
                }
            }
        except Exception as e:
            self.logger.error(f'Error calculating ROI by channel: {e}')
            return {}
    
    def generate_kpi_report(self, data_dict: Dict[str, pd.DataFrame]) -> Dict[str, Dict[str, float]]:
        try:
            report = {}
            
            if 'revenue' in data_dict:
                report['revenue_growth'] = self.calculate_revenue_growth_rate(data_dict['revenue'])
            
            if 'customers' in data_dict and 'marketing' in data_dict:
                report['cac_clv'] = self.calculate_cac_clv_metrics(data_dict['customers'], data_dict['marketing'])
            
            if 'customers' in data_dict:
                report['retention_churn'] = self.calculate_retention_churn_metrics(data_dict['customers'])
            
            if 'revenue' in data_dict and 'costs' in data_dict:
                report['profitability'] = self.calculate_gross_margin(data_dict['revenue'], data_dict['costs'])
            
            if 'marketing' in data_dict and 'revenue' in data_dict:
                report['roi_channels'] = self.calculate_roi_by_channel(data_dict['marketing'], data_dict['revenue'])
            
            return report
        except Exception as e:
            self.logger.error(f'Error generating KPI report: {e}')
            return {}

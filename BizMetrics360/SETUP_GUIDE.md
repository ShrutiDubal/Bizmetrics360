# 🚀 BizMetrics360 Setup Guide

## Quick Start (3 Steps)

### Step 1: Install Python
Make sure you have Python 3.8+ installed on your system.

**Windows:**
- Download from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

**Mac/Linux:**
```bash
# Mac (using Homebrew)
brew install python

# Linux (Ubuntu/Debian)
sudo apt-get install python3 python3-pip
```

### Step 2: Download & Setup
1. Download or clone this repository
2. Open terminal/command prompt in the project folder
3. Run the setup:

**Windows:**
```bash
# Double-click this file or run in command prompt:
start_dashboard.bat
```

**Mac/Linux:**
```bash
python run_dashboard.py
```

### Step 3: Access Dashboard
- The dashboard will automatically open in your browser
- If not, go to: `http://localhost:8501`
- Press `Ctrl+C` in terminal to stop the dashboard

## 🎯 What You'll See

### Main Dashboard Features:
- **KPI Cards**: Revenue Growth, CLV:CAC Ratio, Retention Rate, Gross Margin
- **Interactive Charts**: Revenue trends, customer metrics, marketing ROI
- **Filters**: Date range and region selection
- **Detailed Metrics Table**: All KPIs in one place

### Sample Data Included:
- **Revenue Data**: 1,000+ revenue records with regions and channels
- **Customer Data**: 1,000+ customer profiles with spending patterns
- **Marketing Data**: 500+ marketing campaigns with ROI metrics
- **Cost Data**: 800+ cost records by department and type

## 🔧 Customization

### Replace Sample Data:
1. Prepare your CSV files with the same column structure
2. Replace files in the `data/` folder:
   - `revenue.csv`
   - `customers.csv`
   - `marketing.csv`
   - `costs.csv`

### Modify Dashboard:
1. Edit `app.py` to change calculations
2. Edit `config/dashboard_config.py` for settings
3. Edit `data/sample_data.py` to change data structure

## 📊 Understanding the KPIs

### Revenue Growth Rate
- **Formula**: (Current Month - Previous Month) / Previous Month × 100
- **Good**: >5% monthly growth
- **Action**: Track trends and identify growth drivers

### CLV:CAC Ratio
- **Formula**: Customer Lifetime Value / Customer Acquisition Cost
- **Good**: >3:1 ratio
- **Action**: Optimize marketing spend and customer retention

### Retention Rate
- **Formula**: (Active Customers / Total Customers) × 100
- **Good**: >80% retention
- **Action**: Improve customer experience and engagement

### Gross Margin
- **Formula**: (Revenue - Costs) / Revenue × 100
- **Good**: >60% margin
- **Action**: Optimize pricing and reduce costs

## 🛠️ Troubleshooting

### Common Issues:

**"Module not found" error:**
```bash
pip install -r requirements.txt
```

**Dashboard won't start:**
```bash
# Check if port 8501 is available
# Try a different port:
streamlit run app.py --server.port 8502
```

**Data not loading:**
```bash
# Regenerate sample data:
python data/sample_data.py
```

**Slow performance:**
- Reduce data size in `sample_data.py`
- Use smaller date ranges
- Close other applications

## 📈 Next Steps

### For Business Use:
1. **Connect Real Data**: Replace sample data with your actual business data
2. **Customize KPIs**: Add industry-specific metrics
3. **Set Up Alerts**: Configure threshold notifications
4. **Schedule Reports**: Set up automated reporting

### For Development:
1. **Add New Charts**: Create custom visualizations
2. **Integrate APIs**: Connect to external data sources
3. **Add Authentication**: Secure the dashboard
4. **Deploy**: Host on cloud platforms

## 📞 Support

- **Documentation**: Check the `README.md` file
- **Issues**: Create an issue in the repository
- **Customization**: Modify the configuration files

---

**🎉 You're all set!** Your BizMetrics360 dashboard is ready to provide insights into your business performance.

#!/usr/bin/env python3
"""
BizMetrics360 - Dashboard Launcher
Simple script to set up and run the KPI dashboard
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import pandas
        import plotly
        import numpy
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required packages"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def generate_sample_data():
    """Generate sample data if it doesn't exist"""
    if not os.path.exists("data/revenue.csv"):
        print("📊 Generating sample data...")
        try:
            subprocess.check_call([sys.executable, "data/sample_data.py"])
            print("✅ Sample data generated!")
        except subprocess.CalledProcessError:
            print("❌ Failed to generate sample data")
            return False
    else:
        print("✅ Sample data already exists")
    return True

def run_dashboard():
    """Run the Streamlit dashboard"""
    print("🚀 Starting BizMetrics360 Dashboard...")
    print("📱 Dashboard will open in your browser at http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the dashboard")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped. Goodbye!")

def main():
    """Main launcher function"""
    print("🎯 BizMetrics360 - KPI Intelligence Platform")
    print("=" * 50)
    
    # Check and install dependencies
    if not check_dependencies():
        if not install_dependencies():
            print("❌ Cannot proceed without dependencies")
            return
    
    # Generate sample data
    if not generate_sample_data():
        print("❌ Cannot proceed without sample data")
        return
    
    # Run dashboard
    run_dashboard()

if __name__ == "__main__":
    main()

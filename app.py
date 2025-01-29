# app.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from utils import *
from constants import *
from investment_strategies import *
from tax_calculator import *
from retirement_projections import *

# Page configuration
st.set_page_config(
    page_title="Federal TSP Calculator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

def show_education_section():
    """Enhanced educational information about the TSP calculator"""
    with st.expander("📚 Learn About TSP Calculator", expanded=True):
        st.markdown("""
        ### What is TSP?
        The Thrift Savings Plan (TSP) is a retirement savings and investment plan for Federal employees and uniformed services members.
        
        ### Investment Approaches:
        1. **Conservative (Low Risk)**
           - Higher allocation to G and F Funds
           - Suitable for near-retirement or risk-averse investors
           - Typical returns: 2-4% annually
        
        2. **Moderate (Balanced Risk)**
           - Balanced mix of all funds
           - Suitable for mid-career professionals
           - Typical returns: 5-8% annually
        
        3. **Aggressive (Higher Risk)**
           - Higher allocation to C, S, and I Funds
           - Suitable for young investors with long horizons
           - Potential returns: 8-12% annually
        
        ### Tax Implications:
        - **Traditional TSP**: Contributions reduce current taxable income
        - **Roth TSP**: After-tax contributions, tax-free withdrawals
        - **RMD Considerations**: Required starting at age 73
        
        ### Historical Performance Analysis:
        - Past performance tracking since inception
        - Risk-adjusted return metrics
        - Volatility analysis
        
        ### Retirement Income Projections:
        - Monte Carlo simulations
        - Multiple scenario analysis
        - Inflation-adjusted projections
        """)

def show_risk_tolerance_selector():
    """Allow users to select their investment approach based on risk tolerance"""
    risk_profile = st.sidebar.selectbox(
        "Select Your Risk Tolerance",
        ["Conservative", "Moderate", "Aggressive"],
        help="Choose your investment approach based on your risk tolerance"
    )
    
    if risk_profile == "Conservative":
        st.sidebar.markdown("""
        📊 **Conservative Allocation**:
        - G Fund: 40%
        - F Fund: 30%
        - C Fund: 20%
        - S Fund: 5%
        - I Fund: 5%
        """)
    elif risk_profile == "Moderate":
        st.sidebar.markdown("""
        📊 **Moderate Allocation**:
        - G Fund: 20%
        - F Fund: 20%
        - C Fund: 30%
        - S Fund: 15%
        - I Fund: 15%
        """)
    else:
        st.sidebar.markdown("""
        📊 **Aggressive Allocation**:
        - G Fund: 5%
        - F Fund: 10%
        - C Fund: 45%
        - S Fund: 20%
        - I Fund: 20%
        """)
    
    return risk_profile

def main():
    st.title("Enhanced Federal TSP Calculator")
    
    # Show educational section
    show_education_section()
    
    # Risk tolerance selector in sidebar
    risk_profile = show_risk_tolerance_selector()
    
    # Initialize session state
    initialize_session_state()
    
    # Create main tabs
    tabs = st.tabs([
        "Personal Info",
        "Contributions",
        "Fund Analysis",
        "Tax Planning",
        "Retirement Projections"
    ])
    
    # Personal Information Tab
    with tabs[0]:
        handle_personal_info_tab()
    
    # Contributions Tab
    with tabs[1]:
        handle_contributions_tab()
    
    # Fund Analysis Tab
    with tabs[2]:
        handle_fund_analysis_tab(risk_profile)
    
    # Tax Planning Tab
    with tabs[3]:
        handle_tax_planning_tab()
    
    # Retirement Projections Tab
    with tabs[4]:
        handle_retirement_projections_tab()

if __name__ == "__main__":
    main()

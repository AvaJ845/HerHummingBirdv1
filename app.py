# app.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from utils import (
    initialize_session_state,
    handle_personal_info_tab,
    handle_contributions_tab,
    handle_fund_analysis_tab,
    handle_tax_planning_tab,
    handle_retirement_projections_tab
)
from config import (
    CURRENT_USER, 
    CURRENT_TIMESTAMP, 
    COMPANY_NAME, 
    COMPANY_FOOTER,
    APP_VERSION
)
from constants import RISK_PROFILES, FUND_PERFORMANCE

# Custom CSS for styling
st.set_page_config(
    page_title="Federal TSP Calculator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for footer
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #31333F;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .header-info {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .user-info {
        float: right;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def show_header_info():
    """Display header with current user and timestamp information"""
    header_html = f"""
    <div class="header-info">
        <span>🕒 2025-01-29 22:54:08 UTC</span>
        <span class="user-info">👤 User: AvaJ845</span>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def show_footer():
    """Display footer with company information"""
    footer_html = f"""
    <div class="footer">
        <span>{COMPANY_FOOTER}</span>
        <span style="margin-left: 20px;">Version {APP_VERSION}</span>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def main():
    try:
        # Show header information
        show_header_info()
        
        st.title("Enhanced Federal TSP Calculator")
        
        # Show how to use section
        show_how_to_use()
        
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
        
        # Handle each tab
        with tabs[0]: handle_personal_info_tab()
        with tabs[1]: handle_contributions_tab()
        with tabs[2]: handle_fund_analysis_tab(risk_profile)
        with tabs[3]: handle_tax_planning_tab()
        with tabs[4]: handle_retirement_projections_tab()
        
        # Add footer
        show_footer()
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please try refreshing the page or contact support if the error persists.")
        st.exception(e)

def show_how_to_use():
    """Display instructions on how to use the TSP calculator"""
    with st.expander("🔍 How to Use This Tool", expanded=True):
        st.markdown("""
        ### Quick Start Guide
        
        #### 1. Personal Information Setup
        - Navigate to the "Personal Info" tab
        - Enter your age, salary, and years of service
        - Select your retirement system (FERS or CSRS)
        - Indicate if you're a special category employee
        
        #### 2. Choose Your Risk Profile
        - Use the sidebar to select your risk tolerance:
            * Conservative: Near retirement or risk-averse
            * Moderate: Mid-career balanced approach
            * Aggressive: Early career, longer investment horizon
        
        #### 3. Set Your Contributions
        - Go to the "Contributions" tab
        - Enter your Traditional and Roth contribution percentages
        - View the calculated annual contributions
        - Check agency matching calculations
        
        #### 4. Analyze Your Portfolio
        - Visit the "Fund Analysis" tab to:
            * View fund allocations based on your risk profile
            * Check historical performance
            * Understand risk metrics
        
        #### 5. Tax Planning
        - Use the "Tax Planning" tab to:
            * Calculate tax savings from Traditional contributions
            * Project Required Minimum Distributions (RMDs)
            * Compare Traditional vs. Roth benefits
        
        #### 6. Review Retirement Projections
        - In the "Retirement Projections" tab:
            * View retirement income scenarios
            * Check Monte Carlo simulation results
            * Adjust variables to see different outcomes
        """)

if __name__ == "__main__":
    main()

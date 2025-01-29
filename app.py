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
from config import CURRENT_USER, CURRENT_TIMESTAMP
from constants import RISK_PROFILES, FUND_PERFORMANCE

# Page configuration
st.set_page_config(
    page_title="Federal TSP Calculator",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        
        ### Tips for Best Results
        1. **Keep Information Updated**: Regularly update your salary and contributions
        2. **Review Risk Tolerance**: Reassess your risk profile annually
        3. **Check Tax Implications**: Consider tax brackets when choosing Traditional vs. Roth
        4. **Monitor Performance**: Review fund performance quarterly
        
        ### Need Help?
        - Use the '?' icons next to inputs for detailed explanations
        - Check the educational section for in-depth TSP information
        - Contact your agency's TSP coordinator for specific questions
        """)

def show_education_section():
    """Enhanced educational information about the TSP calculator"""
    with st.expander("📚 Learn About TSP Calculator", expanded=False):
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
        list(RISK_PROFILES.keys()),
        help="Choose your investment approach based on your risk tolerance"
    )
    
    # Display allocation from RISK_PROFILES constant
    st.sidebar.markdown(f"📊 **{risk_profile} Portfolio**")
    st.sidebar.markdown(RISK_PROFILES[risk_profile]['description'])
    
    allocations = RISK_PROFILES[risk_profile]['allocations']
    for fund, allocation in allocations.items():
        st.sidebar.markdown(f"- {fund}: {allocation}%")
    
    return risk_profile

def main():
    try:
        st.title("Enhanced Federal TSP Calculator")
        st.caption(f"Current User: {CURRENT_USER} | Last Updated: 2025-01-29 22:46:10")
        
        # Show how to use section first
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
        with tabs[0]: 
            handle_personal_info_tab()
        
        with tabs[1]: 
            handle_contributions_tab()
        
        with tabs[2]: 
            handle_fund_analysis_tab(risk_profile)
        
        with tabs[3]: 
            handle_tax_planning_tab()
        
        with tabs[4]: 
            handle_retirement_projections_tab()
        
        # Add footer
        st.markdown("---")
        st.caption(f"Data last refreshed: 2025-01-29 22:46:10 UTC")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please try refreshing the page or contact support if the error persists.")
        st.exception(e)

if __name__ == "__main__":
    main()

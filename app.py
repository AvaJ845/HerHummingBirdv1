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

# Custom CSS for styling
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
        <span>🕒 2025-01-29 23:17:46 UTC</span>
        <span class="user-info">👤 User: AvaJ845</span>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

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

def show_footer():
    """Display footer with copyright information"""
    footer_html = """
    <div class="footer">
        <p>© 2025 AvaResearch LLC. All rights reserved.</p>
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

if __name__ == "__main__":
    main()

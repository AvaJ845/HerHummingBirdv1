#appy.py
import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
from utils import (
    calculate_retirement_age,
    calculate_rmd,
    calculate_tax_implications,
    validate_inputs,
    mask_sensitive_data
)
from constants import (
    CURRENT_YEAR,
    ANNUAL_LIMIT,
    CATCH_UP_LIMIT,
    FUND_PERFORMANCE,
    TAX_BRACKETS
)

# Page configuration
st.set_page_config(
    page_title="Federal TSP Calculator",
    page_icon="💰",
    layout="wide"
)

def show_education_section():
    """Display educational information about the TSP calculator"""
    with st.expander("📚 Learn About TSP Calculator", expanded=True):
        st.markdown("""
        ### What is TSP?
        The Thrift Savings Plan (TSP) is a retirement savings and investment plan for Federal employees and members of the uniformed services.
        
        ### Key Features:
        - **Traditional & Roth Contributions**: Choose between pre-tax or after-tax contributions
        - **Agency Matching**: Government matches up to 5% of your contributions
        - **Multiple Fund Options**: Diverse investment choices from G Fund to Lifecycle Funds
        
        ### How to Use This Calculator:
        1. Enter your personal information
        2. Set your contribution preferences
        3. Choose your fund allocations
        4. Review retirement projections
        
        ### Security Features:
        - All sensitive inputs are masked
        - Data is not stored permanently
        - Secure input validation
        """)

def main():
    st.title("Federal TSP Calculator")
    
    # Show educational section at the top
    show_education_section()
    
    # Initialize session state
    if 'personal_info' not in st.session_state:
        st.session_state.personal_info = {
            'age': '',
            'salary': '',
            'years_of_service': '',
            'retirement_system': 'FERS',
            'is_special_category': False,
            'state_of_residence': '',
            'tax_bracket': '',
            'filing_status': 'single'
        }
    
    # Create tabs
    tabs = st.tabs(["Personal Info", "Contributions", "Fund Analysis", "Retirement"])
    
    # Personal Information Tab
    with tabs[0]:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Basic Information")
            try:
                # Masked input fields
                age = st.number_input(
                    "Age",
                    min_value=18,
                    max_value=100,
                    value=int(st.session_state.personal_info['age']) if st.session_state.personal_info['age'] else 18,
                    help="Enter your current age"
                )
                
                salary = st.text_input(
                    "Annual Salary",
                    type="password",
                    value=st.session_state.personal_info['salary'],
                    help="Enter your annual salary"
                )
                
                years_of_service = st.number_input(
                    "Years of Service",
                    min_value=0,
                    max_value=60,
                    value=int(st.session_state.personal_info['years_of_service']) if st.session_state.personal_info['years_of_service'] else 0,
                    help="Enter your years of federal service"
                )
                
                # Validate inputs
                if salary:
                    try:
                        salary = float(mask_sensitive_data(salary))
                        if salary < 0:
                            st.error("Salary cannot be negative")
                    except ValueError:
                        st.error("Please enter a valid salary amount")
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                
        with col2:
            st.subheader("Retirement System")
            retirement_system = st.selectbox(
                "System",
                options=["FERS", "CSRS"],
                index=0 if st.session_state.personal_info['retirement_system'] == 'FERS' else 1
            )
            
            is_special_category = st.checkbox(
                "Special Category Employee",
                value=st.session_state.personal_info['is_special_category'],
                help="Check if you are a law enforcement officer, firefighter, or air traffic controller"
            )

    # Update session state
    st.session_state.personal_info.update({
        'age': age,
        'salary': salary,
        'years_of_service': years_of_service,
        'retirement_system': retirement_system,
        'is_special_category': is_special_category
    })

if __name__ == "__main__":
    main()

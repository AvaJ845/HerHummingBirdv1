#utils.py
# utils.py
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.graph_objects as go
from constants import CURRENT_USER, CURRENT_TIMESTAMP, FUND_PERFORMANCE, TAX_BRACKETS

def initialize_session_state():
    """Initialize session state with default values"""
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

def handle_personal_info_tab():
    """Handle the personal information tab content"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Information")
        age = st.number_input("Age", min_value=18, max_value=100, 
                            value=30 if not st.session_state.personal_info['age'] else 
                            int(st.session_state.personal_info['age']))
        
        salary = st.number_input("Annual Salary ($)", min_value=0, max_value=1000000,
                               value=50000 if not st.session_state.personal_info['salary'] else 
                               int(st.session_state.personal_info['salary']))
        
        years_of_service = st.number_input("Years of Service", min_value=0, max_value=60,
                                         value=0 if not st.session_state.personal_info['years_of_service'] else 
                                         int(st.session_state.personal_info['years_of_service']))

    with col2:
        st.subheader("Retirement System")
        retirement_system = st.selectbox("System", ["FERS", "CSRS"])
        is_special_category = st.checkbox("Special Category Employee")
        filing_status = st.selectbox("Filing Status", ["single", "married"])

    # Update session state
    st.session_state.personal_info.update({
        'age': age,
        'salary': salary,
        'years_of_service': years_of_service,
        'retirement_system': retirement_system,
        'is_special_category': is_special_category,
        'filing_status': filing_status
    })

def handle_contributions_tab():
    """Handle the contributions tab content"""
    st.subheader("TSP Contributions")
    
    col1, col2 = st.columns(2)
    with col1:
        traditional_contrib = st.number_input(
            "Traditional TSP Contribution (%)",
            min_value=0,
            max_value=100,
            value=5
        )
        
        roth_contrib = st.number_input(
            "Roth TSP Contribution (%)",
            min_value=0,
            max_value=100,
            value=0
        )
        
    with col2:
        salary = st.session_state.personal_info.get('salary', 0)
        total_contrib_percent = traditional_contrib + roth_contrib
        
        if total_contrib_percent > 100:
            st.error("Total contributions cannot exceed 100%")
        else:
            traditional_amount = (salary * traditional_contrib / 100)
            roth_amount = (salary * roth_contrib / 100)
            
            st.write(f"Traditional Contribution: ${traditional_amount:,.2f}")
            st.write(f"Roth Contribution: ${roth_amount:,.2f}")
            st.write(f"Total Contribution: ${(traditional_amount + roth_amount):,.2f}")

def handle_fund_analysis_tab(risk_profile):
    """Handle the fund analysis tab content"""
    st.subheader("Fund Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Current Allocation")
        fig = go.Figure(data=[go.Pie(
            labels=list(FUND_PERFORMANCE.keys()),
            values=[FUND_PERFORMANCE[fund]['return'] for fund in FUND_PERFORMANCE.keys()]
        )])
        st.plotly_chart(fig)
        
    with col2:
        st.write("### Fund Performance")
        df = pd.DataFrame(FUND_PERFORMANCE).transpose()
        st.dataframe(df)

def handle_tax_planning_tab():
    """Handle the tax planning tab content"""
    st.subheader("Tax Planning")
    
    salary = st.session_state.personal_info.get('salary', 0)
    filing_status = st.session_state.personal_info.get('filing_status', 'single')
    
    # Find applicable tax bracket
    tax_rate = next((bracket['rate'] for bracket in TAX_BRACKETS 
                    if salary <= bracket[filing_status]), 0.37)
    
    st.write(f"Current Tax Bracket: {tax_rate:.1%}")
    st.write(f"Estimated Tax Savings on Traditional Contributions: "
            f"${(salary * tax_rate):,.2f}")

def handle_retirement_projections_tab():
    """Handle the retirement projections tab content"""
    st.subheader("Retirement Projections")
    
    # Get current age and retirement age
    current_age = st.session_state.personal_info.get('age', 30)
    retirement_age = st.number_input("Expected Retirement Age", 
                                   min_value=current_age,
                                   max_value=100,
                                   value=min(current_age + 30, 65))
    
    # Simple projection
    years_to_retirement = retirement_age - current_age
    current_salary = st.session_state.personal_info.get('salary', 50000)
    
    conservative_growth = current_salary * (1.03 ** years_to_retirement)
    moderate_growth = current_salary * (1.06 ** years_to_retirement)
    aggressive_growth = current_salary * (1.09 ** years_to_retirement)
    
    st.write("### Projected Retirement Account Balance")
    st.write(f"Conservative Estimate: ${conservative_growth:,.2f}")
    st.write(f"Moderate Estimate: ${moderate_growth:,.2f}")
    st.write(f"Aggressive Estimate: ${aggressive_growth:,.2f}")

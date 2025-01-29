#utils.py
import streamlit as st
from typing import Union, Dict
import re

def mask_sensitive_data(data: str) -> str:
    """Mask sensitive data while preserving the actual value in session state"""
    if not data:
        return ""
    return re.sub(r'\d', '*', str(data))

def validate_inputs(data: Dict) -> tuple[bool, str]:
    """Validate user inputs"""
    try:
        if float(data['age']) < 18:
            return False, "Age must be at least 18"
        if float(data['salary']) < 0:
            return False, "Salary cannot be negative"
        if float(data['years_of_service']) < 0:
            return False, "Years of service cannot be negative"
        return True, ""
    except ValueError:
        return False, "Please enter valid numeric values"
    except Exception as e:
        return False, f"Validation error: {str(e)}"

def calculate_retirement_age(age: int, years_of_service: int, retirement_system: str, is_special_category: bool) -> int:
    """Calculate retirement age based on provided parameters"""
    try:
        if retirement_system == 'FERS':
            if is_special_category:
                return min(57, age + (20 - years_of_service))
            birth_year = 2024 - age  # Using current year
            if birth_year < 1948:
                return 55
            if birth_year > 1969:
                return 57
            return 55 + min(2, (birth_year - 1947) * 0.166667)
        else:  # CSRS
            if is_special_category:
                return min(55, age + (20 - years_of_service))
            return min(62, age + (30 - years_of_service))
    except Exception as e:
        st.error(f"Error calculating retirement age: {str(e)}")
        return 0

def calculate_rmd(age: int, balance: float) -> float:
    """Calculate Required Minimum Distribution"""
    try:
        if age < 73:
            return 0
        distribution_periods = {
            73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7,
            77: 22.9, 78: 22.0, 79: 21.1, 80: 20.2
        }
        period = distribution_periods.get(age, 20.2)
        return balance / period
    except Exception as e:
        st.error(f"Error calculating RMD: {str(e)}")
        return 0

def calculate_tax_implications(salary: float, filing_status: str, contributions: Dict) -> Dict:
    """Calculate tax implications of TSP contributions"""
    try:
        from constants import TAX_BRACKETS
        marginal_rate = next((bracket['rate'] for bracket in TAX_BRACKETS 
                            if salary <= bracket[filing_status]), 0.37)
        
        return {
            'traditional_savings': contributions['traditional'] * marginal_rate,
            'roth_tax_paid': contributions['roth'],
            'projected_rmd': calculate_rmd(73, contributions['traditional_balance']),
            'projected_tax_rate': marginal_rate
        }
    except Exception as e:
        st.error(f"Error calculating tax implications: {str(e)}")
        return {}

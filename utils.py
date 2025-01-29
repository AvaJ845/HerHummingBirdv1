#utils.py
import streamlit as st
import pandas as pd
import numpy as np
from typing import Dict
from constants import RISK_PROFILES, FUND_PERFORMANCE, HISTORICAL_PERFORMANCE, RMD_FACTORS

def calculate_portfolio_returns(allocations: Dict, investment_amount: float) -> Dict:
    """Calculate expected returns based on fund allocations"""
    total_return = 0
    portfolio_risk = 0
    
    for fund, percentage in allocations.items():
        if percentage > 0:
            return_rate = FUND_PERFORMANCE[fund]['return'] / 100
            total_return += (return_rate * percentage / 100)
            portfolio_risk += (FUND_PERFORMANCE[fund]['volatility'] * percentage / 100)
    
    expected_value = investment_amount * (1 + total_return)
    
    return {
        'expected_return': total_return * 100,
        'portfolio_risk': portfolio_risk,
        'expected_value': expected_value
    }

def project_retirement_income(
    current_balance: float,
    monthly_contribution: float,
    years_to_retirement: int,
    risk_profile: str
) -> Dict:
    """Project retirement income based on contributions and risk profile"""
    allocations = RISK_PROFILES[risk_profile]['allocations']
    annual_return = sum(FUND_PERFORMANCE[fund]['return'] * (alloc/100) 
                       for fund, alloc in allocations.items())
    
    # Monthly calculations
    months = years_to_retirement * 12
    monthly_return = (1 + annual_return/100)**(1/12) - 1
    
    # Future Value calculation with monthly contributions
    future_value = current_balance * (1 + monthly_return)**months
    future_value += monthly_contribution * (((1 + monthly_return)**months - 1) / monthly_return)
    
    # Calculate estimated monthly retirement income (4% rule)
    monthly_retirement_income = future_value * 0.04 / 12
    
    return {
        'projected_balance': future_value,
        'monthly_retirement_income': monthly_retirement_income,
        'annual_return_rate': annual_return
    }

def calculate_detailed_rmd(age: int, traditional_balance: float) -> Dict:
    """Calculate detailed RMD projections"""
    if age < 72:
        years_to_rmd = 72 - age
        projected_balance = traditional_balance * (1.07 ** years_to_rmd)  # Assuming 7% annual growth
    else:
        projected_balance = traditional_balance
    
    rmd_projections = {}
    current_balance = projected_balance
    
    for projection_age in range(max(72, age), 101):
        if projection_age in RMD_FACTORS:
            rmd_amount = current_balance / RMD_FACTORS[projection_age]
            rmd_projections[projection_age] = {
                'balance': current_balance,
                'rmd_amount': rmd_amount,
                'factor': RMD_FACTORS[projection_age]
            }
            current_balance = (current_balance - rmd_amount) * 1.07  # Assuming 7% growth
    
    return rmd_projections

def analyze_tax_implications(
    traditional_contributions: float,
    roth_contributions: float,
    current_tax_rate: float,
    estimated_retirement_tax_rate: float
) -> Dict:
    """Analyze tax implications of Traditional vs Roth contributions"""
    current_tax_savings = traditional_contributions * current_tax_rate
    retirement_tax_cost = traditional_contributions * estimated_retirement_tax_rate
    roth_current_tax_cost = roth_contributions * current_tax_rate
    
    return {
        'current_tax_savings': current_tax_savings,
        'retirement_tax_cost': retirement_tax_cost,
        'roth_current_tax_cost': roth_current_tax_cost,
        'tax_difference': current_tax_savings - retirement_tax_cost
    }

def get_risk_profile_recommendation(age: int, years_to_retirement: int) -> str:
    """Recommend a risk profile based on age and years to retirement"""
    if years_to_retirement < 5:
        return 'Conservative'
    elif years_to_retirement < 15:
        return 'Moderate'
    else:
        return 'Aggressive'

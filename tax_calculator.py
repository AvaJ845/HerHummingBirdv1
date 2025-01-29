#tax_calculator.py
import pandas as pd
from constants import TAX_BRACKETS

def calculate_tax_savings(contributions, income, filing_status):
    """Calculate tax savings from traditional contributions"""
    marginal_rate = get_marginal_tax_rate(income, filing_status)
    return contributions * marginal_rate

def calculate_rmd_projections(age, balance, life_expectancy=90):
    """Project Required Minimum Distributions"""
    if age < 73:
        return pd.DataFrame()
    
    years = range(age, life_expectancy + 1)
    rmd_factors = {
        73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7,
        77: 22.9, 78: 22.0, 79: 21.1, 80: 20.2
    }
    
    rmds = []
    remaining_balance = balance
    
    for year in years:
        factor = rmd_factors.get(year, 20.2)
        rmd = remaining_balance / factor
        rmds.append({
            'age': year,
            'rmd_amount': rmd,
            'remaining_balance': remaining_balance - rmd
        })
        remaining_balance -= rmd
    
    return pd.DataFrame(rmds)

def get_marginal_tax_rate(income, filing_status):
    """Get the marginal tax rate based on income and filing status"""
    for bracket in TAX_BRACKETS:
        if income <= bracket[filing_status]:
            return bracket['rate']
    return TAX_BRACKETS[-1]['rate']

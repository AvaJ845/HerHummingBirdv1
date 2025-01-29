#investment_strategies.py
import pandas as pd
import numpy as np

INVESTMENT_ALLOCATIONS = {
    "Conservative": {
        "G_Fund": 0.40,
        "F_Fund": 0.30,
        "C_Fund": 0.20,
        "S_Fund": 0.05,
        "I_Fund": 0.05
    },
    "Moderate": {
        "G_Fund": 0.20,
        "F_Fund": 0.20,
        "C_Fund": 0.30,
        "S_Fund": 0.15,
        "I_Fund": 0.15
    },
    "Aggressive": {
        "G_Fund": 0.05,
        "F_Fund": 0.10,
        "C_Fund": 0.45,
        "S_Fund": 0.20,
        "I_Fund": 0.20
    }
}

def calculate_portfolio_metrics(risk_profile):
    """Calculate expected return and risk metrics based on risk profile"""
    allocation = INVESTMENT_ALLOCATIONS[risk_profile]
    
    # Historical returns and volatility
    fund_metrics = {
        "G_Fund": {"return": 0.02, "volatility": 0.01},
        "F_Fund": {"return": 0.035, "volatility": 0.04},
        "C_Fund": {"return": 0.10, "volatility": 0.15},
        "S_Fund": {"return": 0.11, "volatility": 0.18},
        "I_Fund": {"return": 0.09, "volatility": 0.17}
    }
    
    expected_return = sum(allocation[fund] * fund_metrics[fund]["return"] 
                         for fund in allocation)
    
    portfolio_volatility = np.sqrt(sum(
        (allocation[fund] * fund_metrics[fund]["volatility"])**2 
        for fund in allocation
    ))
    
    return {
        "expected_return": expected_return,
        "volatility": portfolio_volatility,
        "sharpe_ratio": (expected_return - 0.02) / portfolio_volatility  # Assuming 2% risk-free rate
    }

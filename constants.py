#constants.py
from datetime import datetime

CURRENT_YEAR = datetime.now().year
ANNUAL_LIMIT = 23000
CATCH_UP_LIMIT = 7500

FUND_PERFORMANCE = {
    'gFund': {'return': 2.35, 'risk': 'Very Low', 'volatility': 0.5},
    'fFund': {'return': 3.45, 'risk': 'Low', 'volatility': 4.8},
    'cFund': {'return': 11.82, 'risk': 'Moderate', 'volatility': 15.2},
    'sFund': {'return': 10.54, 'risk': 'High', 'volatility': 17.5},
    'iFund': {'return': 7.26, 'risk': 'High', 'volatility': 16.8}
}

TAX_BRACKETS = [
    {'rate': 0.10, 'single': 11600, 'married': 23200},
    {'rate': 0.12, 'single': 47150, 'married': 94300},
    {'rate': 0.22, 'single': 100525, 'married': 201050},
    {'rate': 0.24, 'single': 191950, 'married': 383900},
    {'rate': 0.32, 'single': 243725, 'married': 487450},
    {'rate': 0.35, 'single': 609350, 'married': 731200},
    {'rate': 0.37, 'single': float('inf'), 'married': float('inf')}
]

L_FUNDS = [
    'lIncome', 'l2025', 'l2030', 'l2035', 'l2040',
    'l2045', 'l2050', 'l2055', 'l2060', 'l2065'
]

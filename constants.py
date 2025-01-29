#constants.py
from datetime import datetime

CURRENT_TIMESTAMP = "2025-01-29 22:33:05"
CURRENT_USER = "AvaJ845"
CURRENT_YEAR = 2025
ANNUAL_LIMIT = 23000
CATCH_UP_LIMIT = 7500

from datetime import datetime

# Risk-adjusted return metrics
RISK_METRICS = {
    "Conservative": {
        "expected_return": 0.04,
        "volatility": 0.05,
        "max_drawdown": 0.10
    },
    "Moderate": {
        "expected_return": 0.07,
        "volatility": 0.12,
        "max_drawdown": 0.20
    },
    "Aggressive": {
        "expected_return": 0.09,
        "volatility": 0.18,
        "max_drawdown": 0.35
    }
}

# Historical fund performance data
HISTORICAL_PERFORMANCE = {
    # Add historical performance data...
}
# Risk-based portfolio allocations
RISK_PROFILES = {
    'Conservative': {
        'description': 'Lower risk, stable returns, suitable for near-retirement',
        'allocations': {
            'gFund': 40,
            'fFund': 25,
            'cFund': 20,
            'sFund': 10,
            'iFund': 5
        }
    },
    'Moderate': {
        'description': 'Balanced risk and returns, suitable for mid-career',
        'allocations': {
            'gFund': 20,
            'fFund': 20,
            'cFund': 35,
            'sFund': 15,
            'iFund': 10
        }
    },
    'Aggressive': {
        'description': 'Higher risk, higher potential returns, suitable for early career',
        'allocations': {
            'gFund': 5,
            'fFund': 10,
            'cFund': 45,
            'sFund': 25,
            'iFund': 15
        }
    }
}

FUND_PERFORMANCE = {
    'gFund': {
        'return': 2.35,
        'risk': 'Very Low',
        'volatility': 0.5,
        'description': 'Government Securities Investment Fund - Invested in short-term U.S. Treasury securities'
    },
    'fFund': {
        'return': 3.45,
        'risk': 'Low',
        'volatility': 4.8,
        'description': 'Fixed Income Index Investment Fund - Tracks U.S. bond market'
    },
    'cFund': {
        'return': 11.82,
        'risk': 'Moderate',
        'volatility': 15.2,
        'description': 'Common Stock Index Investment Fund - Tracks S&P 500'
    },
    'sFund': {
        'return': 10.54,
        'risk': 'High',
        'volatility': 17.5,
        'description': 'Small Cap Stock Index Investment Fund - Tracks smaller U.S. companies'
    },
    'iFund': {
        'return': 7.26,
        'risk': 'High',
        'volatility': 16.8,
        'description': 'International Stock Index Investment Fund - Tracks international stocks'
    }
}

# Historical performance (10-year average returns)
HISTORICAL_PERFORMANCE = {
    'gFund': [2.1, 2.3, 2.4, 2.35, 2.4, 2.2, 2.3, 2.4, 2.35, 2.35],
    'fFund': [3.2, 3.4, 3.5, 3.3, 3.6, 3.4, 3.5, 3.4, 3.45, 3.45],
    'cFund': [10.5, 11.2, 11.5, 11.8, 12.0, 11.5, 11.8, 11.9, 11.82, 11.82],
    'sFund': [9.8, 10.2, 10.4, 10.5, 10.6, 10.3, 10.5, 10.6, 10.54, 10.54],
    'iFund': [6.8, 7.0, 7.2, 7.3, 7.4, 7.1, 7.2, 7.3, 7.26, 7.26]
}

# RMD Factors
RMD_FACTORS = {
    72: 27.4, 73: 26.5, 74: 25.5, 75: 24.6, 76: 23.7, 77: 22.9,
    78: 22.0, 79: 21.1, 80: 20.2, 81: 19.4, 82: 18.5, 83: 17.7,
    84: 16.8, 85: 16.0, 86: 15.2, 87: 14.4, 88: 13.7, 89: 12.9,
    90: 12.2, 91: 11.5, 92: 10.8, 93: 10.1, 94: 9.5, 95: 8.9,
    96: 8.4, 97: 7.8, 98: 7.3, 99: 6.8, 100: 6.4
}

#config.py
# Current timestamp
CURRENT_TIMESTAMP = "2025-01-29 23:27:58"  # UTC time in YYYY-MM-DD HH:MM:SS format


# Company information
COMPANY_NAME = "AvaResearch LLC"
COMPANY_FOOTER = f"© 2025 {COMPANY_NAME}. All rights reserved."
APP_VERSION = "1.0.0"

# Application settings
DEBUG_MODE = False
ENABLE_LOGGING = True

# Feature flags
ENABLE_MONTE_CARLO = True
ENABLE_HISTORICAL_ANALYSIS = True
ENABLE_TAX_CALCULATOR = True

# Cache settings
CACHE_TIMEOUT = 3600  # 1 hour in seconds
MAX_CACHE_SIZE = 1000  # Maximum number of cached items

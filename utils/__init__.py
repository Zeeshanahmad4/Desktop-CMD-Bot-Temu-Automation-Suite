# __init__.py for the utils package
"""
The utils package contains common utilities and helper functions used across the Temu Automation Suite.
This includes functions for API session setup, configuration loading, and logging setups.
"""

import logging

# Configure logging for the entire application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import shared utilities to be used across the project
from .api_utils import setup_api_session, make_api_request
from .config_utils import load_configuration

# Optionally initialize shared resources here
def initialize_shared_resources():
    """Initialize shared resources and configurations."""
    logging.info("Initializing shared resources for the Temu Automation Suite.")
    # Example: Setup a shared API session
    api_session = setup_api_session()
    return api_session

# Initialize shared resources when the package is imported
shared_api_session = initialize_shared_resources()

# Print initialization message
logging.info("Utils package initialized successfully. Shared resources are set up.")

# __init__.py for the bulk_uploader package
"""
The bulk_uploader package is designed to facilitate the mass uploading of product data from spreadsheets to the Temu store.
This package includes utilities to process spreadsheets, validate data, and communicate with the Temu API.
"""

import pandas as pd
import numpy as np

# Setup logging for the bulk uploader operations
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import necessary components from other packages if needed
from ..utils.common_utils import setup_api_session

# Initialize any necessary configurations
api_session = setup_api_session()

def get_api_session():
    """Utility function to access the configured API session."""
    return api_session

# Print initialization message
logging.info("Bulk Uploader package initialized successfully.")

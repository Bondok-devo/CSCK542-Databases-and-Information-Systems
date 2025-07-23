# =================================================================
#  File: db_config.py
#  Purpose: Loads database configuration from the .env file.
# =================================================================
"""
This module handles loading database configuration from environment variables.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection details
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

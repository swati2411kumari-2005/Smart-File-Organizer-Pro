"""
Logger Module
Smart File Organizer Pro
"""

import logging
import os

# Create logs folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message):
    """
    Save messages to log file.
    """
    logging.info(message)

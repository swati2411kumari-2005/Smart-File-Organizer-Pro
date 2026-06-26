"""
File Operations Module
Smart File Organizer Pro
"""

import os
import shutil
from logger import log_message


def create_folder(folder_path):
    """Create folder if it doesn't exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        log_message(f"Created folder: {folder_path}")


def move_file(source, destination):
    """Move file to destination folder."""
    try:
        shutil.move(source, destination)
        log_message(f"Moved: {source} -> {destination}")
        print(f"✓ Moved: {os.path.basename(source)}")
    except Exception as e:
        print(f"Error: {e}")
        log_message(f"Error moving file: {e}")


def rename_file(old_name, new_name):
    """Rename a file."""
    try:
        os.rename(old_name, new_name)
        log_message(f"Renamed: {old_name} -> {new_name}")
        print("✓ File Renamed Successfully")
    except Exception as e:
        print(f"Error: {e}")
        log_message(f"Rename Error: {e}")


def delete_file(file_path):
    """Delete a file."""
    try:
        os.remove(file_path)
        log_message(f"Deleted: {file_path}")
        print("✓ File Deleted Successfully")
    except Exception as e:
        print(f"Error: {e}")
        log_message(f"Delete Error: {e}")

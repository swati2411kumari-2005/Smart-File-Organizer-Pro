"""
CSV Reader Module
Smart File Organizer Pro
"""

import csv


def read_csv(file_path):
    """
    Read a CSV file and display its contents.
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)

            print("\nCSV Data\n")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("CSV file not found.")

    except Exception as e:
        print(f"Error: {e}")

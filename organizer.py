"""
Smart File Organizer Pro
Author: Swati Kumari
Description:
This program automatically organizes files into folders
based on their file extensions.
"""

import os
import shutil

# File extension mapping
FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",

    ".pdf": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "CSV",
    ".xlsx": "Excel",

    ".mp3": "Music",

    ".mp4": "Videos",

    ".zip": "Archives",
    ".rar": "Archives"
}


def organize_files(folder_path):
    """
    Organizes files into folders based on file extension.
    """

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        # Ignore folders
        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        folder_name = FILE_TYPES.get(extension, "Others")

        destination_folder = os.path.join(folder_path, folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        try:
            shutil.move(file_path,
                        os.path.join(destination_folder, file))

            print(f"Moved: {file} → {folder_name}")

        except Exception as error:
            print(f"Error moving {file}: {error}")


def main():
    print("=" * 45)
    print(" SMART FILE ORGANIZER PRO ")
    print("=" * 45)

    folder = input("Enter folder path: ")

    organize_files(folder)

    print("\nDone! Files organized successfully.")


if __name__ == "__main__":
    main()

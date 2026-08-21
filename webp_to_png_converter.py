"""
WEBP to PNG Converter
----------------------
This script converts all .webp files found in a specified local folder
into .png files, saving them in the same folder.
After that you can check the results and delete the original files if you want.

Requirements:
    pip install Pillow
"""

import os
from pathlib import Path
from PIL import Image

# ----------------------------------------------------------------------
# CONFIGURATION - set the folder path you want to process here
# ----------------------------------------------------------------------
FOLDER_PATH = r"D:\webp_to_png_test"  # <-- change this to your target folder


def convert_webp_to_png(folder_path: str) -> None:
    """Convert every .webp file in the given folder to .png."""

    # --------------------------------------------------------------
    # STEP 1: Validate that the folder exists
    # --------------------------------------------------------------
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"[ERROR] The folder does not exist: {folder_path}")
        return


    # --------------------------------------------------------------
    # STEP 2: Find all .webp files in the folder (case-insensitive)
    # --------------------------------------------------------------
    webp_files = [f for f in folder.iterdir() if f.suffix.lower() == ".webp"]


    # --------------------------------------------------------------
    # STEP 3: If no webp files found, show a clear message and abort the process
    # --------------------------------------------------------------
    if not webp_files:
        print(f"[INFO] No .webp files found in: {folder_path}")
        return

    print(f"[INFO] Found {len(webp_files)} .webp file(s) in: {folder_path}")


    # --------------------------------------------------------------
    # STEP 4: Convert each webp file to png
    # --------------------------------------------------------------
    converted_count = 0
    failed_count = 0

    for webp_file in webp_files:
        png_file = webp_file.with_suffix(".png")
        try:
            with Image.open(webp_file) as img:
                img.convert("RGBA").save(png_file, "PNG")
            print(f"[OK]    {webp_file.name} -> {png_file.name}")
            converted_count += 1
        except Exception as e:
            print(f"[FAIL]  {webp_file.name} -> {e}")
            failed_count += 1


    # --------------------------------------------------------------
    # STEP 5: Print a summary at the end
    # --------------------------------------------------------------
    print("\n[SUMMARY]")
    print(f"  Converted: {converted_count}")
    print(f"  Failed:    {failed_count}")


# ----------------------------------------------------------------------
# ENTRY POINT
# ----------------------------------------------------------------------
if __name__ == "__main__":
    convert_webp_to_png(FOLDER_PATH)
import os
from pathlib import Path

def generate_markdown_links(directory_path):
    target_dir = Path(directory_path)
    
    # Verify the provided directory exists
    if not target_dir.is_dir():
        print(f"Error: The directory '{directory_path}' does not exist.")
        return

    # Find all .md files in the immediate directory (use rglob("*.md") if you want subfolders too)
    md_files = sorted(target_dir.glob("*.md"), key=lambda x: x.name.lower())
    
    if not md_files:
        print("No Markdown (.md) files found in this directory.")
        return

    print("\n--- Copy and paste this under 'Other Files' ---\n")
    
    for file_path in md_files:
        # Gets the filename without the .md extension for a cleaner look
        display_name = file_path.stem.replace('_', ' ').title()
        # Formats it as a Markdown link
        print(f"- <a href='{file_path.name}'>{display_name}</a>")
        
    print("\n-----------------------------------------------\n")

if __name__ == "__main__":
    folder_path = input("Enter the absolute path to your folder containing the Markdown notes: ")
    generate_markdown_links(folder_path.strip())
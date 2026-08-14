import os
import time
import re

def format_title(filename):
    """Removes the extension, replaces underscores/hyphens with spaces, and capitalizes."""
    name = filename.replace(".md", "").replace("_", " ").replace("-", " ")
    return name.title()

def get_other_files(current_file, all_files):
    files_data = []
    
    for filename in all_files:
        # Excludes the file currently being updated so it doesn't link to itself
        if filename != current_file:
            title = format_title(filename)
            files_data.append((title, filename))
            
    # Sort alphabetically by title
    files_data.sort(key=lambda x: x[0].lower())
    
    new_list = ""
    for title, filename in files_data:
        new_list += f"- <a href=\"{filename}\">{title}</a>\n"
        
    return new_list

def update_all_html_tocs():
    # Gather all valid markdown files in the folder
    all_md_files = [f for f in os.listdir(".") if f.endswith(".md")]
    
    pattern = r"(<strong>Other Files</strong>\s*\n+)(.*?)(<strong>Table of Contents</strong>)"
    changed_any = False
    
    for md_file in all_md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Only process files that actually contain your custom sidebar structure
        if "<strong>Other Files</strong>" in content and "<strong>Table of Contents</strong>" in content:
            new_links = get_other_files(md_file, all_md_files)
            replacement = rf"\1\n{new_links}\n\3"
            
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated sidebar links in: {md_file}")
                changed_any = True
                
    if changed_any:
        print("Finished syncing all note files!")

def watch_folder():
    print("Watching folder for changes...")
    last_state = set(os.listdir("."))
    
    try:
        while True:
            time.sleep(2)
            current_state = set(os.listdir("."))
            if current_state != last_state:
                update_all_html_tocs()
                last_state = current_state
    except KeyboardInterrupt:
        print("\nStopped watching.")

if __name__ == "__main__":
    update_all_html_tocs() # Run once on startup
    watch_folder()
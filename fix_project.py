import os
import re

def update_anchor_links(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Regex to find anchor tags with href inside a folder
            updated_content = re.sub(r'href="([^/]+/)([^"/]+)"', r'href="\2"', content)
            
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(updated_content)
            
            print(f"Updated: {filename}")

# Call function with the target directory
update_anchor_links("./")

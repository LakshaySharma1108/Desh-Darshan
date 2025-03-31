import os
import re

def update_css_links(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Remove '/CSS Files/' from CSS file paths
            updated_content = re.sub(r'href="/CSS Files/([^"/]+\.css)"', r'href="\1"', content)
            
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(updated_content)
            
            print(f"Removed '/CSS Files/' from: {filename}")

# Call function with the target directory
update_css_links("./")

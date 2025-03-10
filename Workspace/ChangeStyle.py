import os, re

def modify_html_files(directory, injection_file_1, injection_file_2):
    try:
        with open(injection_file_1, "r", encoding="utf-8") as f:
            injection_text_1 = f.read()
    except FileNotFoundError:
        print(f"Error: The file {injection_file_1} was not found.")
        return
    
    try:
        with open(injection_file_2, "r", encoding="utf-8") as f:
            injection_text_2 = f.read()
    except FileNotFoundError:
        print(f"Error: The file {injection_file_2} was not found.")
        return
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                modified_content = content  # Preserve original content before modifications
                
                # Inject text after the last </style> tag
                last_style_index = modified_content.rfind("</style>")
                if last_style_index != -1:
                    modified_content = (
                        modified_content[:last_style_index + 8] + "\n" + injection_text_1 + modified_content[last_style_index + 8:]
                    )
                
                # Inject text after each </script> tag
                modified_content = re.sub(r"(</script>)", r"\1\n" + injection_text_2, modified_content)
                
                # Ensure <body> is followed by <div class="container">
                if not re.search(r'<div\s+class="container">', modified_content):
                    modified_content = re.sub(
                        r"(<body[^>]*>)", 
                        r'\1\n<div class="container">\n', 
                        modified_content, 
                        count=1
                    )
                
                # Ensure </div> is placed before the closing </body>
                modified_content = re.sub(r"(</body>)", r"</div>\n\1", modified_content, count=1)
                
                # Ensure <div class="navbar"> is inside <div class="container">
                if re.search(r'<div\s+class="container">', modified_content):
                    container_match = re.search(r'(<div\s+class="container">)', modified_content)
                    if container_match:
                        container_start = container_match.start()
                        container_content = modified_content[container_start:]
                        
                        if not re.search(r'<div\s+class="navbar">', container_content):
                            modified_content = re.sub(
                                r'(<div\s+class="container">)', 
                                r'\1\n<div class="navbar"><a href="#" id="backLink">&laquo; Back</a></div>', 
                                modified_content,
                                count=1
                            )
                
                # Replace original file with modified content
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(modified_content)
                print(f"Replaced original file: {file_path}")

if __name__ == "__main__":
    directory_to_search = r"./Microsoft/Microsoft Exchange"
    injection_file_path_1 = "style.txt"
    injection_file_path_2 = "script.txt"
    modify_html_files(directory_to_search, injection_file_path_1, injection_file_path_2)

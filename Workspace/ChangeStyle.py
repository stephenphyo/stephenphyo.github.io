import os
import re

def inject_text_in_script_tags(directory, injection_file_1, injection_file_2):
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
                
                # Inject text after the last </style> tag
                last_style_index = content.rfind("</style>")
                if last_style_index != -1:
                    content = content[:last_style_index + 8] + "\n" + injection_text_1 + content[last_style_index + 8:]
                
                # Inject text after each </script> tag
                content = re.sub(r"(</script>)", r"\1\n" + injection_text_2, content)
                
                # Ensure <body> is followed by <div class="container">
                content = re.sub(r"(<body[^>]*>)", r'\n<div class="container">', content, count=1)
                
                # Ensure </div> is placed before the closing </body>
                content = re.sub(r"(</body>)", r"</div>\n\1", content, count=1)
                
                # Save changes
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated: {file_path}")

if __name__ == "__main__":
    directory_to_search = r"./Oracle/Oracle SQL"
    injection_file_path_1 = "style.txt"
    injection_file_path_2 = "script.txt"
    inject_text_in_script_tags(directory_to_search, injection_file_path_1, injection_file_path_2)

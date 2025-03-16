import os, shutil

def copy_html_files(input_dir, output_dir):

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.html'):
                new_filename = file.replace('&', 'and').replace(' ', '-').lower()

                old_file = os.path.join(root, file)
                new_file = os.path.join(output_dir, new_filename)

                shutil.copy2(old_file, new_file)

                print('Copied: ', new_file)

if __name__ == '__main__':
    input_dir = input('Enter Input Directory Path: ')
    if not os.path.isdir(input_dir):
        raise SystemExit("Invalid Input Directory. Exiting...")

    output_dir = input('Enter Output Directory Path: ')
    if not os.path.isdir(output_dir):
        raise SystemExit("Invalid Output Directory. Exiting...")

    copy_html_files(input_dir, output_dir)
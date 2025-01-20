
import os
import subprocess
from dirlist import get_all_files_and_subdirs

def convert_to_utf8(file_list, output_directory):
    for file_path in file_list:

        parts = file_path.split(os.path.sep)
        fname = parts[-1]

        try:
            # Try reading the file with 'utf-8' encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except UnicodeDecodeError:
            # If 'utf-8' fails, try reading with 'latin-1' encoding
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()

        out_file = os.path.join(output_directory, fname)
        print(f"writing [{out_file}]")
        # Write the content back to the file with 'utf-8' encoding
        with open(out_file, 'w', encoding='utf-8') as file:
            file.write(content)

if __name__ == '__main__':
    # Directory containing HTML files
    input_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\content'
    output_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\content-enc'

    # Ensure output directory exists
    #os.makedirs(output_directory, exist_ok=True)

    #basedir = os.path.join(os.getcwd(),'codecamps-fix')
    file_list = get_all_files_and_subdirs(input_directory)
    convert_to_utf8(file_list,output_directory)

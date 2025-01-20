import os
import subprocess
from dirlist import get_all_files_and_subdirs


def convert_html_to_rst(html_file_path, rst_file_path):
    """Converts a single HTML file to an RST file using pandoc."""
    try:
        subprocess.run(['pandoc', '-f', 'html', '-t', 'rst', '-o', rst_file_path, html_file_path], check=True)
        print(f"Converted: {html_file_path} -> {rst_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {html_file_path}")
        
def convert_md_to_rst(md_file_path, rst_file_path):
    """Converts a single Markdown file to an RST file using pandoc.
    	pandoc yourfile.md -t rst -o outputfile.rst
    """
    try:
        subprocess.run(['pandoc', '-t', 'rst', '-o', rst_file_path, html_file_path], check=True)
        print(f"Converted: {md_file_path} -> {rst_file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {md_file_path}")


if __name__ == '__main__':
    # Directory containing HTML files
    input_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\extra_files_html'
    output_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\rst_output'

    # Ensure output directory exists
    #os.makedirs(output_directory, exist_ok=True)

    basedir = os.path.join(os.getcwd(),'extra_files_html')
    files = get_all_files_and_subdirs(basedir)
    for file in files:
        if file.find(".html") > -1:
            rst_fpath = f"{file.replace('.html', '.rst')}"
            convert_html_to_rst(file, rst_fpath)
        elif file.find(".md") > -1:
            rst_fpath = f"{file.replace('.md', '.rst')}"
            convert_html_to_rst(file, rst_fpath)
        else:
            continue

        
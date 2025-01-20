import glob
import os
import subprocess
from dirlist import get_all_files_and_subdirs
import os
import glob


def fix_encoding(input_dir, output_dir):
    """
    Fix encoding issues in .rst files by replacing non-UTF-8 characters.

    Args:
        input_dir (str): Directory containing the input .rst files.
        output_dir (str): Directory where the fixed files will be saved.
    """
    # Define replacements
    replacements = {
        b'\x91': b'"',
        b'\x92': b'"',
        b'\x93': b'"',  # Opening smart quote
        b'\x94': b'"',  # Closing smart quote
        b'\x96': b'"',
        b'\xf6': b'"',
        b'\xa0': b' ',
        b'\xfc': b' ',
        b'\xe8': b' ',
        b'\xef': b' ',
        b'\xbf': b' ',

        b'\x85': b' ',
        b'\xbd': b' ',
        b'\xe2': b' ',
        b'\x80': b' ',
        b'\xc2': b' ',

        b'\x9c': b' ',
        b'\x9d': b' ',
        b'\x99': b' ',

        b'\xa6': b' ',
        b'\xb0': b' ',

        b'\x97': b' ',
        b'\xa3': b' ',

        b'\x84': b' ',
        b'\xe9': b' ',
        b'\xe9': b' ',







    }

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Process all .rst files in the input directory
    for file in glob.glob(os.path.join(input_dir, "*.rst")):
        with open(file, "rb") as f:
            content = f.read()

        # Apply replacements
        for old, new in replacements.items():
            content = content.replace(old, new)

        # Save the fixed file in the output directory
        output_file = os.path.join(output_dir, os.path.basename(file))
        with open(output_file, "wb") as f:
            f.write(content)
        print(f"Wrote fixed output to [{output_file}]")

    print(f"Processed all .rst files from {input_dir} and saved them to {output_dir}.")


if __name__ == '__main__':
    # Directory containing HTML files
    input_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\niac'
    output_directory = r'C:\Users\bergr\github\branches\test\gen_rst\source\niac-fix'

    fix_encoding(input_directory, output_directory)


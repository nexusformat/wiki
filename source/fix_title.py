import os
import subprocess
from dirlist import get_all_files_and_subdirs

def generate_equals_string(input_string):
    length = len(input_string)
    return '=' * length

def fix_title(fpath, output_directory):
    try:
        is_content = False
        if fpath.find('content') > -1:
            is_content = True
        final_lines = []
        write_file = False
        if os.path.exists(fpath):
            parts = fpath.split(os.path.sep)
            fname = parts[-1]
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()

                idx = 0
                for l in lines:
                    if is_content or ((idx < 2) and l.find(".. container:: content") > -1):
                        #insert title
                        name = f"{parts[-1].replace('.rst','').replace('_',' ')}"
                        final_lines.append(f"{generate_equals_string(name)}\n")
                        #final_lines.append(f"{parts[-1].replace('.rst','').replace('_',' ')}\n")
                        final_lines.append(f"{name}\n")
                        final_lines.append(f"{generate_equals_string(name)}\n\n\n")
                        final_lines.append(l)
                        idx -=1000000000
                        write_file = True
                        #now turn it off
                        is_content = False
                    else:
                        final_lines.append(l)
                    idx += 1
                    if idx > 5 and not write_file:
                        return
        if write_file:
            outfile = os.path.join(output_directory,fname)
            with open(outfile, 'w') as f:
                f.writelines(final_lines)
            print(f'Done fixing title for {outfile}')
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")



if __name__ == '__main__':
    # Directory containing HTML files
    input_directory = r'C:\Users\bergr\github\branches\11\conv_files'
    output_directory = r'C:\Users\bergr\github\branches\11\conv_files\fixed'

    # Ensure output directory exists
    #os.makedirs(output_directory, exist_ok=True)

    #basedir = os.path.join(os.getcwd(),'codecamps-fix')
    files = get_all_files_and_subdirs(input_directory)
    for file in files:
        if file.find('.rst') > -1:
            fix_title(file, output_directory)

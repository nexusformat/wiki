import subprocess
import re
import os
import subprocess
from dirlist import get_all_files_and_subdirs

def check_and_fix_links(file_list):
    """
    Checks and fixes broken links in a list of files using LinkChecker.

    :param file_list: List of file paths to check
    """
    for file in file_list:
        print(f"Checking file: {file}")

        # Run linkchecker and capture output
        try:
            result = subprocess.run(
                ["linkchecker", "--check-extern", file],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
        except FileNotFoundError:
            print("LinkChecker is not installed or not in PATH.")
            return

        # Parse for broken links
        errors = extract_broken_links(result.stdout)
        if errors:
            print(f"Found {len(errors)} broken links in {file}. Fixing...")
            fix_links_in_file(file, errors)
        else:
            print(f"No broken links found in {file}.")


def extract_broken_links(output):
    """
    Extracts broken links from LinkChecker output.

    :param output: LinkChecker output as a string
    :return: List of broken link strings
    """
    # Regex pattern to extract URLs flagged as broken
    pattern = re.compile(r"URL\s+([^ ]+)\s+Error")
    return pattern.findall(output)


def fix_link(link):
    """
    Fixes a broken link by appending "broke" to it.

    :param link: The broken link as a string
    :return: Modified link string
    """
    return link + "broke"


def fix_links_in_file(file_path, broken_links):
    """
    Modifies a file to fix broken links by appending "broke" to each.

    :param file_path: Path to the file
    :param broken_links: List of broken link strings
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Replace broken links with the "fixed" versions
        for link in broken_links:
            fixed_link = fix_link(link)
            content = content.replace(link, fixed_link)

        with open(file_path, "w") as file:
            file.write(content)
        print(f"Fixed broken links in {file_path}.")

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


# Example usage
files_to_check = ["example1.html", "example2.rst"]
check_and_fix_links(files_to_check)

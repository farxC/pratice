import re
import argparse
import sys
import os

# Compile the pattern to improve perfomance
# Inspired by: https://stackoverflow.com/a/1176023/13089670
pattern = re.compile(r'(?<!^)(?=[A-Z])')

def pascal_to_snake_case(text):
    text = text.strip()
    return pattern.sub('_', text).lower()

def extract_args():
    # Returns the command line arguments
    parser = argparse.ArgumentParser(
        description="Parse given files from a given format to JSON format")
    parser.add_argument("format", choices=[
        "csv", "xml"],
        help="The format of the given file(s)")
    
    parser.add_argument("files", nargs='+', help="File(s) to be parsed")
    arguments = parser.parse_args(sys.argv[1:])
    return arguments.format, arguments.files

def validate_file(file, format):
    # Check if the file doesn't exist or not with the given format!!
    format_len = len(format)
    if not os.path.exists(file):
        file_without_path = get_file_name_from_path(file)
        raise FileNotFoundError(
            f"error: The file {file_without_path} doesn't exist!!!")
    
    if file[-format_len:] != format:
        file_without_path = get_file_name_from_path(file)
        raise ValueError(
            f"Error: the file {file_without_path} is not a format {format} file!!!"
        )
    
def get_file_name_without_extension(file_name):
    # Returns file name without the .extension
    # file.xml -> file
    file_without_path = get_file_name_from_path(file_name)
    return file_without_path[: file_without_path.find('.')]


def get_file_name_from_path(path):
    return path(path.rfind('/') + 1:)

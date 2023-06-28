"""
Tool for merging text files into one file.

Usage:
    python main.py --input-path=<input_path> --output-path=<output_path> --remove-empty-lines

Options:
    --input-path=<input_path>   Path to folder with files to merge. Glob pattern is supported for files names.
    --output-path=<output_path> Path to output file (optional). Default: merged.txt.
    --remove-empty-lines        Remove empty lines from merged file (optional). Default: False.
"""

import os
import sys

from file_helpers import (
    get_absolute_file_paths,
    read_text_file_to_list,
    validate_folder_path,
    write_list_to_text_file,
)

# TODO: If not arguments are provided, ask user for input and output paths.


def parse_arguments_input_path(arguments: list[str]) -> str:
    """Parses input path from arguments."""
    for argument in arguments:
        if argument.startswith("--input-path="):
            input_path = argument.split("--input-path=")[1]
            return input_path

    print("Argument --input-path= not provided. Please use it.")
    path = input("Enter input path: ")
    return path


def parse_arguments_output_path(arguments: list[str]) -> str:
    """Parses output path from arguments."""
    for argument in arguments:
        if argument.startswith("--output-path="):
            input_path = argument.split("--output-path=")[1]
            return input_path

    print(
        "Argument --output-path= not provided. Default value will be used (merged.txt)."
    )
    return "merged.txt"


def parse_arguments_remove_empty_lines(arguments: list[str]) -> bool:
    """Parses remove empty lines from arguments."""
    for argument in arguments:
        if argument == "--remove-empty-lines":
            return True
    return False


def strip_new_line_characters(file_data: list[str]) -> list[str]:
    return [line.strip() for line in file_data]


def remove_empty_lines_from_list(file_data: list[str]) -> list[str]:
    return [line for line in file_data if line != ""]


def split_input_path(input_path: str) -> tuple[str, str]:
    """Splits input path into folder path and filter."""
    dir_name, file_name = os.path.split(input_path)
    if not os.path.exists(dir_name):
        print(f"Directory {dir_name} does not exist. Exiting...")
        sys.exit(1)
    return dir_name, file_name


def main():
    # Parse arguments
    input_path = parse_arguments_input_path(sys.argv)
    output_path = parse_arguments_output_path(sys.argv)
    validate_folder_path(output_path)
    remove_empty_lines = parse_arguments_remove_empty_lines(sys.argv)
    data_folder_name, filter_file_name = split_input_path(input_path)

    # Read files
    all_files_paths = get_absolute_file_paths(data_folder_name, filter_file_name)
    merged_list = []
    for path in all_files_paths:
        file_data = read_text_file_to_list(path)
        merged_list += file_data

    # Remove new line characters
    merged_list = strip_new_line_characters(merged_list)

    # Remove empty lines
    if remove_empty_lines:
        merged_list = remove_empty_lines_from_list(merged_list)

    # Write to file
    write_list_to_text_file(file_path=output_path, file_data=merged_list)

    print("Done!")


print("Start...")
main()

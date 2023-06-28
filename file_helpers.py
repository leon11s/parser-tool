import fnmatch
import os


def write_list_to_text_file(file_data: list[str], file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in file_data:
            file.write(line + "\n")


def read_text_file_to_list(file_path: str) -> list[str]:
    """Reads text file and returns list of lines."""
    with open(file_path, "r") as file:
        file_data = file.readlines()
    return file_data


def get_absolute_file_paths(folder_name: str, filter: str = "*") -> list[str]:
    absolute_paths = []
    for dirpath, _, filenames in os.walk(folder_name):
        for filename in filenames:
            if fnmatch.fnmatch(filename, filter):
                absolute_path = os.path.abspath(os.path.join(dirpath, filename))
                absolute_paths.append(absolute_path)
    return absolute_paths

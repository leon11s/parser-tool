file_one = "data/file_a.txt"
file_two = "data/file_b.txt"
final_merged_file = "data/merged_file.txt"
remove_empty_lines = True


def read_text_file_to_list(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        file_data = file.readlines()
    return file_data


def strip_new_line_characters(file_data: list[str]) -> list[str]:
    return [line.strip() for line in file_data]


def remove_empty_lines_from_list(file_data: list[str]) -> list[str]:
    return [line for line in file_data if line != ""]


def write_list_to_text_file(file_data: list[str], file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in file_data:
            file.write(line + "\n")


# Read files
file_a_data = read_text_file_to_list(file_one)
file_b_data = read_text_file_to_list(file_two)

# Merge files
merged_list = file_a_data + file_b_data

# Remove new line characters
merged_list = strip_new_line_characters(merged_list)

# Remove empty lines
if remove_empty_lines:
    merged_list = remove_empty_lines_from_list(merged_list)

# Write to file
write_list_to_text_file(file_path=final_merged_file, file_data=merged_list)

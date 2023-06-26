file_one = "data/file_a.txt"
file_two = "data/file_b.txt"
final_merged_file = "data/merged_file.txt"
remove_empty_lines = True

with open(file_one, "r") as file_a:
    file_a_data = file_a.readlines()


with open(file_two, "r") as file_b:
    file_b_data = file_b.readlines()

merged_list = file_a_data + file_b_data
merged_list = [line.strip() for line in merged_list]

# Remove empty lines
if remove_empty_lines:
    merged_list = [line for line in merged_list if line != ""]


with open(final_merged_file, "w") as merged_file:
    for line in merged_list:
        merged_file.write(line + "\n")

import os
import sys
from typing import Union

import pdfkit

WKHTMLTOPDF_EXECUTABLE = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
BASE_TAXON_URL = "https://gd.eppo.int/taxon/"


def validate_folder_path(path: str) -> None:
    if os.path.isfile(path):
        print(f"Error: {path} is a file, not a folder.")
        sys.exit(1)

    os.makedirs(path, exist_ok=True)


def convert_webpage_to_pdf(
    url: str,
    output_file_path: str,
    wkhtmltopdf_path: Union[str, None] = None,
) -> None:
    try:
        pdfkit.from_url(
            url,
            output_file_path,
            verbose=True,
            configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path),
        )
    except OSError:
        print("Error: wkhtmltopdf not found in the specified location.")


def run_code_mode() -> None:
    code = input("Enter the code of the taxon: ")
    url = f"{BASE_TAXON_URL}{code.upper()}"
    output_file_path = f"{code}.pdf"
    convert_webpage_to_pdf(url, output_file_path, WKHTMLTOPDF_EXECUTABLE)


def run_file_mode() -> None:
    input_file_path = input("Enter the path to the input file: ")
    output_folder_path = input("Enter the path to the output folder: ")
    validate_folder_path(output_folder_path)
    if os.path.exists(input_file_path):
        with open(input_file_path, "r") as input_file:
            for line in input_file:
                code = line.strip()
                url = f"{BASE_TAXON_URL}{code.upper()}"
                output_file_path = os.path.join(output_folder_path, f"{code}.pdf")
                convert_webpage_to_pdf(url, output_file_path, WKHTMLTOPDF_EXECUTABLE)
    else:
        print("Error: Input file does not exist.")


def run_search_mode() -> None:
    pass


def main():
    try:
        mode = sys.argv[1]
        if mode == "code":
            print("Running in code mode.")
            run_code_mode()
        elif mode == "file":
            print("Running in file mode.")
            run_file_mode()
        elif mode == "search":
            print("Running in search mode.")
            run_search_mode()
        else:
            print(
                "Error: Invalid mode specified. Please specify a valid mode (code, file, search)."
            )
    except IndexError:
        print("Error: No mode specified. Please specify a mode (code, file, search).")


if __name__ == "__main__":
    main()
# https://gd.eppo.int/search?k=ralstonia
# https://gd.eppo.int/taxon/RALSSL
#

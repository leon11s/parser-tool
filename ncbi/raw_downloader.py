import os
import shutil
from zipfile import ZipFile

import pandas as pd
import requests


def extract_zip_file(zip_file_path, output_dir):
    with ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)
    print(f"Zip file extracted to: {output_dir}")


def get_acc_numbers_from_excel(file_path: str, sheet_name: str) -> list[str]:
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    data["Input_clean"] = data["Input"].str.replace(">", "")
    data["Input_clean"] = data["Input_clean"].str.replace("prf||", "")
    return data.loc[:, "Input_clean"].to_list()


def export_to_file(file_path: str, name: str, output_dir: str) -> None:
    os.makedirs("data_temp", exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    extract_zip_file(file_path, "data_temp")
    # copy file to data_extracted
    file_path = os.path.join("data_temp", "ncbi_dataset", "data", "protein.faa")
    shutil.copyfile(file_path, os.path.join(output_dir, f"{name}.faa"))
    # remove temp folder
    shutil.rmtree("data_temp")


def download_from_api(acc_number: str, download_folder: str, output_dir: str) -> None:
    try:
        url = f"https://api.ncbi.nlm.nih.gov/datasets/v2alpha/protein/accession/{acc_number}/download"
        query_param = {"include_annotation_type": "FASTA_PROTEIN"}
        os.makedirs(download_folder, exist_ok=True)
        file_path = os.path.join(download_folder, f"{acc_number}.zip")
        with open(file_path, "wb") as file:
            resp = requests.get(url, params=query_param)
            file.write(resp.content)
        export_to_file(file_path, acc_number, output_dir)
        print(f"Downloaded {url} to {file_path}.")
    except Exception as e:
        print(f"Error downloading {acc_number}: {e}")


def main():
    file_path = input("Select the file with accession numbers: ")
    sheet_name = input("Select the sheet name: ")
    output_dir = input("Select the output directory: ")
    acc_numbers = get_acc_numbers_from_excel(file_path, sheet_name)

    # remove previous data folder if exists
    shutil.rmtree("data", ignore_errors=True)
    shutil.rmtree(output_dir, ignore_errors=True)
    shutil.rmtree("data_temp", ignore_errors=True)

    for acc_number in acc_numbers:
        print(f"---> Downloading {acc_number}...")
        download_from_api(acc_number, "data", output_dir)

    shutil.rmtree("data", ignore_errors=True)

    print("Done!")


if __name__ == "__main__":
    main()

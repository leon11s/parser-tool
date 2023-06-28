import requests

from file_helpers import validate_folder_path


def download(url: str, file_path: str) -> None:
    """Download file from url and save it locally under `file_path`"""
    validate_folder_path(file_path)
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloaded {url} to {file_path}.")


def main():
    url = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/blood_pressure.csv"
    file_path = "data/blood_pressure.csv"
    download(url, file_path)


main()

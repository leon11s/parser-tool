import os

import requests


def download(url: str, folder_path: str) -> None:
    """Download file from url and save it locally under `file_path`"""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, url.split("/")[-1])
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloaded {url} to {file_path}.")


def main():
    url = "https://podatki.gov.si/dataset/83c7e79c-eff6-4e99-8de3-c1942ba86188/resource/84f76597-64d8-4e9e-9351-4df81b08aae5/download/lokacijezbiralnikovzaodpadnojedilnooljevobinisevnica.csv"
    folder = "data"
    download(url, folder)


main()

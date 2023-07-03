from typing import Union

import pdfkit


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


# https://gd.eppo.int/search?k=ralstonia
# https://gd.eppo.int/taxon/RALSSL
# C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

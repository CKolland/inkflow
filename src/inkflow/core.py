from pathlib import Path

import cairosvg
from jinja2 import Template
import pandas as pd


def create_data_flow(
    path_to_template: str, path_to_csv: str, output_dir: str, to_pdf: bool
):
    """
    Renders an SVG template for each row of a CSV file and optionally converts the result to PDF.

    This function reads a Jinja2-compatible SVG template and a CSV file containing dynamic data.
    It renders one SVG file per row in the CSV, replacing placeholders with column values, and
    saves each rendered SVG in the output directory. If `to_pdf` is True, each SVG is also
    converted to a corresponding PDF file using CairoSVG.

    :param path_to_template: Path to the SVG template file containing Jinja2 placeholders.
    :type path_to_template: str
    :param path_to_csv: Path to the CSV file providing dynamic data rows.
    :type path_to_csv: str
    :param output_dir: Directory where the generated SVG (and optional PDF) files will be saved.
    :type output_dir: str
    :param to_pdf: If True, convert each rendered SVG to a corresponding PDF file.
    :type to_pdf: bool

    :raises FileNotFoundError: If the template or CSV file cannot be found.
    :raises pandas.errors.ParserError: If the CSV file is malformed.
    :raises cairosvg.parser.ParsingError: If PDF conversion fails due to invalid SVG content.

    :return: None
    """

    # Load SVG template
    with open(path_to_template, "r", encoding="utf-8") as f:
        template = Template(f.read())

    # Load CSV data
    flow_data = pd.read_csv(path_to_csv)

    # Setup output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)

    # Fill SVG template with dynamic data flow
    for idx, row in flow_data.iterrows():
        placeholders = row.to_dict()
        rendered_svg = template.render(**placeholders)

        # Save SVG
        save_svg = f"{output_dir}/{path_to_template.stem}_{idx}.svg"

        with open(save_svg, "w", encoding="utf-8") as f:
            f.write(rendered_svg)

        if to_pdf:
            # Save PDF
            save_pdf = f"{output_dir}/{path_to_template.stem}_{idx}.pdf"

            # Convert SVG to PDF
            cairosvg.svg2pdf(url=str(save_svg), write_to=str(save_pdf))

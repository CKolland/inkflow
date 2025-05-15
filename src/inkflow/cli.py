import argparse
from pathlib import Path

from inkflow.core import create_data_flow


def main():
    """
    Entry point for the `inkflow` package.

    This function provides a command-line interface (CLI) for generating customized SVG
    and optionally PDF files using a Jinja2-based SVG template and CSV data.

    The user provides an SVG template containing Jinja2 placeholders and a CSV file with
    corresponding data rows. For each row in the CSV, a personalized badge is generated
    and saved to the specified output directory. Optionally, SVGs can be converted to PDF.

    Command-line arguments:
        * -t, --template : Path to the SVG template file.
        * -f, --flow-data : Path to the CSV file containing dynamic data.
        * -o, --output : Path to the directory where output files will be saved (default: current directory).
        * -p, --to-pdf : Boolean flag (default: True). If True, output will include PDFs converted from SVGs.

    Example:
        python cli.py -t template.svg -f data.csv -o outputs/ --to-pdf True

    :raises argparse.ArgumentError: If required arguments are missing or invalid.
    """

    # Setup command line interface
    parser = argparse.ArgumentParser(
        description="Lets dynamic data flow into an SVG template."
    )

    # Setup arguments
    parser.add_argument(
        "-t",
        "--template",
        type=Path,
        help="Path to the SVG template.",
    )
    parser.add_argument(
        "-f",
        "--flow-data",
        type=Path,
        help="Path to the CSV file that provides the data flow." "data",
        type=Path,
        help="",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("."),
        help="Directory to save the generated output.",
    )
    parser.add_argument(
        "-p",
        "--to-pdf",
        action="store_true",
        help="If set then SVG outputs are converted to PDF.",
    )

    args = parser.parse_args()

    create_data_flow(args.template, args.flow_data, args.output, args.to_pdf)


if __name__ == "__main__":
    main()

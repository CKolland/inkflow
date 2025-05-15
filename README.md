# `inkflow`

`inkflow` is a Python package that inserts data into placeholders inside SVG files using a dynamic data flow. This enables you to generate customized SVG (and optionally PDF) documents, such as name tags, badges, or labels, by merging template SVGs with data from CSVs. `inkflow` provides a simple command-line interface (CLI) for this workflow.

## Features

- Insert dynamic data into SVG templates using placeholder tags.
- Generate multiple SVG files from a single template and data source.
- Optionally convert generated SVGs to PDF format.
- Simple and flexible command-line interface.
- Supports CSV data sources for batch generation.

## How It Works

1. **Prepare an SVG Template:**  
   Design your SVG file and use placeholders (e.g., `{{ name }}`, `{{ role }}`) where you want dynamic data to appear.

2. **Prepare Your Data:**  
   Create a CSV file where each column matches a placeholder in your SVG template.

3. **Run Inkflow:**  
   Use the CLI to merge your data with the template, generating one output file per data row.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/CKolland/inkflow
cd inkflow
pip install -r requirements.txt
```

## Usage

The basic command structure:

```bash
python -m inkflow.cli --template <path_to_template.svg> --data <path_to_data.csv> [--output <output_dir>] [--pdf]
```

- `--template`: Path to your SVG template with placeholders.
- `--data`: Path to your CSV file containing data for placeholders.
- `--output`: (Optional) Output directory for generated files (default: `output/`).
- `--pdf`: (Optional) Also generate PDF versions of the output.

### Example

Suppose you have:

- Template: `templates/name_tag.svg` (with `{name}` and `{company}` placeholders)
- Data: `data/attendees.csv` (with columns `name,company`)

Generate SVG name tags:

```bash
python -m inkflow.cli --template inkflow/templates/name_tag.svg --data data/attendees.csv
```

Generate both SVG and PDF name tags:

```bash
python -m inkflow.cli --template inkflow/templates/name_tag.svg --data data/attendees.csv --pdf
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

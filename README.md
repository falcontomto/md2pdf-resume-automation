# Markdown-to-PDF Resume Converter

Convert my resume in PDF into a PDF.

Built on [`markdown-pdf`](https://pypi.org/project/markdown-pdf/), with styling controlled by a plain CSS file.

## Repository layout

| File | Purpose |
| --- | --- |
| `RESUME.md` | My resume in Markdown |
| `export.py` | Python script for the conversion |
| `styles.css` | Stylesheet applied to the PDF |

## Requirements

- Python 3.12 (`>=3.12,<3.13`)

## Local usage

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Export
python export.py RESUME.md
```

By default the PDF is written next to the input file (`RESUME.md` -> `RESUME.pdf`).

### Options

```
python export.py <markdown> [--css CSS] [--output OUTPUT]
```

| Argument | Default | Description |
| --- | --- | --- |
| `markdown` | (required) | Input Markdown file |
| `--css` | `styles.css` | Stylesheet to apply. (Optional) |
| `--output` | `<input>.pdf` | Output PDF path. (Optional) |

Example:

```bash
python export.py RESUME.md --css styles.css --output my-resume.pdf
```
## Styling

Edit `styles.css` to change the look of the PDF.
Not all CSS stylings are available. 
Check [markdown-pdf](https://pypi.org/project/markdown-pdf/) for details.

## GitHub Actions

The "Build PDF" workflow builds the PDF and publishes it as a GitHub Release.

**Triggers**

- **Push** that changes any `*.md` file, `export.py`, `styles.css` or `requirements.txt`
- **Manual run** (`workflow_dispatch`) with optional inputs:
  - `markdown_file`: Markdown file to convert (default `RESUME.md`)
  - `output_name`: output PDF name (default `<name>-<timestamp>.pdf`)

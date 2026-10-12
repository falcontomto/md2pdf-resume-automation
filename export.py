import argparse
from pathlib import Path

from markdown_pdf import MarkdownPdf, Section


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert markdown to a styled PDF.")
    parser.add_argument("markdown", type=Path, help="input markdown file")
    parser.add_argument("--css", type=Path, default=Path("styles.css"),
                        help="stylesheet (default: styles.css)")
    parser.add_argument("--output", type=Path, default=None,
                        help="output PDF (default: next to input)")
    args = parser.parse_args()

    if not args.markdown.is_file():
        parser.error(f"File not found: {args.markdown}")

    css = args.css.read_text(encoding="utf-8") if args.css.is_file() else None
    output = args.output or args.markdown.with_suffix(".pdf")

    pdf = MarkdownPdf(toc_level=2, optimize=True)
    pdf.meta["title"] = args.markdown.stem
    pdf.meta["author"] = "Joe"

    pdf.add_section(
        Section(
            args.markdown.read_text(encoding="utf-8"),
            root=str(args.markdown.parent),
            paper_size="A4",
            borders=(60, 60, -60, -60),
        ),
        user_css=css,
    )
    pdf.save(output)


if __name__ == "__main__":
    main()
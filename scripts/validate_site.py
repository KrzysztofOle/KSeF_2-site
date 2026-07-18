"""Validate the dependency-free bilingual GitHub Pages website."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
PAGES = {"index.html": "en", "pl.html": "pl"}


class PageParser(HTMLParser):
    """Collect document metadata and link targets from one HTML page."""

    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[str] = []
        self.lang: str | None = None
        self.title_count = 0

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        if tag == "html":
            self.lang = values.get("lang")
        if identifier := values.get("id"):
            self.ids.add(identifier)
        if tag == "a" and (href := values.get("href")):
            self.references.append(href)
        if tag == "script" and (src := values.get("src")):
            self.references.append(src)
        if tag == "link" and values.get("rel") == "stylesheet":
            if href := values.get("href"):
                self.references.append(href)
        if tag == "title":
            self.title_count += 1


def parse(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def validate_page(filename: str, language: str) -> list[str]:
    path = ROOT / filename
    page = parse(path)
    errors: list[str] = []

    if page.lang != language:
        errors.append(f"{filename}: expected lang={language!r}, got {page.lang!r}")
    if page.title_count != 1:
        errors.append(f"{filename}: expected one title, got {page.title_count}")

    for reference in page.references:
        parsed = urlsplit(reference)
        if parsed.scheme in {"http", "https", "mailto"}:
            continue
        if reference.startswith("#"):
            if parsed.fragment not in page.ids:
                errors.append(f"{filename}: missing anchor {reference}")
            continue

        target = path.parent / parsed.path
        if not target.is_file():
            errors.append(f"{filename}: missing file {parsed.path}")
            continue
        if parsed.fragment and parsed.fragment not in parse(target).ids:
            errors.append(f"{filename}: missing target {reference}")

    return errors


def main() -> None:
    errors = [
        error
        for filename, language in PAGES.items()
        for error in validate_page(filename, language)
    ]
    if errors:
        raise SystemExit("\n".join(errors))
    print("Static site validation passed.")


if __name__ == "__main__":
    main()

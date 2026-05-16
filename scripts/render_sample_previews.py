"""
Render preview screenshots of the ACME Insight Studio sample brief (.docx)
and sample deck (.pptx). Uses Word/PowerPoint COM automation (requires Office
on Windows). Outputs PNG images into samples/previews/.
"""

import os
import sys
from pathlib import Path

import win32com.client
import pythoncom


REPO_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = REPO_ROOT / "samples"
PREVIEW_DIR = SAMPLES_DIR / "previews"
DOCX = SAMPLES_DIR / "gtm-plan-acme-insight-studio.docx"
PPTX = SAMPLES_DIR / "gtm-plan-acme-insight-studio.pptx"


def export_pptx_slides_as_png(pptx_path: Path, out_dir: Path) -> list[Path]:
    """Export each slide of a .pptx as a PNG using PowerPoint COM."""
    out_dir.mkdir(parents=True, exist_ok=True)
    pythoncom.CoInitialize()
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = 1
    prs = ppt.Presentations.Open(str(pptx_path), WithWindow=False)
    paths: list[Path] = []
    try:
        for i, slide in enumerate(prs.Slides, start=1):
            out = out_dir / f"deck-slide-{i:02d}.png"
            slide.Export(str(out), "PNG", 1600, 900)
            paths.append(out)
    finally:
        prs.Close()
        ppt.Quit()
    return paths


def export_docx_pages_as_png(docx_path: Path, out_dir: Path) -> list[Path]:
    """Export .docx pages as PNG by saving to PDF via Word, then rendering
    PDF pages with PyMuPDF (fitz)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = out_dir / "_temp_brief.pdf"

    pythoncom.CoInitialize()
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = 0
    try:
        doc = word.Documents.Open(str(docx_path), ReadOnly=True)
        # FileFormat 17 = wdFormatPDF
        doc.SaveAs2(str(pdf_path), FileFormat=17)
        doc.Close(False)
    finally:
        word.Quit()

    import fitz  # PyMuPDF

    pdf = fitz.open(str(pdf_path))
    paths: list[Path] = []
    zoom = 1.7
    mat = fitz.Matrix(zoom, zoom)
    try:
        for i, page in enumerate(pdf, start=1):
            pix = page.get_pixmap(matrix=mat, alpha=False)
            out = out_dir / f"brief-page-{i:02d}.png"
            pix.save(str(out))
            paths.append(out)
    finally:
        pdf.close()

    pdf_path.unlink(missing_ok=True)
    return paths


def main():
    if not DOCX.exists():
        print(f"Missing: {DOCX}", file=sys.stderr)
        sys.exit(1)
    if not PPTX.exists():
        print(f"Missing: {PPTX}", file=sys.stderr)
        sys.exit(1)

    print("Rendering deck slides...")
    deck_imgs = export_pptx_slides_as_png(PPTX, PREVIEW_DIR)
    for p in deck_imgs:
        print(f"  - {p.relative_to(REPO_ROOT)}")

    print("Rendering brief pages...")
    brief_imgs = export_docx_pages_as_png(DOCX, PREVIEW_DIR)
    for p in brief_imgs:
        print(f"  - {p.relative_to(REPO_ROOT)}")

    print(f"\nWrote {len(deck_imgs) + len(brief_imgs)} preview images to "
          f"{PREVIEW_DIR.relative_to(REPO_ROOT)}/")


if __name__ == "__main__":
    main()

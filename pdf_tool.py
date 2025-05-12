import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs(pdf_list, output):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"Merged PDF saved as '{output}'.")

def split_pdf(pdf_path, output_dir):
    reader = PdfReader(pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = os.path.join(output_dir, f"page_{i+1}.pdf")
        with open(output_filename, 'wb') as f:
            writer.write(f)
        print(f"Saved: {output_filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Merge or split PDFs.")
    subparsers = parser.add_subparsers(dest="command")

    # Merge command
    merge_parser = subparsers.add_parser("merge", help="Merge multiple PDFs.")
    merge_parser.add_argument("pdfs", nargs="+", help="List of PDF files to merge.")
    merge_parser.add_argument("-o", "--output", default="merged.pdf", help="Output PDF filename.")

    # Split command
    split_parser = subparsers.add_parser("split", help="Split a PDF into separate pages.")
    split_parser.add_argument("pdf", help="PDF file to split.")
    split_parser.add_argument("-d", "--dir", default="output_pages", help="Directory to save split pages.")

    args = parser.parse_args()

    if args.command == "merge":
        merge_pdfs(args.pdfs, args.output)
    elif args.command == "split":
        os.makedirs(args.dir, exist_ok=True)
        split_pdf(args.pdf, args.dir)
    else:
        parser.print_help()

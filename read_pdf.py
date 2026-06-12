import sys
try:
    from PyPDF2 import PdfReader
except ImportError:
    import subprocess
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pypdf2'], check=True)
    from PyPDF2 import PdfReader

pdf_path = r"C:\Users\SAIFUDDIN\Downloads\publications_reports1774859128428_05e8ebb5-0598-4112-844c-bbe00e04aab8_33rd_Edition_of_ES-2026_Final.pdf"

reader = PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

# Extract first 15 pages of content
with open('pdf_extract.txt', 'w', encoding='utf-8') as f:
    for i, page in enumerate(reader.pages[:25]):
        text = page.extract_text()
        if text:
            f.write(f"\n\n===== PAGE {i+1} =====\n")
            f.write(text)

print("Extraction done - see pdf_extract.txt")

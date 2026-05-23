import fitz # PyMuPDF
import sys

def verify_pdf(filepath):
    try:
        doc = fitz.open(filepath)
        num_pages = len(doc)
        print(f"Total pages: {num_pages}")

        if num_pages == 200:
             print("SUCCESS: 200 pages.")
        else:
             print("FAILED: Page count is not 200.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_pdf(sys.argv[1])

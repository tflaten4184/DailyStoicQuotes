import PyPDF2
import re


def extract_text_from_pdf(pdf_file: str):

    outfile = open("output.txt", "w")

    # Open the PDF file of your choice
    with open(pdf_file, 'rb') as pdf:
        reader = PyPDF2.PdfReader(pdf, strict=False)
        # no_pages = len(reader.pages)
        pdf_text = []

        currentPage = 0
        for page in reader.pages:
            currentPage += 1
            if currentPage >= 16 and currentPage <= 412:
                content = page.extract_text()
                outfile.write(content)
                outfile.write("\n ------------------- \n")
                pdf_text.append(content)

        outfile.close()

        return pdf_text


def main():
    extracted_text = extract_text_from_pdf('DailyStoic.pdf')
    for text in extracted_text:
        # split_message = re.split(r'\s+|[,;?!.-]\s*', text.lower())
        print(text)


if __name__ == '__main__':
    main()
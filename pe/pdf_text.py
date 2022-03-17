from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import json
import re

def convert_pdf_to_txt(path):#This function helps in getting the text from the pdf and further complete the phrase to sentence.
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        print(page)
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

    return text


def formatt(pdf_file):
    get_data=convert_pdf_to_txt(pdf_file)
    get_data = re.sub(' +', ' ', get_data)
    #get_data=get_data.split('\n')
    req_list=[line for line in get_data.split('\n') if line.strip() != '']
    req_list = [i for i in req_list if i]
    req_list= [i for i in req_list if len(i)>100]
    return req_list
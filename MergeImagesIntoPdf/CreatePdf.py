# -*- coding: utf-8 -*-

#将多张图片合并成一pdf文件

#from https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images#

from fpdf import FPDF
from PIL import Image

import os

def makePdf(pdfFileName, listPages):

    cover = Image.open(listPages[0])
    width, height = cover.size

    pdf = FPDF(unit = "pt", format = [width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(page, 0, 0)

    pdf.output(pdfFileName, "F")

makePdf("result.pdf", [imgFileName for imgFileName in os.listdir('.') if imgFileName.endswith("png")])

from pathlib import Path
import glob
from fpdf import FPDF
import math

filepaths = glob.glob('text_files/*.txt')

print(filepaths)

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.set_text_color(0,0,0)
pdf.set_font(family='Times', style='B', size=14)

for path in filepaths:
    with open(path) as file:
        text_file = file.read()
    
    filename = Path(path).stem
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=0,h=14, txt=filename, align='L', ln=1)

    print(f"Filename: {path} -- No chars: {len(text_file)}")

    pdf.set_font(family='Times', style='', size=12)
    no_iter = math.ceil(len(text_file)/110)
    for i in range(no_iter):     
        if i == no_iter:
            pdf.cell(w=0,h=7, txt=text_file[i*110:], align='L', ln=1)
        else:        
            pdf.cell(w=0,h=7, txt=text_file[i*110:(i+1)*110], align='L', ln=1)

pdf.output('merge_text.pdf')


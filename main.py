import pandas as pd
import glob
from fpdf import FPDF 

filepaths = glob.glob("Invoices\*.xlsx")
print(filepaths)

for file in filepaths:
    
    df = pd.read_excel(file, sheet_name='Sheet 1')
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    
    header_name = df.columns.values.tolist()
    header_length = []
    
    for item in header_name:
        header_length.append(len(item))

    header_length[1] = header_length[1]+ 8
    header_length[2] = header_length[2] - 2
    header_length[3] = header_length[3] - 4
    header_length[4] = header_length[4] - 2
    
    invoice_Number, invoice_date = file[9:len(file)-5].split("-")
    
    pdf.set_font(family="Times", style='B', size=16 )
    pdf.set_text_color(0,0,0)

    pdf.cell(w=0, h=8, txt= f'Invoice nr. {invoice_Number}', border=0, ln=1, align='')
    pdf.cell(w=0, h=12, txt= f'Date {invoice_date}', border=0, ln=1, align='')

    for index, item in enumerate(header_name):
        pdf.set_font(family="Times", style='B', size=12 )
        pdf.set_text_color(0,0,0)
        if index < len(header_name)-1:
            pdf.cell(w=header_length[index]*3, h=12, txt= item, border=1, ln=0, align='C')
        else:
            pdf.cell(w=header_length[index]*3, h=12, txt= item, border=1, ln=1, align='C')
    
    pdf.set_font(family="Times", style='', size=10 )
    total = 0
    for index, row in df.iterrows():
        print(row[header_name[index]])
        pdf.cell(w=header_length[0]*3, h=10, txt= str(row[header_name[0]]), border=1, ln=0)
        pdf.cell(w=header_length[1]*3, h=10, txt= row[header_name[1]], border=1, ln=0)
        pdf.cell(w=header_length[2]*3, h=10, txt= str(row[header_name[2]]), border=1, ln=0, align='R')
        pdf.cell(w=header_length[3]*3, h=10, txt= str(row[header_name[3]]), border=1, ln=0, align='R')
        pdf.cell(w=header_length[4]*3, h=10, txt= str(row[header_name[4]]), border=1, ln=1, align='R')
        total = total + float(row[header_name[4]])

    pdf.cell(w=header_length[0]*3, h=12, txt= '', border=1, ln=0)
    pdf.cell(w=header_length[1]*3, h=12, txt= '', border=1, ln=0)
    pdf.cell(w=header_length[2]*3, h=12, txt= '', border=1, ln=0, align='R')
    pdf.cell(w=header_length[3]*3, h=12, txt= '', border=1, ln=0, align='R')
    pdf.cell(w=header_length[4]*3, h=12, txt= str(total), border=1, ln=1, align='R')
    
    pdf.set_font(family="Times", style='B', size=10 )
    pdf.cell(w=0, h=12, txt= f'The total due amount is {str(total)} Euros', border=0, ln=1, align='L')
    pdf.cell(w=0, h=12, txt= f'Python How', border=0, ln=1, align='L')



    pdf.output(file.replace('xlsx','pdf'))
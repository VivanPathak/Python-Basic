from fpdf import FPDF

Pdf = FPDF(orientation='L',unit='cm',format= 'A4')
Pdf.add_page()

#Let's add some text

Pdf.set_font(family='Times',style='B',size=50)
Pdf.cell(w=15,h=5,txt='Flatmates Bill',border=1, align='C')

Pdf.output("Flatmate's Bill.pdf")
import webbrowser
from fpdf import FPDF


class Bill:
    """
    This class Contains data about a bill, such as Total amount and Period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """Create a flatmate who lives in the house and share the bill """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate_2):
        weight = self.days_in_house / (self.days_in_house + flatmate_2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport(Flatmate):
    """Creates a pdf which contains data about flatmates such as name, bill, due amount
    and other things"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        Flatmate1_Pays = str(round(flatmate1.pays(bill, flatmate2), 2))
        Flatmate2_Pays = str(round(flatmate2.pays(bill, flatmate1), 2))
        # Stylle of the Pdf
        Pdf = FPDF(orientation='P', unit='cm', format='A4')
        Pdf.add_page()

        # Setting of the title

        #Add Icon
        Pdf.image(name="house (1).png", w=3, h=3)

        Pdf.set_font(family='Times', style='B', size=30)
        Pdf.cell(w=0, h=2, txt='Flatmates Bill', border=0, align='C',ln=1)


        #Insert Period of the bill and the value
        Pdf.set_font(family='Times', style='I', size=20)
        Pdf.cell(w=6, h=2, txt='Period:',border=0,align='C')
        Pdf.set_font(family='Times', style='B', size=17)
        Pdf.cell(w=10, h=2, txt=bill.period, align='C', border=0,ln=1)


        # Insert name  of the flatmate1 and the amount he has to pay...
        Pdf.set_font(family='Times', style='I', size=20)
        Pdf.cell(w=6, h=1, txt=flatmate1.name, border=0, align='C')
        Pdf.set_font(family='Times', style='B', size=17)
        Pdf.cell(w=10, h=1, txt=Flatmate1_Pays, align='C', border=0, ln=1)

        # Insert name  of the flatmate2 and the amount he has to pay...
        Pdf.set_font(family='Times', style='I', size=20)
        Pdf.cell(w=6, h=1, txt=flatmate2.name, border=0, align='C')
        Pdf.set_font(family='Times', style='B', size=17)
        Pdf.cell(w=10, h=1, txt=Flatmate2_Pays, align='C', border=0, ln=1)
        Pdf.output(self.filename)



        webbrowser.open(self.filename)

#Creating CLI to improve the code
amount = float(input("Pls enter the amount of the Bill here: "))
period = input("Enter the period of the bill e.g. December 2021: ")

Name_Flatmate1 = input("Enter the name of first Flatmate: ")
Days_In_House_1 = int(input(f"Pls enter no. of days {Name_Flatmate1} stayed in the house:  "))

Name_Flatmate2 = input("Enter the name of The second flatmate: ")
Days_In_House_2 = int(input(f"Pls enter no. of days {Name_Flatmate2} stayed in the house:  "))


the_bill = Bill(amount,period)
Flatmate1  = Flatmate(Name_Flatmate1,Days_In_House_1)
Flatmate2  = Flatmate(Name_Flatmate2, Days_In_House_2)

print(f" {Name_Flatmate1} pays: ", Flatmate1.pays(the_bill, Flatmate2))
print(f" {Name_Flatmate2} pays:   ", Flatmate2.pays(the_bill, Flatmate1))

Pdfreport = PdfReport(filename= f"{the_bill.period}.pdf ")
Pdfreport.generate(Flatmate1, Flatmate2,the_bill)
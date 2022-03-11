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
        self.days_in_house

    def pays(self, bill):
        pass


class PdfReport:
    """Creates a pdf which contains data about flatmates such as name, bill, due amount
    and other things"""

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=12000, period="september 2021")
Flatmate1 = Flatmate(name="Vivan", days_in_house=25)
Flatmat2 = Flatmate(name="Ved", days_in_house=20)

print(Vivan.pays(bill=the_bill))
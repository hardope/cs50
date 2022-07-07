from fpdf import FPDF


class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0, 60, 'CS50 Shirtificate')
        self._pdf.image("shirtificate.png")
        
    def save(self, name):
        self._pdf.output(name)



name = input("Name: ")
pdf = PDF(name)

pdf.save('shirtificate.pdf')
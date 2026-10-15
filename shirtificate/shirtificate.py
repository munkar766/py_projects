from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 32)
        self.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")


def generate_shirtificate(name):
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.image("shirtificate.png", x=20, y=70, w=170)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)

    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


def main():
    name = input("Name: ").strip()
    generate_shirtificate(name)


if __name__ == "__main__":
    main()

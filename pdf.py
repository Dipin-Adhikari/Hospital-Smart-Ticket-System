from fpdf import FPDF

def main(id, name, sex, age, address, date, time, department, room_no):
    class PDF(FPDF):
        def header(self):
            self.set_font('helvetica', 'B', 20)
            self.set_fill_color(255, 255, 255)
            self.set_line_width(1)
        
            self.cell(0, 10, 'Smart Hospital', border=True, align='C', fill=True)
            self.ln(20)

        def edits(self, name, sex, age, address, date, time, department, room_no):
            self.add_page()
            self.set_font('helvetica', '', 12)
            self.set_fill_color(255, 255, 255)
            self.set_line_width(1)
            self.cell(100, 10, f'Name: {name}', fill=True, border=True)
            self.cell(96, 10, f'Sex: {sex}', fill=True, border=True)
            self.ln(8)
            self.cell(100, 10, f'Age: {age}', fill=True, border=True)
            self.cell(96, 10, f'Address:{address}', fill=True, border=True)
            self.ln(8)
            self.cell(100, 10, f'Date: {date}', fill=True, border=True)
            self.cell(96, 10, f'Time: {time}', fill=True, border=True)
            self.ln(8)
            self.cell(100, 10, f'Department: {department}', fill=True, border=True)
            self.cell(96, 10, f'Room No: {room_no}', fill=True, border=True)
            self.ln(20)

            self.set_font('helvetica', '', 16)
            self.cell(0, 85, 'Investigation:', border=True, align='L', fill=True)
            self.ln(95)
            self.cell(0, 85, 'Treatment Given:', border=True, align='L', fill=True)


        def footer(self):
            self.set_y(-15)
            self.set_font('helvetica', '', 12)
            self.set_line_width(1)
            self.set_fill_color(255, 255, 255)
            self.cell(0, 12, 'Case Seen By: ', border=True, fill=True)


    pdf = PDF('P', 'mm', 'Letter')
    pdf.edits(name, sex, age, address, date, time, department, room_no)
    filename = name + id + '.pdf'
    pdf.output(filename)



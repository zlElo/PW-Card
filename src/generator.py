from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import random
import string



def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return random.choice(characters)

def abc(cols):
    letters = ['']
    for j in range(cols):
        for i in string.ascii_uppercase:
            letters.append(i)

        return letters
        
def create_password_card(filename, rows, cols, id):
    data = [[generate_password() for j in range(cols)] for i in range(rows)]
    # Add coordinates around the table
    for i in range(rows):
        data[i].insert(0, f"{i+1}")  # Add y-coordinate
        data[i].append(f"{i+1}")  # Add y-coordinate
    coords_row = abc(cols)  # Add x-coordinates for the top and bottom rows
    data.insert(0, coords_row)  # Add coordinates for the top row
    data.append(coords_row)  # Add coordinates for the bottom row

    pdf = SimpleDocTemplate(filename, pagesize=letter)
    table = Table(data, colWidths=10, rowHeights=10)
    table.setStyle(TableStyle([
        ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
        ('BOX', (0,0), (-1,-1), 0.5, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),  # Add background color to the first column
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Add background color to the first row
        ('BACKGROUND', (-1, 0), (-1, -1), colors.lightgrey),  # Add background color to the last column
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),  # Add background color to the last row

    ]))
        
    # Add the table to the elements list
    elems = [table]

    style = getSampleStyleSheet()
    style['Normal'].fontSize = 8  # Set the font size
    style['Normal'].alignment = 1  # 0 for left, 1 for center, 2 for right

    # Add the table to the elements list
    elems = [Paragraph(f"Identification: {id}", style['Normal']), Spacer(5, 10)]  # Add a spacer with 20 units of vertical space
    elems.append(table)

    # Bild hinzufügen
    im = Image("logo/pw-card-bg.png", 1*inch, 1*inch)  # Bildgröße anpassen
    im.hAlign = 'LEFT'  # Ausrichtung des Bildes
    elems.insert(0, im)  # Bild an erster Stelle einfügen
        
    # Build the PDF
    pdf.build(elems)

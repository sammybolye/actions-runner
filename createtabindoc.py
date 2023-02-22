from docx import Document
from docx.shared import Cm

def create_table_in_word(severity, base_score, exploit_score, version, cve_list):
    # Create a new Word document
    doc = Document()

    # Create a table with 4 columns and 2 rows
    table = doc.add_table(rows=2, cols=5)

    # Add table headers
    table.rows[0].cells[0].text = 'Severity Rating'
    table.rows[0].cells[1].text = 'Base Score'
    table.rows[0].cells[2].text = 'Exploitability Score'
    table.rows[0].cells[3].text = 'Version'
    table.rows[0].cells[4].text = 'CVE List'

    # Add the input values to the table
    table.rows[1].cells[0].text = severity
    table.rows[1].cells[1].text = base_score
    table.rows[1].cells[2].text = exploit_score
    table.rows[1].cells[3].text = version
    table.rows[1].cells[4].text = '\n'.join(cve_list)

    # Auto-fit the table columns
    for row in table.rows:
        for cell in row.cells:
            cell.width = Cm(5.0)

    table.style = 'Table Grid'        

    # Save the document
    doc.save('table.docx')

#Example usage
# severity = 'Critical'
# base_score = '10.0'
# exploit_score = '9.8'
# version = '1.1.1k'
# cve_list = ['CVE-2022-1292', 'CVE-2022-2068', 'CVE-2022-0778', 'CVE-2021-23840', 'CVE-2021-3712', 'CVE-2021-23841', 'CVE-2021-4160', 'CVE-2020-1971', 'CVE-2020-1968', 'CVE-2021-23839']
# create_table_in_word(severity, base_score, exploit_score,version, cve_list)
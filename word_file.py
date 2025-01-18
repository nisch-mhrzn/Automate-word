from docx import Document
import paragraphs

document=Document()
document.add_heading("Hello World")
document.save("test.docx")

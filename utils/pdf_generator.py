from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph


def create_pdf(text, filename):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in text.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

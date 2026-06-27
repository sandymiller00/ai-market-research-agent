from utils.pdf_generator import create_pdf


def generate_report(content, topic):
    filename = f"reports/{topic.replace(' ', '_')}.pdf"

    create_pdf(content, filename)

    return filename

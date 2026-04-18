from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(results):
    file_path = "report.pdf"
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()

    content = []

    for r in results:
        text = f"{r['name']} - Score: {r['score']}% | Missing: {', '.join(r['missing'])}"
        content.append(Paragraph(text, styles["Normal"]))

    doc.build(content)
    return file_path
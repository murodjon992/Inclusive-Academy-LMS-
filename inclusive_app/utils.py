from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
from PyPDF2 import PdfReader, PdfWriter
from django.utils import timezone
import io
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

# Admin Views
def fill_certificate(template_path, output_path, user, test_name,created_at=None):
    packet = io.BytesIO()

    if created_at is None:
        created_at = timezone.now().strftime("%d.%m.%Y")
    c = canvas.Canvas(packet, pagesize=landscape(A4))

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_WIDTH/2+40, PAGE_HEIGHT/2+140, f"{user.first_name} {user.last_name}")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(PAGE_WIDTH / 2 + 100, PAGE_HEIGHT / 2+40, f'"{test_name}"')

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(PAGE_WIDTH / 2 + 180 , PAGE_HEIGHT / 2-240, f'{created_at}')

    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    template = PdfReader(template_path)

    writer = PdfWriter()
    page = template.pages[0]
    page.merge_page(overlay.pages[0])
    writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)
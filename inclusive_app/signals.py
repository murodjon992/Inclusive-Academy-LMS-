from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import  Certificate
from .utils import fill_certificate
import os


def create_certificate_after_test(sender, instance, created, **kwargs):
    # faqat yangi test bo‘lsa
    if not created:
        return

    # agar oldin yaratilgan bo‘lsa
    if hasattr(instance, 'certificate'):
        return

    cert = Certificate.objects.create(
        user=instance.user,
        test_result=instance
    )

    template_path = settings.BASE_DIR / 'static/certificates/inc_sertifikat.pdf'
    output_path = settings.MEDIA_ROOT / f'certificates/cert_{cert.id}.pdf'

    fill_certificate(
        template_path=template_path,
        output_path=output_path,
        user=instance.user,
        test_name=instance.test.title
    )

    cert.pdf.name = f'certificates/cert_{cert.id}.pdf'
    cert.save()

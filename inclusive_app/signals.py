from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import  Certificate,QuizResult
from .utils import fill_certificate
import os

@receiver(post_save, sender=QuizResult)
def create_certificate_after_test(sender, instance, created, **kwargs):
    # faqat yangi test bo‘lsa
    if not created:
        return

    if not instance.passed:
        return

    if Certificate.objects.filter(user=instance.user, course=instance.quiz.course).exists():
        return

    cert = Certificate.objects.create(
        user=instance.user,
        course=instance.quiz.course,
        score=instance.score
    )

    template_path = settings.BASE_DIR / 'static/certificates/inc_sertifikat.pdf'
    output_path = settings.MEDIA_ROOT / f'certificates/cert_{cert.id}.pdf'

    fill_certificate(
        template_path=template_path,
        output_path=output_path,
        user=instance.user,
        test_name=instance.quiz.title
    )

    cert.pdf.name = f'certificates/cert_{cert.id}.pdf'
    cert.save()

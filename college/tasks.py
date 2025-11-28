from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from users.models import User
from college.models import Subscription


@shared_task
def send_information(course_id):
    """Отправляет сообщение пользователю."""
    subject = "Обновление курса!"
    message = "Материалы курса обновлены!"
    subscription = Subscription.objects.filter(course_id=course_id)
    for s in subscription:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [s.user.email])


@shared_task
def blocking_user():
    """Проверяет пользователя по дате последнего входа."""
    month_ago = timezone.now() - timezone.timedelta(days=30)
    inactive_user = User.objects.filter(last_login__lt=month_ago, is_active=True)
    inactive_user.update(is_active=False)

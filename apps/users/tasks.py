from django.core.mail import send_mail

from django_rest_practice.celery import app


@app.task
def send_message_to_user(email):
    send_mail(
        'Title',
        "Hello, I'm from Kyrgyzstan, Osh. We do start new magazine!",
        'artnyr2004@gmail.com',
        [email],
        fail_silently=False,
    )


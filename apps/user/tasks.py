from practice.celery import app
from send_tg import send_telegram
from django.core.mail import send_mail


@app.task
def send():
     send_mail(
          'Заголовок',
          'Ты натурал!!',
          'mammonth02@gmail.com',
          ['ssavutokhunov@gmail.com'],
          fail_silently=False,
     )
     send_telegram('прив')
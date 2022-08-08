from practice.celery import app
from django.core.mail import send_mail


@app.task
def send(self):
     send_mail(
          'Заголовок',
          'Ты натурал!!',
          'mammonth02@gmail.com',
          [self],
          fail_silently=False,
     )

from practice.celery import app
from send_tg import send_telegram
from apps.info.models import *
from django.db.models import F
import datetime


@app.task
def send_info_tg():
        today = datetime.date.today()
        active = Active.objects.get(id = 1)

        if active.date != today:
            ActiveList.objects.create(date = active.date, int = active.today)
            send_telegram(f'за "{active.date}" было сделано запросов: {active.today}')
            Active.objects.all().update(date = today, today = 0)




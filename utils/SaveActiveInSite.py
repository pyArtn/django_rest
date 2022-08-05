from apps.info.models import *
from django.db.models import F
import datetime



class SaveActive:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        r = self.get_response(request)

        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            if not Active.objects.all():
                Active.objects.create(id = 1, all = 0, today = 0, date = today)

            today = datetime.date.today()
            active = Active.objects.get(id = 1)


            if active.date != today:
                ActiveAll.objects.create(date = active.date, int = active.today)
                Active.objects.all().update(date = today, today = 0)
            Active.objects.all().update(all = F("all") + 1, today = F("today") + 1)

        return r
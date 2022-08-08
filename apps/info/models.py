from django.db import models

# Create your models here.

class Active(models.Model):
    all = models.BigIntegerField()
    today = models.IntegerField()
    date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class ActiveList(models.Model):
    date = models.DateField()
    int = models.IntegerField()

    def __str__(self):
        return f'{self.date}: {self.int}   {self.id}'


from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    real_name =  models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} {}'.format(id,self.real_name,self.tz)

class ActivityPeriod(models.Model):
    aid = models.ForeignKey(Users, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)

    def __str__(self):
        return '{} {} {}'.format(self.aid,self.start_time,self.end_time)
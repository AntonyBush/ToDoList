from django.contrib.admin.widgets import AdminSplitDateTime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms import widgets
from django.utils import timezone
from datetime import datetime,timedelta
import pytz


# Create your models here.
class Task(models.Model):
    utc=pytz.UTC
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def default_start_time():
        now = timezone.now()
        start = now.replace(hour=22, minute=0, second=0, microsecond=0)
        return start if start > now else start + timedelta(days=1) 
    deadline=models.DateTimeField(auto_now_add=False,null=True,blank=False,default=default_start_time)
    def __str__(self):
        return self.title

    def is_end_date(self):
        return timezone.now() > self.deadline

    class Meta:
        ordering=['complete']
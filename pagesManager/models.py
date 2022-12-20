from django.db import models

class Profile(models.Model):
    idProfile = models.AutoField(primary_key=True)
    key_id = models.IntegerField(default=0)
    user_name = models.CharField(max_length=30)
    last_login = models.CharField(max_length=30, blank=True, default='')

from django.db import models
from phone_field import PhoneField

class CusData(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200,)
    phone       = PhoneField(null=False, blank=False, unique=True)
    provider    = models.CharField(max_length=200, blank=False)
    email       = models.CharField(max_length=200, blank=True)
    dateOfbirth = models.CharField(max_length=200, blank=True)
    point       = models.IntegerField(default=0)
    coupon      = models.IntegerField(default=0)
    last_check_in = models.CharField(max_length=30, blank=True, default='')

    @classmethod
    def create(cls, id, name, phone):
        CusData = cls(
            id= id,
            phone= phone,
            name= name,
        )
        # do something with the book
        return CusData


class CheckInData(models.Model):
    id           = models.AutoField(primary_key=True)
    idCus        = models.IntegerField(default=0)
    name         = models.CharField(max_length=200, blank=True)
    phone        = PhoneField(null=False, blank=False)
    checkInTime  =  models.CharField(max_length=30, blank=True, default='')
    orderPrice   = models.IntegerField(default=0)
    flag         = models.IntegerField(default=0)

    @classmethod
    def create(cls, id, phone):
        CheckInData = cls(
            id= id,
            phone= phone,
        )
        # do something with the book
        return CheckInData   
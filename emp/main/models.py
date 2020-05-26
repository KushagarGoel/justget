from django.contrib.auth.models import User
from django.db import models




class Post(models.Model):
    travel_type = models.CharField(max_length=50)
    purpose = models.CharField(max_length=50)
    purpose_desc = models.CharField(max_length=50)
    journey_type= models.CharField(max_length=50)
    mode= models.CharField(max_length=50)
    from_place= models.CharField(max_length=50)
    to_place= models.CharField(max_length=50)
    travel_date= models.DateField(max_length=50)
    etd= models.CharField(max_length=50)
    classs= models.CharField(max_length=50)
    air_train= models.CharField(max_length=50)
    booking_type= models.CharField(max_length=50)
    advance_req = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
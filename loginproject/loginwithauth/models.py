from django.db import models

class admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=56)
    email = models.CharField(max_length=56)
    password = models.CharField(max_length=76)

    class Meta:
            db_table = 'admin'


class user(models.Model):
    id = models.AutoField(primary_key=True)
    nic = models.CharField(max_length=12)
    nickname = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phoneNo = models.CharField(max_length=100)

    class Meta:
            db_table = 'user'

class reviews(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    queAndAnsr = models.TextField()
    geo_tag = models.TextField()
    device_signature= models.TextField()

    class Meta:
            db_table = 'reviews'


class complaints(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    geo_tag = models.TextField()
    description= models.TextField()

    class Meta:
            db_table = 'complaints'

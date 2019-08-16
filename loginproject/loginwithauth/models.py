from django.db import models
#from django.utils import timezone

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
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = 'user'
    
    def __str__(self):
        return self.nic

class review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    queAndAnsr = models.TextField()
    geo_tag = models.TextField()
    device_signature= models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = 'review'

    def __str__(self):
        return str(self.user_id)
    
    # @property
    # def days_since_creation(self):
    #     diff = timezone.now() - self.date_created
    #     return diff.days


class complaint(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    geo_tag = models.TextField()
    description= models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True) 

    class Meta:
            db_table = 'complaint'

    def __str__(self):
        return str(self.user_id)

    # @property
    # def days_since_creation(self):
    #     diff = timezone.now() - self.date_created
    #     return diff.days

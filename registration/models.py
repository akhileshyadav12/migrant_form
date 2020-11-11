from django.db import models

LOCATIONCHOICE = (
    ('Select','None'),
    ('MUMBAI','MUMBAI'),
    ('DELHI', 'DELHI'),
    ('BANGLORE','BANGLORE'),
    ('GUJRAT','GUJRAT'),
    ('PUNE','PUNE'),
)




class Person(models.Model):
    name = models.CharField(max_length=130)
    mobile=models.IntegerField(primary_key=True)

    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    job=models.CharField(max_length=10,choices=LOCATIONCHOICE,default='Select')
    home=models.CharField(max_length=10,choices=LOCATIONCHOICE,default='Select')

    bio = models.TextField(blank=True)

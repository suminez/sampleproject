from django.db import models

# Create your models here.
# sample_project (db)
#docs.djangoproject.com
#python manage.py makemigrations if any change happend in model
#python manage.py migrate

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Teams(models.Model):
    teamname=models.CharField(max_length=250)
    teamimg=models.ImageField(upload_to='teampics')
    teamdesc=models.TextField()

    def __str__(self):
        return self.teamname


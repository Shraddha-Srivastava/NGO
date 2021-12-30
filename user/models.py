from django.db import models


# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    mobile = models.CharField(max_length=20)
    message = models.CharField(max_length=800)

    def __str__(self):
        return self.name


class gallery(models.Model):
    pdes = models.CharField(max_length=200)
    gpic = models.ImageField(upload_to='static/gallery/', default="")
    gdate = models.DateField()


class events(models.Model):
    city = models.CharField(max_length=100)
    etitle = models.CharField(max_length=400)
    epurpose = models.TextField(max_length=2000)
    epic = models.ImageField(upload_to='static/events', default="")
    edate = models.DateField()
    sthanks = models.CharField(max_length=200)


class city(models.Model):
    cityname = models.CharField(max_length=50)
    cdate = models.DateField()

    def __str__(self):
        return self.cityname


class membership(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, primary_key=True)
    mobile = models.CharField(max_length=20)
    cityname = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    address = models.TextField(max_length=700)
    picture = models.ImageField(upload_to='static/members', default="")
    mdate = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class donate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=20)
    cityname = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    address = models.TextField(max_length=700)
    amount = models.FloatField()
    ddate = models.DateField()

    def __str__(self):
        return self.name


class notification(models.Model):
    news = models.TextField(max_length=500)
    ndate = models.DateField()

class slider(models.Model):
    stitle=models.CharField(max_length=100)
    sdes=models.TextField(max_length=5600)
    spic=models.ImageField(upload_to='static/slider',default="")

class video(models.Model):
    vlink=models.CharField(max_length=500)
    vtitle=models.CharField(max_length=500)
    vdate=models.DateField()
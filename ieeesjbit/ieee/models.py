from django.db import models


class Members(models.Model):
    name = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 10)
    sem = models.IntegerField()

    def __str__(self):
        return self.name


class General(models.Model):
    phone = models.CharField(max_length = 14)
    email = models.EmailField()


class Form(models.Model):
    name = models.CharField(max_length=50)
    event_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()


class News(models.Model):
    news_item = models.TextField(max_length = 200)

class Announcement(models.Model):
    announcement = models.TextField(max_length = 200)

class Events(models.Model):
    event_name = models.CharField(max_length = 200)
    event_date = models.DateField()
    event_description = models.TextField(max_length = 200)

    def __str__(self):
        return self.event_name


class Posts(models.Model):
    Name = models.CharField(max_length = 100)
    About_Post = models.TextField(max_length = 500)
    Attachment = models.FileField()
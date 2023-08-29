from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10)
    desc = models.TextField(max_length=4000)

    def __str__(self):
        return self.name + ' - ' + self.email


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='subject_logos/', null=True, blank=True)
    # classes = models.CharField(max_length=50)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # images = models.ImageField(upload_to='event_img/', null=True, blank=True)

    def __str__(self):
        return self.title


class EventImage(models.Model):

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    images=models.ImageField(upload_to='event_img/', default="cmsNvsd_kjzx_jdn", null=True, blank=True)

    def __str__(self):
        return f"Image for {self.event.title}"
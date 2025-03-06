from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('webinar', 'Webinar'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()
    link = models.URLField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    event_host = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.title

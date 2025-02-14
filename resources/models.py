from django.db import models

class Resource(models.Model):
    CATEGORY_CHOICES = [
        ('technical', 'Technical'),
        ('non-technical', 'Non-Technical'),
        ('data', 'Data'),
        ('infrastructure', 'Infrastructure'),
        ('reports', 'Reports'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='resources_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

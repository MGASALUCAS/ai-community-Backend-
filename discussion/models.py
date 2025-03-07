from django.db import models
from django.conf import settings

class Discussion(models.Model):
    CATEGORIES = [
        ('career', 'Career'),
        ('connect', 'Connect'),
        ('data', 'Data'),
        ('help', 'Help'),
        ('platform', 'Platform'),
    ]
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    topic = models.CharField(max_length=255)
    caption = models.TextField()
    reference_link = models.URLField(blank=True, null=True, default='NIL')
    created_at = models.DateTimeField(auto_now_add=True)

class DiscussionComment(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class DiscussionLike(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

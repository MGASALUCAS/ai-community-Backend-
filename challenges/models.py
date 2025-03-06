from django.db import models

class Challenge(models.Model):
    CHALLENGE_TYPES = [
        ('paid', 'Paid'),
        ('knowledge', 'Knowledge')
    ]
    
    INDUSTRIES = [
        ('finance', 'Finance'),
        ('agriculture', 'Agriculture'),
        ('healthcare', 'Healthcare'),
        ('security', 'Security'),
        ('education', 'Education'),
        ('business', 'Business'),
        ('other', 'Other')
    ]
    
    name = models.CharField(max_length=255)
    host_phone = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin_profile = models.URLField()
    description = models.TextField()
    host_name = models.CharField(max_length=255)
    evaluation_details = models.TextField()
    challenge_type = models.CharField(max_length=10, choices=CHALLENGE_TYPES)
    start_date = models.DateField()
    close_date = models.DateField()
    industry = models.CharField(max_length=20, choices=INDUSTRIES)
    poster_image = models.ImageField(upload_to='challenge_posters/')
    prize = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

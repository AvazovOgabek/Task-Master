from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default-avatar-icon-of-social-media-user-vector.jpeg')
    location = models.CharField(max_length=100, blank=True)
    is_expected = models.IntegerField(default=0) 
    done = models.IntegerField(default=0) 
    deleted = models.IntegerField(default=0)
    tasks_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username

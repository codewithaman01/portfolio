# models.py
from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.created_at}"

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # Add this line

    def __str__(self):
        return self.name

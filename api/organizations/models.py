from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_expired = models.BooleanField(default=False)

    def create_user(self):
        pass
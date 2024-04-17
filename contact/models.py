from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=212)
    last_name = models.CharField(max_length=212)
    email = models.EmailField()
    tel_number = models.CharField(max_length=212)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
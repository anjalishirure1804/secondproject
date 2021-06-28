from django.db import models

class Contact(models.Model):
    username=models.CharField(max_length=34)
    email=models.EmailField()
    contact=models.CharField(max_length=10)
    dob=models.DateField()

    def __str__(self):
        return self.username
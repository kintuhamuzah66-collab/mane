from django.db import models

class Member(models.Model):
    registration_number = models.CharField(max_length=16)
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
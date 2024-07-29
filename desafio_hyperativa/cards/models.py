from django.db import models

# from django_cryptography.fields import encrypt


class Card(models.Model):
    name = models.CharField(max_length=29)
    card_number = models.CharField(max_length=255, blank=False, null=False)


class CardsBatch(models.Model):
    file = models.FileField(upload_to="uploads/")

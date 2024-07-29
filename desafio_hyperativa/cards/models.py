from django.conf import settings
from django.db import models
from encrypted_fields import fields
from .validators import validate_file_extension


class Card(models.Model):
    name = models.CharField(max_length=29)
    _card_number_data = fields.EncryptedCharField(max_length=255, editable=False)
    card_number = fields.SearchField(
        hash_key=settings.FIELD_ENCRYPTION_KEYS[0],
        encrypted_field_name="_card_number_data",
    )


class CardsBatch(models.Model):
    file = models.FileField(upload_to="uploads/", validators=[validate_file_extension])

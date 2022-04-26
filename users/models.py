from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """ User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    photo = models.ImageField(upload_to="users/photo", blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, default=GENDER_OTHER)
    bio = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    credit_user = models.BooleanField(default=False)

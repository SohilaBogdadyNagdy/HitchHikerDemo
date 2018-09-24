from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField, IntegerField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), max_length=255)
    country = CharField(_("Country of User"), blank=True, max_length=30)
    email = EmailField(_("E-mail of User"), blank=False, max_length=30)
    password = CharField(_("Account Password"), blank=False, max_length=30)
    image = ImageField(_("User profile image"), blank=True)
    age = IntegerField(_("User Age"),blank=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

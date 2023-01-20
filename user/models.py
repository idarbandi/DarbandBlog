from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You Must Provide an Email Address'))
        email = self.normalize_email(email)
        user = self.model(user_name=user_name, email=email,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('super user must be assigned to isstaff=True.')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('super user must be assigned to issuperuser=True.')

        return self.create_user(email, user_name, first_name, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    user_name = models.CharField(_('user name'), max_length=150, unique=True)
    first_name = models.CharField(_('first name'), max_length=20, blank=True)
    start_date = models.DateTimeField(_('user join date'), auto_now_add=True)
    about = models.TextField(_('about user'), blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name']

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
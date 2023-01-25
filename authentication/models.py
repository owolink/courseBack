from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField( verbose_name='Email', max_length=255, unique=True)
    first_name = models.CharField( verbose_name='Name', max_length=255)
    last_name = models.CharField(verbose_name='Surname', max_length=255)
    photo = models.ImageField(verbose_name='Photo', upload_to='users/photos')
    bio = models.TextField(verbose_name='About')

    is_active = models.BooleanField(verbose_name='Activated', default=False)
    is_staff = models.BooleanField(verbose_name='Staff', default=False)
    is_superuser = models.BooleanField(verbose_name='Admin', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    objects = UserManager()

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
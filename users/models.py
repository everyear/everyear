from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        """ Creates and Save a User with the given email, nickname and password """
        if not email:
            raise ValueError('이메일 계정은 필수 입니다.')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, nickname=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(
            email=email,
            nickname=nickname,
            password=password,
            **extra_fields
        )

        user.is_admin = True
        user.save(using=self._db)

        return user


class Generaions(models.IntegerChoices):
    first = 1, _("1기")
    second = 2, _("2기")


class InterestingAt(models.TextChoices):
    BACKEND = 'BACKEND', _('Backend-end')
    FRONTEND = 'FRONTEND', _('Front-end')
    MLOPS = 'MLOPS', _('MLOps')
    DS = 'DS', _('Data Scientists')
    pass


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='email'
    )
    profile = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/profile/',
        verbose_name='profile'
    )
    nickname = models.CharField(
        max_length=10,
        blank=False, 
        unique=True,
        verbose_name='nickname'
    )
    name = models.CharField(
        max_length=10,
        verbose_name='name'
    )
    generation = models.IntegerField(
        null=True,
        blank=True,
        choices=Generaions.choices,
        verbose_name='gen'
    )

    birth = models.DateField(
        null=True,
        blank=True
    )
    interesting = models.CharField(
        null=True, blank=True,
        max_length=20,
        choices=InterestingAt.choices,
        verbose_name='interesting'
    )
    github = models.URLField(
        null=True, blank=True,
        max_length=200
    )
    blog = models.URLField(
        null=True, blank=True,
        max_length=200
    )
    bio = models.CharField(
        null=True, blank=True,
        max_length=100,
        verbose_name='bio'
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

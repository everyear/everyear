from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Generaions(models.IntegerChoices):
    first = 1, _("1기")
    second = 2, _("2기")


class InterestingAt(models.TextChoices):
    BACKEND = 'BACKEND', _('Backend-end')
    FRONTEND = 'FRONTEND', _('Front-end')
    MLOPS = 'MLOPS', _('MLOps')
    DS = 'DS', _('Data Scientists')
    


class User(AbstractUser):
    profile = models.ImageField(
        null=True,
        blank=True,
        upload_to='images/profile/',
        verbose_name='profile',
        help_text=_('이미지 형태의 프로필 사진입니다.')
    )

    email = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='email',
        help_text=_('이메일')
    )
    
    nickname = models.CharField(
        max_length=10,
        blank=False, 
        unique=True,
        verbose_name='nickname',
        help_text=_('웹상에서 사용할 닉네임입니다.')
    )
    name = models.CharField(
        max_length=10,
        verbose_name='name',
        help_text=_('사용자 이름')
    )

    generation = models.IntegerField(
        null=True,
        blank=True,
        choices=Generaions.choices,
        verbose_name='generation',
        help_text=_('기수(옵션)')
    )

    birth = models.DateField(
        null=True,
        blank=True,
        help_text=_('생일(옵션)')
    )
    interesting = models.CharField(
        null=True, blank=True,
        max_length=20,
        choices=InterestingAt.choices,
        verbose_name='interesting',
        help_text=_('흥미(옵션)')
    )
    github = models.URLField(
        null=True, blank=True,
        max_length=200,
        help_text=_('깃허브 주소(옵션)')
    )
    blog = models.URLField(
        null=True, blank=True,
        max_length=200,
        help_text=_('블로그 주소(옵션)')
    )
    bio = models.CharField(
        null=True, blank=True,
        max_length=100,
        verbose_name='bio',
        help_text=_('자기소개(옵션)')
    )
    pass
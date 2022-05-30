# Generated by Django 4.0.4 on 2022-05-28 10:35

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile', models.ImageField(blank=True, help_text='이미지 형태의 프로필 사진입니다.', null=True, upload_to='images/profile/', verbose_name='profile')),
                ('email', models.CharField(help_text='이메일', max_length=255, unique=True, verbose_name='email')),
                ('nickname', models.CharField(help_text='웹상에서 사용할 닉네임입니다.', max_length=10, unique=True, verbose_name='nickname')),
                ('name', models.CharField(help_text='사용자 이름', max_length=10, verbose_name='name')),
                ('generation', models.IntegerField(blank=True, choices=[(1, '1기'), (2, '2기')], help_text='기수(옵션)', null=True, verbose_name='generation')),
                ('birth', models.DateField(blank=True, help_text='생일(옵션)', null=True)),
                ('interesting', models.CharField(blank=True, choices=[('BACKEND', 'Backend-end'), ('FRONTEND', 'Front-end'), ('MLOPS', 'MLOps'), ('DS', 'Data Scientists')], help_text='흥미(옵션)', max_length=20, null=True, verbose_name='interesting')),
                ('github', models.URLField(blank=True, help_text='깃허브 주소(옵션)', null=True)),
                ('blog', models.URLField(blank=True, help_text='블로그 주소(옵션)', null=True)),
                ('bio', models.CharField(blank=True, help_text='자기소개(옵션)', max_length=100, null=True, verbose_name='bio')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

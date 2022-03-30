# Generated by Django 3.2.11 on 2022-03-29 17:20

from django.db import migrations, models


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
                ('email', models.CharField(max_length=255, unique=True, verbose_name='email')),
                ('profile', models.ImageField(blank=True, null=True, upload_to='images/profile/', verbose_name='profile')),
                ('nickname', models.CharField(max_length=10, unique=True, verbose_name='nickname')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('generation', models.IntegerField(blank=True, choices=[(1, '1기'), (2, '2기')], null=True, verbose_name='gen')),
                ('birth', models.DateField(blank=True, null=True)),
                ('interesting', models.CharField(blank=True, choices=[('BACKEND', 'Backend-end'), ('FRONTEND', 'Front-end'), ('MLOPS', 'MLOps'), ('DS', 'Data Scientists')], max_length=20, null=True, verbose_name='interesting')),
                ('github', models.URLField(blank=True, null=True)),
                ('blog', models.URLField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, max_length=100, null=True, verbose_name='bio')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    list_display = ('username', 'email', 'nickname',  'generation', 'interesting')
    list_filter = ('generation', 'interesting')

    fieldsets = (
        ('user info', {'fields':('profile', 'nickname', 'name', 'generation', 'birth', 'interesting', 'github', 'blog', 'bio')}),
    ) + UserAdmin.fieldsets
    
    

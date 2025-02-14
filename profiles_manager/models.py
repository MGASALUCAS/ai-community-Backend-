from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.



class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    ROLE_CHOICES = [
        ('system_admin', 'System Admin'),
        ('administrator', 'Administrator'),
        ('contributor', 'Contributor'),
        ('user', 'Normal User'),
    ]

    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    def assign_role(self):
        """Assigns a default role-based group to the user upon creation."""
        group, created = Group.objects.get_or_create(name=self.get_role_display())
        self.groups.add(group)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    



from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Role & Permissions'), {'fields': ('role', 'is_staff', 'is_active', 'groups')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_staff', 'is_active'),
        }),
    )

    def save_model(self, request, obj, form, change):
        """Automatically assign a user to the correct group when saving."""
        obj.assign_role()
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, CustomUserAdmin)




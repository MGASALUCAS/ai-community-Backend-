from django.contrib import admin
from .admin_site import admin_site
from .models import CustomUser, CustomUserAdmin

admin_site.register(CustomUser, CustomUserAdmin)




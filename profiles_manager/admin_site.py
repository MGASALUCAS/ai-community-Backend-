from django.contrib.admin import AdminSite
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.urls import path

CustomUser = get_user_model()

class MyAdminSite(AdminSite):
    site_header = "Admin Dashboard"
    site_title = "Admin Panel"
    index_title = "User & Role Management"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('user-stats/', self.admin_view(self.user_count_view), name="user-stats"),
        ]
        return custom_urls + urls

    def user_count_view(self, request):
        total_users = CustomUser.objects.count()
        system_admins = CustomUser.objects.filter(role="system_admin").count()
        administrators = CustomUser.objects.filter(role="administrator").count()
        contributors = CustomUser.objects.filter(role="contributor").count()
        normal_users = CustomUser.objects.filter(role="user").count()

        return HttpResponse(f"""
            <h2>Total Registered Users: {total_users}</h2>
            <ul>
                <li>System Admins: {system_admins}</li>
                <li>Administrators: {administrators}</li>
                <li>Contributors: {contributors}</li>
                <li>Normal Users: {normal_users}</li>
            </ul>
        """)

admin_site = MyAdminSite(name="custom_admin")


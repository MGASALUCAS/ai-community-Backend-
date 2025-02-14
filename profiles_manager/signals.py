from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.apps import apps

CustomUser = get_user_model()

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == "profiles_manager":  # Ensure it's our app
        # Define Groups
        groups = {
            "System Admin": [],
            "Administrator": [],
            "Contributor": [],
            "Normal User": [],
        }

        # Assign Permissions
        for group_name in groups.keys():
            group, created = Group.objects.get_or_create(name=group_name)

            # Give full permissions to System Admin
            if group_name == "System Admin":
                group.permissions.set(Permission.objects.all())  # All Permissions

            # Give user management permissions to Administrators
            elif group_name == "Administrator":
                content_types = ContentType.objects.get_for_models(CustomUser)
                user_permissions = Permission.objects.filter(content_type=content_types[CustomUser])
                group.permissions.set(user_permissions)

            # Contributors can access but not modify
            elif group_name == "Contributor":
                pass  # Can assign specific permissions later

            # Normal Users have default permissions
            elif group_name == "Normal User":
                pass  # No special permissions

            group.save()

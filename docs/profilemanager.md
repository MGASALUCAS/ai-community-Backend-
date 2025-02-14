views.py
--------

This module contains the views for the profile management app, utilizing Django REST framework's generic views to handle user-related operations.

Classes:
    - SignupView: Handles user registration.
    - SigninView: Handles user authentication and token generation.
    - UpdateProfileView: Handles updating user profiles.
    - ForgotPasswordView: Handles password reset requests.

models.py
---------

This module defines the CustomUser model, which represents a user in the application with additional fields for gender and role.

Classes:
    - CustomUser: A model representing a user with fields for email, gender, role, and methods for role assignment.

admin.py
--------

This module registers the CustomUser model with the Django admin site, allowing for management of users through the admin interface.

Classes:
    - CustomUserAdmin: Customizes the admin interface for the CustomUser model, including list display, filters, and search fields.

admin_site.py
-------------

This module defines a custom admin site for enhanced user and role management.

Classes:
    - MyAdminSite: Custom admin site with additional views and configurations.

serializers.py
--------------

This module contains serializers for the profile management app, used to validate and transform data for API requests and responses.

Classes:
    - SignupSerializer: Validates and creates new users.
    - SigninSerializer: Validates user credentials for authentication.
    - UpdateProfileSerializer: Validates and updates user profile data.
    - ForgotPasswordSerializer: Validates email for password reset requests.

signals.py
----------

This module defines signals to automatically create user groups and assign permissions after migrations.

Functions:
    - create_user_groups: Creates predefined user groups and assigns permissions.
"""
views.py
--------

This module contains the views for the Resource app, utilizing Django REST framework's generic views to handle CRUD operations.

Classes:
    - ResourceListCreateView: Handles listing all resources and creating a new resource.
    - ResourceDetailView: Handles retrieving, updating, or deleting a specific resource.

models.py
---------

This module defines the Resource model, which represents a resource in the application.

Classes:
    - Resource: A model representing a resource with fields for title, description, image, category, link, and created_at.

admin.py
--------

This module registers the Resource model with the Django admin site, allowing for management of resources through the admin interface.

Classes:
    - ResourceAdmin: Customizes the admin interface for the Resource model, including list display and search fields.
"""
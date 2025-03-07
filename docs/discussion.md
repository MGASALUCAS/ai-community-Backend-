
# Discussion App Documentation

## Overview

The `discussion` app allows users to create discussion posts, comment on discussions, and like discussions. The app provides API endpoints to manage discussions, comments, and likes.

## Models

### Discussion

- `author`: ForeignKey to the user who created the discussion.
- `title`: Title of the discussion.
- `category`: Category of the discussion (career, connect, data, help, platform).
- `topic`: Topic of the discussion.
- `caption`: Caption of the discussion.
- `reference_link`: Optional reference link for the discussion.
- `created_at`: Timestamp when the discussion was created.

### DiscussionComment

- `discussion`: ForeignKey to the discussion being commented on.
- `author`: ForeignKey to the user who created the comment.
- `text`: Text of the comment.
- `created_at`: Timestamp when the comment was created.

### DiscussionLike

- `discussion`: ForeignKey to the discussion being liked.
- `user`: ForeignKey to the user who liked the discussion.
- `created_at`: Timestamp when the like was created.

## Serializers

### DiscussionSerializer

Serializes all fields of the `Discussion` model.

### DiscussionCommentSerializer

Serializes all fields of the `DiscussionComment` model.

### DiscussionLikeSerializer

Serializes all fields of the `DiscussionLike` model.

## Views

### DiscussionViewSet

- Handles CRUD operations for discussions.
- Only authenticated users can create discussions.

### DiscussionCommentViewSet

- Handles CRUD operations for discussion comments.
- Only authenticated users can create comments.

### DiscussionLikeViewSet

- Handles CRUD operations for discussion likes.
- Only authenticated users can like discussions.

## URLs

The `discussion` app URLs are included in the project's URL configuration.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiscussionViewSet, DiscussionCommentViewSet, DiscussionLikeViewSet

router = DefaultRouter()
router.register(r'discussions', DiscussionViewSet)
router.register(r'discussion-comments', DiscussionCommentViewSet)
router.register(r'discussion-likes', DiscussionLikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## API Endpoints

### Discussions

- **GET /api/discussions/**: Retrieve a list of discussions.
- **POST /api/discussions/**: Create a new discussion.
- **GET /api/discussions/{id}/**: Retrieve a specific discussion.
- **PUT /api/discussions/{id}/**: Update a specific discussion.
- **DELETE /api/discussions/{id}/**: Delete a specific discussion.

### Discussion Comments

- **GET /api/discussion-comments/**: Retrieve a list of discussion comments.
- **POST /api/discussion-comments/**: Create a new discussion comment.
- **GET /api/discussion-comments/{id}/**: Retrieve a specific discussion comment.
- **PUT /api/discussion-comments/{id}/**: Update a specific discussion comment.
- **DELETE /api/discussion-comments/{id}/**: Delete a specific discussion comment.

### Discussion Likes

- **GET /api/discussion-likes/**: Retrieve a list of discussion likes.
- **POST /api/discussion-likes/**: Create a new discussion like.
- **GET /api/discussion-likes/{id}/**: Retrieve a specific discussion like.
- **PUT /api/discussion-likes/{id}/**: Update a specific discussion like.
- **DELETE /api/discussion-likes/{id}/**: Delete a specific discussion like.

## Sample Dummy Data

### Discussion

```json
{
    "author": 1,
    "title": "How to get started with AI?",
    "category": "career",
    "topic": "AI Basics",
    "caption": "Looking for resources to get started with AI.",
    "reference_link": "http://example.com/ai-resources",
    "created_at": "2023-10-01T12:00:00Z"
}
```

### Discussion Comment

```json
{
    "discussion": 1,
    "author": 2,
    "text": "Check out this course on Coursera!",
    "created_at": "2023-10-01T13:00:00Z"
}
```

### Discussion Like

```json
{
    "discussion": 1,
    "user": 3,
    "created_at": "2023-10-01T14:00:00Z"
}
```

## Admin Registration

The `Discussion`, `DiscussionComment`, and `DiscussionLike` models are registered in the Django admin interface.

```python
from django.contrib import admin
from .models import Discussion, DiscussionComment, DiscussionLike

admin.site.register(Discussion)
admin.site.register(DiscussionComment)
admin.site.register(DiscussionLike)
```

## Permissions

All authenticated users can create discussions, comments, and likes.

## Conclusion

The `discussion` app provides a comprehensive API for managing discussions, comments, and likes. This documentation covers the models, serializers, views, URLs, API endpoints, sample data, and admin registration.

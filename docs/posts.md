
# Posts App Documentation

## Overview

The `posts` app manages user posts, comments, and likes. Only users with the `contributor` role can create posts. The app provides API endpoints to manage posts, comments, and likes.

## Models

### Post

- `author`: ForeignKey to the user who created the post.
- `name`: Name of the post.
- `post_type`: Type of the post (blog, newsletter, talks & podcast, other).
- `tags`: Tags associated with the post.
- `caption`: Caption of the post.
- `link`: Link to the post.
- `media`: Media file associated with the post.
- `created_at`: Timestamp when the post was created.

### Comment

- `post`: ForeignKey to the post being commented on.
- `author`: ForeignKey to the user who created the comment.
- `text`: Text of the comment.
- `created_at`: Timestamp when the comment was created.

### Like

- `post`: ForeignKey to the post being liked.
- `user`: ForeignKey to the user who liked the post.
- `created_at`: Timestamp when the like was created.

## Serializers

### PostSerializer

Serializes all fields of the `Post` model.

### CommentSerializer

Serializes all fields of the `Comment` model.

### LikeSerializer

Serializes all fields of the `Like` model.

## Views

### IsContributor

Custom permission class to check if the user is a contributor.

### PostViewSet

- Handles CRUD operations for posts.
- Only authenticated users with the `contributor` role can create posts.

### CommentViewSet

- Handles CRUD operations for comments.
- Only authenticated users can create comments.

### LikeViewSet

- Handles CRUD operations for likes.
- Only authenticated users can like posts.

## URLs

The `posts` app URLs are included in the project's URL configuration.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

## API Endpoints

### Posts

- **GET /api/posts/**: Retrieve a list of posts.
- **POST /api/posts/**: Create a new post (requires contributor role).
- **GET /api/posts/{id}/**: Retrieve a specific post.
- **PUT /api/posts/{id}/**: Update a specific post.
- **DELETE /api/posts/{id}/**: Delete a specific post.

### Comments

- **GET /api/comments/**: Retrieve a list of comments.
- **POST /api/comments/**: Create a new comment.
- **GET /api/comments/{id}/**: Retrieve a specific comment.
- **PUT /api/comments/{id}/**: Update a specific comment.
- **DELETE /api/comments/{id}/**: Delete a specific comment.

### Likes

- **GET /api/likes/**: Retrieve a list of likes.
- **POST /api/likes/**: Create a new like.
- **GET /api/likes/{id}/**: Retrieve a specific like.
- **PUT /api/likes/{id}/**: Update a specific like.
- **DELETE /api/likes/{id}/**: Delete a specific like.

## Sample Dummy Data

### Post

```json
{
    "author": 1,
    "name": "Introduction to Quantum Computing",
    "post_type": "blog",
    "tags": "#quantum #computing",
    "caption": "An introductory blog on quantum computing.",
    "link": "http://example.com/quantum-computing",
    "media": "path/to/media.jpg",
    "created_at": "2023-10-01T12:00:00Z"
}
```

### Comment

```json
{
    "post": 1,
    "author": 2,
    "text": "Great article on quantum computing!",
    "created_at": "2023-10-01T13:00:00Z"
}
```

### Like

```json
{
    "post": 1,
    "user": 3,
    "created_at": "2023-10-01T14:00:00Z"
}
```

## Admin Registration

The `Post`, `Comment`, and `Like` models are registered in the Django admin interface.

```python
from django.contrib import admin
from .models import Post, Comment, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
```

## Permissions

Only users with the `contributor` role can create posts. All authenticated users can create comments and likes.

## Conclusion

The `posts` app provides a comprehensive API for managing posts, comments, and likes, with appropriate permissions for contributors. This documentation covers the models, serializers, views, URLs, API endpoints, sample data, and admin registration.

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

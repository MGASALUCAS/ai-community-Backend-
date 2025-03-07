from django.contrib import admin
from .models import Discussion, DiscussionComment, DiscussionLike

admin.site.register(Discussion)
admin.site.register(DiscussionComment)
admin.site.register(DiscussionLike)

from django.contrib import admin

from .models import Comment

# to get the comments from admin so we can mod them
admin.site.register(Comment)

from django.db import models
# using to get the time comment was added
from django.utils import timezone

# model for the guestbook index page
class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)
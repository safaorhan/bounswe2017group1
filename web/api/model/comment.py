from __future__ import unicode_literals

from django.db import models
from profile import Profile
from heritage import Heritage

class Comment(models.Model):
    text = models.TextField()
    heritage = models.ForeignKey(Heritage)
    creator = models.ForeignKey(Profile)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/user_{0}/{1}'.format(instance.user, filename)

class Document(models.Model):
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    user = "default"
    docfile = models.FileField(upload_to=user_directory_path)

    #def __init__(self, *args, **kwargs):
    #    self.user = args[0]
    #    return super(Document, self).__init__(*args, **kwargs)

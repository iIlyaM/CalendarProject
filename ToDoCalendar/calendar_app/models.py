from django.db import models


class UserAuth(models.Model):
    email = models.CharField(max_length=150, unique=True, null=False, blank=False)
    password = models.CharField(max_length=150, null=False, blank=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)


class UserData(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
#   group_id =
    user_auth = models.OneToOneField(UserAuth, on_delete=models.CASCADE)


class UserRecord(models.Model):
    date = models.DateField(null=False, blank=False)
    record_title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    record_text = models.TextField(max_length=10000, null=True, blank=True)
    author_id = models.ForeignKey(UserData, on_delete=models.CASCADE)

from django.db import models


class ApplicationUser(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.JSONField()
    login = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    roles = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    token = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)


class ImportEvents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.JSONField()
    number_of_events = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)


class EventLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.JSONField()
    application_user_id = models.ForeignKey(
        ApplicationUser, on_delete=models.CASCADE)
    import_events_id = models.ForeignKey(
        ImportEvents, on_delete=models.CASCADE)
    comments_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    quest = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    note = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now=True)
    checksum = models.BigIntegerField()

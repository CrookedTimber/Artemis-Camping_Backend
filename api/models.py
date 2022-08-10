from django.db import models
from datetime import datetime

# from django.contrib.auth.models import User

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    destination_latitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        null=False,
        blank=False,
    )
    destination_longitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        null=False,
        blank=False,
    )
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    creation_date = models.DateField(default=datetime.now)
    last_update = models.DateField(default=datetime.now)
    last_updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="last_updated_by"
    )
    public = models.BooleanField("Public", default=False)

    class Meta:

        ordering = ["-creation_date"]


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=1024)
    gmaps_id = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        null=False,
        blank=False,
    )
    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        null=False,
        blank=False,
    )
    retrieval_date = models.DateField(auto_now_add=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

    class Meta:

        ordering = ["-retrieval_date"]


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    join_date = models.DateField(default=datetime.now)
    name = models.CharField(max_length=20)
    member = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="member_in_trip"
    )
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

    update_date = models.DateField(default=datetime.now)
    create_member_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="create_member_user"
    )
    update_member_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="update_member_user"
    )


class Checklist(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField(max_length=20)
    remark = models.TextField(max_length=1024)
    user_in_charge = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_in_charge"
    )
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_checklist_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="create_checklist_user"
    )
    update_checklist_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="update_checklist_user"
    )
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)


class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField(max_length=20)
    price = models.IntegerField(blank=True, null=False, default=0)
    remark = models.TextField(max_length=1024)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_budget_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="create_budget_user"
    )
    update_budget_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="update_budget_user"
    )
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    message_body = models.TextField(max_length=1024)
    create_date = models.DateField(default=datetime.now)
    create_message_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)


class Setting(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField(max_length=20)
    value = models.TextField(max_length=20)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_setting_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="create_setting_user"
    )
    update_setting_member = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="update_setting_member"
    )

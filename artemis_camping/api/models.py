from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class TripDetail(models.Model):
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
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now_add=True)
    last_updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, related_name="last_updated_by"
    )
    public = models.BooleanField("Public", default=False)

    class Meta:

        ordering = ["-creation_date"]
        
        
class Place(models.Model):
    name = models.TextField(max_length=1024)
    place_id = models.CharField(max_length=50)
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
    # trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    retrieval_date = models.DateField(auto_now_add=True)
    
    class Meta:

        ordering = ["-retrieval_date"]
        

# Create your models here.

class Trip(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20)
    public = models.BooleanField(default=False)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_trip_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_trip_user')
    update_trip_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_trip_user')

class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField(max_length=20)
    price = models.IntegerField(blank=True, null=False, default=0)
    remark = models.TextField(max_length=1024)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_budget_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_budget_user')
    update_budget_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_budget_user')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

class Checklist(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.TextField(max_length=20)
    remark = models.TextField(max_length=1024)
    user_in_charge = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_in_charge')
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_checklist_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_checklist_user')
    update_checklist_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_checklist_user')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

class Duration(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_duration_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_duration_user')
    update_duration_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_duration_user')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

class Map(models.Model):
    id = models.AutoField(primary_key=True)
    location_from = models.TextField(max_length=500)
    location_to = models.TextField(max_length=500)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_map_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_map_user')
    update_map_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_map_user')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateField(default=datetime.now)
    update_date = models.DateField(default=datetime.now)
    create_member_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_member_user')
    update_member_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_member_user')
    member_in_trip = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='member_in_trip')
    trip = models.ForeignKey(Trip, on_delete=models.SET_NULL, null=True)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
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
    create_setting_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='create_setting_user')
    update_setting_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='update_setting_member')


    """Uses coordinates for working with Google Places API and Open Weather API"""
    """Dates data needs to be adjusted to work with Open Weather API """
class GoogleMap(models.Model):
    name = models.CharField("Trip Name", max_length=50)
    start_latitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    start_longitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    destination_latitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    destination_longitude = models.DecimalField(
        max_digits=11, decimal_places=7, null=False, blank=True
    )
    start_date = models.DateField()
    end_date = models.DateField()
    difficulty = models.IntegerChoices("Difficulty", "Easy Medium Hard")
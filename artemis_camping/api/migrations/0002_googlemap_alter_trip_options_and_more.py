# Generated by Django 4.1 on 2022-08-08 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="GoogleMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Trip Name")),
                (
                    "start_latitude",
                    models.DecimalField(blank=True, decimal_places=7, max_digits=11),
                ),
                (
                    "start_longitude",
                    models.DecimalField(blank=True, decimal_places=7, max_digits=11),
                ),
                (
                    "destination_latitude",
                    models.DecimalField(blank=True, decimal_places=7, max_digits=11),
                ),
                (
                    "destination_longitude",
                    models.DecimalField(blank=True, decimal_places=7, max_digits=11),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name="trip",
            options={},
        ),
        migrations.RemoveField(
            model_name="trip",
            name="creation_date",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="creator",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="destination_latitude",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="destination_longitude",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="last_update",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="last_updated_by",
        ),
        migrations.RemoveField(
            model_name="trip",
            name="start_date",
        ),
        migrations.AddField(
            model_name="trip",
            name="create_date",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="trip",
            name="create_trip_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="create_trip_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="trip",
            name="update_date",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="trip",
            name="update_trip_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="update_trip_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="trip",
            name="name",
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name="trip",
            name="public",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="TripDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "destination_latitude",
                    models.DecimalField(decimal_places=15, max_digits=20),
                ),
                (
                    "destination_longitude",
                    models.DecimalField(decimal_places=15, max_digits=20),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("creation_date", models.DateField(auto_now_add=True)),
                ("last_update", models.DateField(auto_now_add=True)),
                ("public", models.BooleanField(default=False, verbose_name="Public")),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "last_updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="last_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-creation_date"],
            },
        ),
        migrations.CreateModel(
            name="Setting",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("item", models.TextField(max_length=20)),
                ("value", models.TextField(max_length=20)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_setting_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_setting_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "update_setting_member",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_setting_member",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message_body", models.TextField(max_length=1024)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_message_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Member",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_member_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_member_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "member_in_trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="member_in_trip",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
                (
                    "update_member_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_member_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Map",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("location_from", models.TextField(max_length=500)),
                ("location_to", models.TextField(max_length=500)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_map_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_map_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
                (
                    "update_map_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_map_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Duration",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("start_date", models.DateField(default=datetime.datetime.now)),
                ("end_date", models.DateField(default=datetime.datetime.now)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_duration_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_duration_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
                (
                    "update_duration_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_duration_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Checklist",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("item", models.TextField(max_length=20)),
                ("remark", models.TextField(max_length=1024)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_checklist_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_checklist_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
                (
                    "update_checklist_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_checklist_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user_in_charge",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user_in_charge",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Budget",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("item", models.TextField(max_length=20)),
                ("price", models.IntegerField(blank=True, default=0)),
                ("remark", models.TextField(max_length=1024)),
                ("create_date", models.DateField(default=datetime.datetime.now)),
                ("update_date", models.DateField(default=datetime.datetime.now)),
                (
                    "create_budget_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="create_budget_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "trip",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="api.trip",
                    ),
                ),
                (
                    "update_budget_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="update_budget_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
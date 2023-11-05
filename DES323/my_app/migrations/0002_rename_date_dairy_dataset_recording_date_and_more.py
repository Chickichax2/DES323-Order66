# Generated by Django 4.2.7 on 2023-11-05 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dairy_dataset",
            old_name="date",
            new_name="recording_date",
        ),
        migrations.AddField(
            model_name="dairy_dataset",
            name="added_by",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="dairy_dataset",
            name="added_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="dairy_dataset",
            name="farm_size",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="dairy_dataset",
            name="product_type",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="dairy_dataset",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]

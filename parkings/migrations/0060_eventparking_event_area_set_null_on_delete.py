# Generated by Django 2.2.15 on 2023-12-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0059_eventarea_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventparking',
            name='event_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_parkings', to='parkings.EventArea', verbose_name='event area'),
        ),
    ]
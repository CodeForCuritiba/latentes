# Generated by Django 3.0.3 on 2020-02-13 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quilombola', '0008_community_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='phase_no',
        ),
    ]

# Generated by Django 3.0 on 2019-12-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quilombola', '0003_auto_20191229_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='area',
            field=models.DecimalField(decimal_places=8, max_digits=19, verbose_name='area'),
        ),
    ]
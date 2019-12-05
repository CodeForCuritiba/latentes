# Generated by Django 3.0 on 2019-12-05 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_no', models.PositiveSmallIntegerField(verbose_name='phase number')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('area', models.DecimalField(decimal_places=4, max_digits=4, verbose_name='area')),
                ('family_no', models.PositiveIntegerField(default=0, verbose_name='number of families')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='communities', to='base.City', verbose_name='city')),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpapp', '0003_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='predonation',
            name='accno',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predonation',
            name='bank',
            field=models.CharField(default=12, max_length=250),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]

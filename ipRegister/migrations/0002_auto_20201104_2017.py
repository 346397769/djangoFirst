# Generated by Django 3.1.2 on 2020-11-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipRegister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipregister',
            name='ip',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='ipregister',
            name='mac',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='ipregister',
            name='office',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='ipregister',
            name='phone',
            field=models.CharField(max_length=18, null=True),
        ),
    ]

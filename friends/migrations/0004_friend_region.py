# Generated by Django 3.2.16 on 2022-11-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_alter_friend_people_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='region',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
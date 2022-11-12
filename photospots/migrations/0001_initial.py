# Generated by Django 3.2.13 on 2022-11-12 00:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photospot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('photo_img', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like_users', models.ManyToManyField(related_name='like_photospots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-16 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ext_user', '0002_rename_profile_photo_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_pekerti_peserta',
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-17 07:27

from django.db import migrations, models
import pekerti.functions.function


class Migration(migrations.Migration):

    dependencies = [
        ('pekerti', '0002_auto_20211115_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='gelombang',
            name='is_full',
            field=models.BooleanField(blank=True, default=False, verbose_name='Apakah Sudah Penuh'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='link_kesanggupan',
            field=models.FileField(blank=True, upload_to=pekerti.functions.function.user_directory_path, validators=[pekerti.functions.function.validate_file_extension], verbose_name='Dokumen Kesanggupan'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='link_transfer',
            field=models.FileField(blank=True, upload_to=pekerti.functions.function.user_directory_path, validators=[pekerti.functions.function.validate_file_extension], verbose_name='Bukti Transfer'),
        ),
        migrations.AlterField(
            model_name='peserta',
            name='nidn',
            field=models.CharField(blank=True, max_length=10, verbose_name='NIDN'),
        ),
    ]
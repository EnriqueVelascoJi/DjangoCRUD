# Generated by Django 3.1.6 on 2021-02-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0002_auto_20210205_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='alumno', verbose_name='Fotografía'),
        ),
    ]

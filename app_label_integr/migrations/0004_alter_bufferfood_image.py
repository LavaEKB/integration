# Generated by Django 4.1 on 2022-08-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_label_integr', '0003_connectsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bufferfood',
            name='image',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='upload/images/food/', verbose_name='Изображение'),
        ),
    ]

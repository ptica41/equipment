# Generated by Django 5.0.7 on 2024-08-07 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='name_804',
            field=models.CharField(blank=True, null=True, verbose_name='Наименование в 804 приказе'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-25 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20181225_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='overlay_and_button_color',
            field=models.CharField(default='#cd9557', max_length=7),
        ),
    ]
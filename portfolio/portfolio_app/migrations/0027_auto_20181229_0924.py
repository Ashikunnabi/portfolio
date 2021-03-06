# Generated by Django 2.1.4 on 2018-12-29 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0026_index_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='footer',
            field=models.CharField(default='Copyright &copy; ashikunnabi.pythonanywhere.com | 2018', max_length=100),
        ),
        migrations.AlterField(
            model_name='index',
            name='user_status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=8),
        ),
    ]

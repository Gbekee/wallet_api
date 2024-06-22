# Generated by Django 5.0.6 on 2024-06-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_bank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bank',
        ),
        migrations.AddField(
            model_name='wallet',
            name='bank',
            field=models.CharField(default='World Bank', max_length=50),
        ),
    ]
# Generated by Django 5.0.6 on 2024-05-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_team_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.URLField(),
        ),
    ]

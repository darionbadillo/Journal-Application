# Generated by Django 4.2.7 on 2023-11-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='color',
            field=models.CharField(choices=[('blue', 'Blue'), ('yellow', 'Yellow'), ('black', 'Black'), ('pink', 'Pink')], default='black', max_length=10),
        ),
    ]

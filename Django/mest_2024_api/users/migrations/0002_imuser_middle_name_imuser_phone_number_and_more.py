# Generated by Django 5.0.1 on 2024-02-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='imuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='imuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AlterField(
            model_name='imuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=155),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_cohort_alter_classschedule_cohort'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cohort',
            old_name='title',
            new_name='name',
        ),
    ]
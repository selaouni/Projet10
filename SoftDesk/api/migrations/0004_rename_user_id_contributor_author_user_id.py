# Generated by Django 4.1.2 on 2022-11-08 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_issue_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='user_id',
            new_name='author_user_id',
        ),
    ]
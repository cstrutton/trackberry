# Generated by Django 4.0.4 on 2022-04-25 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor_menu', '0004_alter_supervisorsubmenuitem_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supervisorsubmenuitem',
            old_name='test',
            new_name='text',
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='text',
            new_name='title',
        ),
        migrations.AddField(
            model_name='service',
            name='summary',
            field=models.CharField(default=50, max_length=200),
            preserve_default=False,
        ),
    ]

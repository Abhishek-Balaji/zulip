# Generated by Django 2.2.10 on 2020-03-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0270_realmfilter_stream_ids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realmfilter',
            name='stream_ids',
            field=models.TextField(default='[]'),
        ),
    ]

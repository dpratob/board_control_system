# Generated by Django 5.1.4 on 2025-01-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0008_alter_boardpublication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardpublication',
            name='interaction',
            field=models.URLField(help_text='e.g., http://example.com', max_length=18),
        ),
    ]

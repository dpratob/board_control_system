# Generated by Django 5.1.4 on 2025-01-18 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_alter_board_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards_in_group', to='boards.group'),
        ),
    ]

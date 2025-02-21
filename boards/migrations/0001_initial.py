# Generated by Django 5.1.5 on 2025-02-14 18:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=6)),
                ('model', models.CharField(max_length=10)),
                ('resolution', models.CharField(help_text='e.g., ____x___', max_length=9)),
                ('size_inches', models.DecimalField(decimal_places=1, max_digits=3, validators=[django.core.validators.MinValueValidator(5)])),
            ],
            options={
                'verbose_name': 'Board Feature',
                'verbose_name_plural': 'Board Features',
                'db_table': 'board_feature',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(blank=True, upload_to='events/audios/')),
                ('graphic', models.ImageField(blank=True, upload_to='events/graphics/')),
                ('image', models.ImageField(blank=True, upload_to='events/images/')),
                ('video', models.FileField(blank=True, upload_to='events/videos/')),
                ('text', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'group',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=7)),
                ('last_name', models.CharField(max_length=8)),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'User'), (1, 'Admin')], default=0)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=10)),
                ('serial_number', models.CharField(max_length=8, unique=True)),
                ('section', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)])),
                ('is_active', models.BooleanField(default=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards_with_feature', to='boards.boardfeature')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards_in_group', to='boards.group')),
            ],
            options={
                'verbose_name': 'Board Master',
                'verbose_name_plural': 'Boards Master',
                'db_table': 'board',
            },
        ),
        migrations.CreateModel(
            name='BoardPublication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.FileField(upload_to='publication_files/')),
                ('description', models.CharField(max_length=27)),
                ('interaction', models.URLField(help_text='e.g., http://example.com', max_length=18)),
                ('duration', models.PositiveIntegerField(help_text='e.g., ___ min')),
                ('repetition_count', models.PositiveIntegerField(default=0)),
                ('current_cycle', models.PositiveIntegerField(default=0)),
                ('start_date', models.DateField(help_text='e.g., yyyy-mm-dd')),
                ('end_date', models.DateField(help_text='e.g., yyyy-mm-dd')),
                ('time', models.TimeField(help_text='e.g., HH:mm:ss')),
                ('role', models.PositiveSmallIntegerField(choices=[(0, 'Daily Unlimited'), (1, 'Scheduled with Repeats'), (2, 'User-Controlled Perpetual')], default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications_in_board', to='boards.board')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications_with_event', to='boards.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications_by_user', to='boards.user')),
            ],
            options={
                'verbose_name': 'Board Publication',
                'verbose_name_plural': 'Board Publications',
                'db_table': 'board_publication',
            },
        ),
    ]

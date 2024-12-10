# Generated by Django 5.1.3 on 2024-11-26 04:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='data',
            new_name='data_fim',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='processo',
        ),
        migrations.AddField(
            model_name='evento',
            name='data_inicio',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='evento',
            name='descricao',
            field=models.TextField(blank=True),
        ),
    ]

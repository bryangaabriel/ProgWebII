# Generated by Django 5.1.3 on 2024-11-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogados', '0002_remove_advogado_email_alter_advogado_especializacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advogado',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='advogado',
            name='telefone',
            field=models.CharField(default='00000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='especializacao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='advogado',
            name='oab',
            field=models.CharField(max_length=15),
        ),
    ]

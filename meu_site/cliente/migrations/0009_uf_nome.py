# Generated by Django 4.0.1 on 2022-02-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_alter_cliente_estcivil_alter_cliente_carro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uf',
            name='nome',
            field=models.CharField(default='', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]

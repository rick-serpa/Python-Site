# Generated by Django 4.0.1 on 2022-02-06 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_cliente_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='EstCivil',
            field=models.IntegerField(choices=[(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), (4, 'Viúvo(a)'), (5, 'Desquitado(a)'), (6, 'União Estável')], default=1),
        ),
        migrations.AddField(
            model_name='cliente',
            name='carro',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='filhos',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='renda',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]

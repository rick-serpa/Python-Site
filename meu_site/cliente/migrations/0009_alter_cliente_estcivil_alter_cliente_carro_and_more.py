# Generated by Django 4.0.1 on 2022-02-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0008_alter_cliente_estcivil_alter_cliente_carro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='EstCivil',
            field=models.IntegerField(blank=True, choices=[(1, 'Solteiro(a)'), (2, 'Casado(a)'), (3, 'Divorciado(a)'), (4, 'Viúvo(a)'), (5, 'Desquitado(a)'), (6, 'União Estável')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='carro',
            field=models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='filhos',
            field=models.CharField(blank=True, choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nasc',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='profissao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='renda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True),
        ),
    ]

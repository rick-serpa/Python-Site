# Generated by Django 4.0.1 on 2022-03-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0022_alter_cliente_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(blank=True, default='usuario@provedor.com.br', max_length=100),
            preserve_default=False,
        ),
    ]

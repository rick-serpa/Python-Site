# Generated by Django 4.0.1 on 2022-03-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0024_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nasc',
            field=models.DateField(default='2022-03-13'),
            preserve_default=False,
        ),
    ]

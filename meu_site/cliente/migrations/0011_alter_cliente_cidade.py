# Generated by Django 4.0.1 on 2022-02-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_uf_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.ManyToManyField(auto_created=True, to='cliente.Cidade'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-13 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0017_alter_cliente_cpfcnpj_alter_uf_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cidade'),
        ),
    ]

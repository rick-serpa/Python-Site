# Generated by Django 4.0.1 on 2022-01-30 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_categ'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
            options={
                'db_table': 'servico',
            },
        ),
    ]

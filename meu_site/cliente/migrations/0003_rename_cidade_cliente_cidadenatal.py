# Generated by Django 4.0.1 on 2022-02-06 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cidade_uf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cidade',
            new_name='cidadeNatal',
        ),
    ]
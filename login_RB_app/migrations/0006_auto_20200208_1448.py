# Generated by Django 2.2.9 on 2020-02-08 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_RB_app', '0005_auto_20200202_1040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='mikrotik',
            old_name='name',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='mikrotik',
            old_name='password',
            new_name='senha',
        ),
    ]

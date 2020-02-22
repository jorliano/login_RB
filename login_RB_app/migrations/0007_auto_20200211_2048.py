# Generated by Django 2.2.9 on 2020-02-11 23:48
from django.db import migrations, models

def popular_categorias(apps, schema_editor):
    Categoria = apps.get_model("login_RB_app","Categoria")
    c = Categoria(descricao='cliente')
    c.save()
    c2 = Categoria(descricao='concentrador')
    c2.save()
    c3 = Categoria(descricao='core')
    c3.save()

class Migration(migrations.Migration):

    dependencies = [
        ('login_RB_app', '0006_auto_20200208_1448'),
    ]

    operations = [
        migrations.RunPython(popular_categorias)
    ]
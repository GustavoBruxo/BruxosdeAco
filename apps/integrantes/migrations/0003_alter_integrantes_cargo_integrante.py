# Generated by Django 4.0.2 on 2022-03-04 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0002_remove_integrantes_data_saida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='integrantes',
            name='cargo_integrante',
            field=models.CharField(choices=[('1-PRE', 'Presidente'), ('2-VIC', 'Vice-Presidente'), ('3-DIR', 'Diretor'), ('4-INT', 'Integrante'), ('5-PRO', 'Prospero'), ('6-ESP', 'Espelho')], default='4-INT', max_length=5),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrantes', '0004_alter_integrantes_cargo_integrante'),
    ]

    operations = [
        migrations.CreateModel(
            name='InMemorian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/')),
                ('descricao', models.TextField()),
            ],
        ),
    ]

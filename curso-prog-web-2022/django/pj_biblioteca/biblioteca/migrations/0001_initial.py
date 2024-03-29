# Generated by Django 4.1 on 2022-08-23 22:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('biografia', models.TextField()),
                ('email', models.EmailField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'autores',
            },
        ),
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(11)])),
                ('editorial', models.TextField()),
                ('data', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'edições',
            },
        ),
        migrations.CreateModel(
            name='Linguagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'linguagens',
            },
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('introducao', models.TextField()),
                ('autor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
                ('edicao_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.edicao')),
                ('linguagem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.linguagem')),
            ],
            options={
                'verbose_name_plural': 'artigos',
            },
        ),
    ]

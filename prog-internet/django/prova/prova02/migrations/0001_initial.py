# Generated by Django 4.1 on 2022-08-18 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diretor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Diretores',
            },
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Funções',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('carteiraTrabalho', models.IntegerField()),
                ('dataContratacao', models.DateField()),
                ('salario', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Funcionários',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Gêneros',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Horários',
            },
        ),
        migrations.CreateModel(
            name='Premiacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('ano', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Premiações',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('capacidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeBR', models.CharField(max_length=45)),
                ('nomeEN', models.CharField(max_length=45)),
                ('anoLancamento', models.IntegerField()),
                ('sinopse', models.TextField()),
                ('diretor_idDiretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.diretor')),
                ('genero_idGenero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.genero')),
            ],
            options={
                'verbose_name_plural': 'Filmes',
            },
        ),
        migrations.CreateModel(
            name='HorarioTrabalhoFuncionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao_idfuncao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.funcao')),
                ('funcionario_idfuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.funcionario')),
                ('horario_idhorario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.horario')),
            ],
            options={
                'verbose_name_plural': 'Horários de trabalho de funcionários',
                'unique_together': {('horario_idhorario', 'funcionario_idfuncionario')},
            },
        ),
        migrations.CreateModel(
            name='FilmeTemPremiacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ganhou', models.BooleanField()),
                ('filme_idfilme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.filme')),
                ('premiacao_idpremiacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.premiacao')),
            ],
            options={
                'verbose_name_plural': 'Filmes que têm premiações',
                'unique_together': {('filme_idfilme', 'premiacao_idpremiacao')},
            },
        ),
        migrations.CreateModel(
            name='FilmeExibidoSala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme_idfilme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.filme')),
                ('horario_idhorario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.horario')),
                ('sala_idSala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova02.sala')),
            ],
            options={
                'unique_together': {('filme_idfilme', 'horario_idhorario', 'sala_idSala')},
            },
        ),
    ]

# Django - Passo a passo
## Atualizando pip
```pip install --upgrade pip```

## Criando e entrando no ambiente de desenvolvimento virtual
```python -m venv ./venv```
<br>
Entre em ./venv/Scripts e:
<br>
```activate```

## Instalando Django
```pip install django ```

## Iniciando projeto django
```django-admin startproject nomedoprojeto```

## Rodando servidor
```py manage.py runserver```

## Criando usuário
```py manage.py makemigrations```
```py manage.py migrate```
```py manage.py createsuperuser```
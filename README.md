# Relatório: Projeto de Cadastro de Clientes em Django
## Introdução
O Django é um framework web em Python que facilita o desenvolvimento de aplicações web robustas e escaláveis. Neste relatório, descreveremos um projeto prático de cadastro de clientes utilizando Django. O objetivo é criar uma aplicação web que permita o cadastro de informações essenciais de clientes, incluindo nome, sobrenome e data de nascimento.

## Configuração do Ambiente
O primeiro passo ao utilizar o Django é configurar o ambiente de desenvolvimento. Certifique-se de ter o Python instalado em sua máquina e, em seguida, instale o Django utilizando o pip:


pip install django
Após a instalação, verifique a versão do Django para garantir que a instalação foi bem-sucedida:


django-admin --version
Criação do Projeto Django
Utilizamos o seguinte comando para criar um novo projeto Django chamado "cadastroclientes":


django-admin startproject cadastroclientes
O comando acima cria a estrutura de diretórios básica para o nosso projeto.

Criação do Aplicativo "clientes"
Para gerenciar o cadastro de clientes, é aconselhável criar um aplicativo específico. Para criar o aplicativo "clientes", utilizamos o comando:


cd cadastroclientes
python manage.py startapp clientes
Em seguida, registramos o aplicativo no arquivo de configuração settings.py do projeto:

python

INSTALLED_APPS = [
     ...
    'clientes',
     ...
]
Definição do Modelo de Cliente
Um elemento fundamental do nosso projeto é o modelo de dados que representa um cliente. No arquivo models.py dentro do aplicativo "clientes", definimos o seguinte modelo:

python
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
Este modelo inclui três campos: nome, sobrenome e data_nascimento, sendo que o método __str__ é definido para apresentar o cliente de forma legível.

Migrações e Banco de Dados
Após definir o modelo de dados, geramos migrações para aplicar essas alterações ao banco de dados:


python manage.py makemigrations
python manage.py migrate
Dessa forma, a tabela correspondente ao modelo Cliente é criada no banco de dados configurado.

Administração de Clientes
O Django fornece um painel de administração que facilita a gestão de dados. Para habilitar a administração do modelo Cliente, registramos o modelo no arquivo admin.py do aplicativo "clientes":

python

from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)
A partir desse ponto, podemos acessar o painel de administração em /admin/ e gerenciar os registros de clientes.

## Conclusão
Este relatório apresentou um projeto de cadastro de clientes desenvolvido com o framework Django em Python. Através da definição do modelo de dados, configuração de migrações, criação de uma interface de administração e utilização de formulários, é possível construir uma aplicação web simples, mas funcional, para o cadastro de clientes. O Django oferece uma estrutura sólida para o desenvolvimento web, tornando o processo eficiente e altamente produtivo. Este projeto pode ser uma base sólida para futuras expansões e personalizações, dependendo das necessidades do negócio.

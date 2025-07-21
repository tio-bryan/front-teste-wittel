# O que é?

Este repositório é um front feito para o teste da Wittel. Há 3 páginas nela:

* Clientes (lista, busca, apaga edita)
* Cadastrar Cliente
* Relatórios

Ela consome os dados da API feito no repositório [back-teste-wittel](https://github.com/tio-bryan/back-teste-wittel) possa consumir.

Feito no Ubuntu 24.04.2 LTS dentro de um WSL 2 do Windows 11 Pro 24H2.

# Quais framworks/bibliotecas foram utilizadas?

[Django](https://www.djangoproject.com/)  
[Black Dashboard Django (Creative Tim)](https://www.creative-tim.com/product/black-dashboard-django)

# Como executar?/Pré-requisitos

* Antes de tudo, deixe executando a API do repositório [back-teste-wittel](https://github.com/tio-bryan/back-teste-wittel)
* Instale o [Git](https://git-scm.com/downloads) caso não tenha
* Clone este repositório: `git clone https://github.com/tio-bryan/front-teste-wittel.git`
* Entre na pasta do repositório: `cd front-teste-wittel`;
* Instale [Python](https://www.python.org/downloads/) versão maior igual a 3.12.3 caso não tenha
* Crie um ambiente virtual: `python3 -m venv {{nome_do_ambiente_virtual}}`
* Ative o ambiente virtual:
    - Linux: `source {{nome_do_ambiente_virtual}}/bin/activate`
    - Windows: `nome_do_ambiente_virtual\Scripts\Activate`
* Instale as dependências/bibliotecas: `pip install -r requirements.txt`
* Rode o projeto com o comando: `python3 manage.py runserver 8001` (8001 ou qualquer outra porta que não seja a 8000 utilizada pelo back)
* Acesse [http://127.0.0.1:8001/](http://127.0.0.1:8001/)

## Observações

* Caso queira desativar o ambiente virtual:
`deactivate`

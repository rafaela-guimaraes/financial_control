# financial_control por Rafaela Santos
Esse projeto foi construído utilizando [Python](https://www.python.org/) versão 3.6.5 e [Django](https://www.djangoproject.com/download/) versão 2.0.4

### Como executar o sistema?
Para exectar o sistema é necessário possuir [Python](https://www.python.org/) e  
[Django](https://www.djangoproject.com/download/) instalados na máquina. 

Pelo terminal, entre na pasta do projeto (financial_control) e digite os seguintes comandos

```sh
$ python manage.py migrate
$ python manage.py loaddata finances_db.json
$ python manage.py runserver
```
Para acessar o sistema:
```sh
127.0.0.1:8000/finances/
```
Cadastre um usuário para acessar o sistema.

## Sobre a solução

Trata-se de um sistema para lançamentos de receitas/despesas por período mensal. Basicamente, a solução possui uma sequência de telas para cadastro e visualização das finanças: 

**Login**
O acesso ao sistema é restrito a usuários cadastrados, dessa forma, é solicitado um login. Caso não possua um, clique em *Registrar*.

**Início**
Exibe as 5(cinco) últimas receitas e despesas lançadas no mês atual. Também possibilita *"Ver mais"*, ou seja, acessar uma página de detalhamento de todas as despesas e receitas filtradas pelo período escolhido pelo usuário.

**Adicionar receita e adicionar despesa**
No formulário de criação de lançamentos, o usuário seleciona a categoria, o valor, a data de pagamento/recebimento e descreve sua receita/despesa.

**Extrato de lançamentos**
Na tela de extrato é exibida a relação *entrada x saída* de despesas e receitas, bem como o saldo.

**Resumo de despesas por categoria**
Para maior controle financeiro, há a exibição dos gastos e o total por categoria

## Aprimoramentos
Caso houvesse maior tempo disponível para aperfeiçoamento, as próximas melhorias seriam:

* Formulário para criação, edição e remoção das categorias
* Gráfico para exibição de despesas por categoria
* Otimizar o front-end
# **Sistema Bancário - V2**

### Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

### Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades e Demonstração](#funcionalidades-e-demonstração-da-aplicação)
* [Como Usar a Aplicação](#como-usar-a-aplicação)
* [Equipe do Projeto](#equipe-do-projeto)
* [Conclusão](#conclusão)
* [Prévia do Projeto](#prévia-do-projeto)

## Descrição do Projeto

Este projeto é a segunda versão de um sistema bancário, desenvolvida em Python. O código foi refatorado para se tornar mais robusto e modular, permitindo o gerenciamento de múltiplos usuários e contas correntes. As operações de depósito, saque e extrato agora são vinculadas a uma conta específica. O projeto foi aprimorado para utilizar funções com regras de passagem de argumentos (argumentos posicionais e nomeados), o que melhora a organização e a legibilidade do código.

### Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.x

### Estrutura do Projeto

```bash
sistema-bancario/
├── main.py
└── README.md
```
* `main.py`: Contém todo o código-fonte da aplicação, incluindo as variáveis globais, o menu e a lógica das operações.
* `README.md`: Este arquivo de documentação, explicando o projeto.

### Status do Projeto

✅ Concluído - Versão 2.0

Este projeto foi finalizado em sua segunda versão, com todas as funcionalidades implementadas e testadas.

## Funcionalidades e Demonstração da Aplicação

### Principais Funcionalidades

* **Cadastro de Usuário:** Permite criar novos usuários com validação de CPF único.
* **Criação de Conta:** Permite criar contas correntes, com um número sequencial, vinculando-as a um usuário existente.
* **Depósito:** Realiza depósitos em uma conta específica, com argumentos posicionais.
* **Saque:** Opera sobre uma conta específica, com as regras de limite diário e valor, e por argumentos nomeados.
* **Extrato:** Exibe o histórico de transações e o saldo de uma conta específica, utilizando argumentos posicionais e nomeados.
* **Listar Contas:** Permite visualizar todas as contas cadastradas no sistema.

### Como funciona

A aplicação é executada via terminal, com um menu interativo que guia o usuário. Os dados de usuários e contas são armazenados em listas de dicionários, o que permite o gerenciamento de múltiplos objetos de forma eficiente. As operações agora são realizadas em funções separadas, que recebem e retornam os dados necessários para o sistema.

### Como Usar a Aplicação

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Navegue até a pasta do projeto no seu terminal.
3.  Execute o seguinte comando:
    ```bash
    python main.py
    ```
4.  Utilize as opções do menu para criar usuários (`nu`), criar contas (`nc`) e depois realizar as operações bancárias (`d`, `s`, `e`) e visualizar as contas (`lc`).

## Equipe do Projeto

<a href="https://github.com/amaro-netto" title="Amaro Netto"><img width="180" src="https://github.com/user-attachments/assets/b7a3a1bf-304a-4974-b75f-1d620ad6ecf1"/></a>

## Conclusão

A refatoração para a V2 solidificou conceitos de modularização, passagem de argumentos e estruturas de dados mais complexas em Python. O sistema agora é mais escalável e preparado para futuras expansões, como a implementação de classes para um design orientado a objetos.

## Prévia do Projeto

A prévia do projeto agora demonstra o novo menu e as funcionalidades de múltiplas contas em execução.

<img width="1572" height="1025" alt="image" src="https://github.com/user-attachments/assets/6035baaa-1457-46af-a336-fadc58b70012" />

# **Sistema Bancário - V1**

### Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)

### Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades e Demonstração](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Como Usar a Aplicação](#como-usar-a-aplicação)
* [Equipe do Projeto](#equipe-do-projeto)
* [Conclusão](#conclusão)
* [Prévia do Projeto](#prévia-do-projeto)

## Descrição do Projeto

Este projeto é a primeira versão de um sistema bancário simples, desenvolvido em Python. Ele simula as operações básicas de um caixa eletrônico, permitindo que um único usuário realize depósitos, saques e visualize seu extrato. O objetivo principal foi aplicar a lógica de programação, manipulação de variáveis e estruturas condicionais para atender aos requisitos de um desafio de programação.

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

✅ Concluído - Versão 1.0

Este projeto foi finalizado em sua primeira versão, com todas as funcionalidades básicas implementadas e testadas.

## Funcionalidades e Demonstração da Aplicação

### Principais Funcionalidades

* **Depósito:** Permite adicionar valores positivos à conta.
* **Saque:** Limita os saques a um máximo de 3 por dia, com valor máximo de R$ 500,00 por operação, e verifica se o saldo é suficiente.
* **Extrato:** Exibe o histórico de todas as transações (depósitos e saques) e o saldo atual da conta.

### Como funciona

A aplicação é executada via terminal e apresenta um menu interativo para o usuário escolher a operação desejada. As transações são armazenadas em uma lista e o saldo é atualizado a cada operação.

### Como Usar a Aplicação

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Navegue até a pasta do projeto no seu terminal.
3.  Execute o seguinte comando:
```bash
    python main.py
```
4.  Siga as instruções do menu para realizar as operações de depósito, saque e extrato.

## Equipe do Projeto

<a href="https://github.com/amaro-netto" title="Amaro Netto"><img width="180" src="https://github.com/user-attachments/assets/b7a3a1bf-304a-4974-b75f-1d620ad6ecf1"/></a>

## Conclusão

Este projeto foi uma excelente oportunidade para solidificar conceitos de lógica de programação, variáveis e controle de fluxo em Python. As próximas versões podem incluir funcionalidades como a criação de classes para `Usuário` e `Conta`, múltiplas contas, e uma interface gráfica.

## Prévia do Projeto

A prévia do projeto é baseada em sua execução via terminal, exibindo um menu simples e mensagens de interação com o usuário.

<img width="1572" height="1025" alt="image" src="https://github.com/user-attachments/assets/6035baaa-1457-46af-a336-fadc58b70012" />

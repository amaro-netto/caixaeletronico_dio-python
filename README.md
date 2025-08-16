# **Sistema Bancário - V4**

### Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![Tkinter](https://img.shields.io/badge/Tkinter-000000?style=for-the-badge&logo=python&logoColor=white)]()

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

Esta é a quarta versão de um sistema bancário, desenvolvida em Python. O projeto evoluiu significativamente, substituindo a interface de terminal por uma **Interface Gráfica (GUI)** completa, utilizando a biblioteca Tkinter. Além disso, a persistência de dados foi implementada através de um **banco de dados local SQLite**, garantindo que as informações de clientes, contas e transações sejam salvas e não se percam ao encerrar o programa.

### Tecnologias Utilizadas

* **Linguagem de Programação:** Python 3.x
* **Banco de Dados:** SQLite3
* **Interface Gráfica:** Tkinter

### Estrutura do Projeto

```bash
sistema-bancario/
├── main.py
├── gui.py
├── database.py
└── README.md
```
* `main.py`: Ponto de entrada da aplicação. Inicializa o banco de dados e a interface gráfica.
* `gui.py`: Contém a lógica de toda a Interface Gráfica (janelas, botões, campos, etc.).
* `database.py`: Encapsula toda a lógica de comunicação com o banco de dados SQLite, incluindo a criação de tabelas e as operações de escrita e leitura.
* `README.md`: Este arquivo de documentação, atualizado para a V4.

### Status do Projeto

✅ Concluído - Versão 4.0

Esta versão está finalizada e com todas as funcionalidades implementadas e testadas, com interface gráfica e persistência de dados.

## Funcionalidades e Demonstração da Aplicação

### Principais Funcionalidades

* **Interface Gráfica:** Substitui a interação por comandos de texto por uma interface visual com janelas e botões.
* **Persistência de Dados:** Todos os dados de clientes, contas e transações são salvos de forma permanente em um arquivo de banco de dados.
* **Cadastro de Usuário:** Permite criar novos clientes através de um formulário na GUI.
* **Criação de Conta:** Permite criar contas correntes, vinculando-as a um cliente existente.
* **Depósito, Saque e Extrato:** Todas as operações são realizadas por meio de formulários na interface, com a validação e atualização dos dados no banco.

### Como funciona

O programa é iniciado pelo `main.py`, que cria o banco de dados e abre a janela principal da GUI. A interação do usuário com a interface aciona funções que se comunicam com o `database.py`, que por sua vez manipula os dados no arquivo `banco.db`.

### Como Usar a Aplicação

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Navegue até a pasta do projeto no seu terminal.
3.  Execute o seguinte comando **uma única vez** para inicializar o banco de dados:
    ```bash
    python database.py
    ```
4.  Em seguida, execute a aplicação com:
    ```bash
    python main.py
    ```
5.  Utilize as opções do menu da GUI para interagir com o sistema.

## Equipe do Projeto

<a href="https://github.com/amaro-netto" title="Amaro Netto"><img width="180" src="https://github.com/user-attachments/assets/b7a3a1bf-304a-4974-b75f-1d620ad6ecf1"/></a>

## Conclusão

A implementação da V4 marcou um grande avanço no projeto, introduzindo conceitos fundamentais de desenvolvimento de aplicações, como a separação de camadas (GUI e banco de dados) e a persistência de informações. O projeto está agora preparado para futuras otimizações, como a migração para um design Orientado a Objetos na próxima versão.

## Prévia do Projeto

A prévia do projeto demonstra a interface gráfica e o fluxo de operações do sistema.
<img width="1148" height="793" alt="Captura de tela 2025-08-16 194524" src="https://github.com/user-attachments/assets/7add3a5b-8f57-4c7f-9bd0-6ee8510b4caf" />


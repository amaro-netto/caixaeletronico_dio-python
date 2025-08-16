# **Sistema Bancário - V3 (POO)**

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

Este projeto é a terceira e mais avançada versão de um sistema bancário. Ele foi completamente atualizado para seguir os princípios da **Programação Orientada a Objetos (POO)**, substituindo as estruturas de dados baseadas em dicionários por classes e objetos. A arquitetura do sistema agora é mais robusta e escalável, modelando o domínio bancário com classes como `Cliente`, `Conta`, `Historico` e `Transacao`, conforme um diagrama UML. O objetivo foi aprofundar os conceitos de classes, herança, encapsulamento e polimorfismo em Python.

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
✅ Concluído - Versão 3.0

Este projeto foi finalizado em sua terceira versão, com todas as funcionalidades implementadas e testadas.

## Funcionalidades e Demonstração da Aplicação

### Principais Funcionalidades

* **Cadastro de Clientes:** Permite criar novos clientes (objetos da classe `Cliente`) com validação de CPF único.
* **Criação de Contas:** Permite criar contas correntes (objetos da classe `ContaCorrente`), com um número sequencial, e vinculá-las a um cliente existente.
* **Depósito:** Operação realizada através do método `depositar()` do objeto da conta, garantindo a atualização do saldo e do histórico.
* **Saque:** Operação realizada através do método `sacar()` do objeto da conta, com as regras de limite diário e valor, além da validação de saldo suficiente.
* **Extrato:** Exibe o histórico de transações e o saldo de uma conta específica, acessando os atributos do objeto da conta.
* **Listar Contas:** Permite visualizar todas as contas (objetos) cadastradas no sistema.

### Como funciona

A aplicação é executada via terminal e agora interage com objetos, que encapsulam os dados e o comportamento do sistema. Os objetos de clientes e contas são armazenados em listas, e as operações bancárias são realizadas chamando os métodos correspondentes de cada objeto. Essa abordagem orientada a objetos torna o código mais intuitivo, organizado e escalável.

### Como Usar a Aplicação

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Navegue até a pasta do projeto no seu terminal.
3.  Execute o seguinte comando:
    ```bash
    python main.py
    ```
4.  Utilize as opções do menu para criar clientes (`nu`), criar contas (`nc`) e depois realizar as operações bancárias (`d`, `s`, `e`) e visualizar as contas (`lc`).

## Equipe do Projeto

<a href="https://github.com/amaro-netto" title="Amaro Netto"><img width="180" src="https://github.com/user-attachments/assets/b7a3a1bf-304a-4974-b75f-1d620ad6ecf1"/></a>

## Conclusão

A refatoração para a V3, utilizando a Programação Orientada a Objetos, solidificou conceitos de herança, encapsulamento e polimorfismo, resultando em um código mais limpo, reutilizável e fácil de manter. O sistema agora é mais escalável e representa um avanço significativo na modelagem do problema.

## Prévia do Projeto

A prévia do projeto agora demonstra o novo menu e as funcionalidades de múltiplas contas em execução.

<img width="1572" height="1025" alt="image" src="https://github.com/user-attachments/assets/6035baaa-1457-46af-a336-fadc58b70012" />

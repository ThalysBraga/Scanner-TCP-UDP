# 🔍 Scanner de Portas TCP e UDP

Este é um **scanner de portas TCP e UDP** simples, desenvolvido em Python, que verifica o estado das portas de um determinado host/IP.

## 📌 Funcionalidades

- Varredura de **portas TCP** utilizando `socket`.
- Varredura de **portas UDP** enviando pacotes vazios e aguardando resposta.
- Identifica portas **Abertas, Fechadas e Filtradas**.
- Compatível com **Windows, Linux e macOS** sem necessidade de permissões de administrador.
- **Interface gráfica moderna** usando `customtkinter`.
- **Exportação de relatório** dos resultados da varredura em `.txt`.

## 🚀 Como Funciona?

O scanner segue estas regras:

### 🔹 TCP

- **Aberta**: A conexão foi estabelecida com sucesso.
- **Fechada ou Filtrada**: O servidor recusou a conexão ou um firewall bloqueou a resposta.
- **Filtrada (sem resposta)**: Nenhuma resposta foi recebida, indicando possível bloqueio por firewall.

### 🔹 UDP

- **Aberta**: O servidor respondeu com algum dado.
- **Fechada**: O sistema respondeu com um erro "Port Unreachable".
- **Aberta ou Filtrada (sem resposta)**: Nenhuma resposta foi recebida, pode estar aberta ou bloqueada por firewall.

## 🛠️ Requisitos

- Python 3.x
- [`customtkinter`](https://github.com/TomSchimansky/CustomTkinter)

Instale com:

```bash
pip install customtkinter

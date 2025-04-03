# 🔍 Scanner de Portas TCP e UDP

Este é um **scanner de portas TCP e UDP** simples, desenvolvido em Python, que verifica o estado das portas de um determinado host/IP.

## 📌 Funcionalidades

- Varredura de **portas TCP** utilizando `socket`.
- Varredura de **portas UDP** enviando pacotes vazios e aguardando resposta.
- Identifica portas **Abertas, Fechadas e Filtradas**.
- Compatível com **Windows, Linux e macOS** sem necessidade de permissões de administrador.

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

## 📥 Instalação

Clone este repositório e entre na pasta do projeto:

```bash
 git clone https://github.com/seu-usuario/scanner-portas.git
 cd scanner-portas
```

## ▶️ Como Usar

Execute o script informando o IP e as portas a serem verificadas:

```bash
python scanner.py <IP> -p <PORTAS>
```

### 🔹 Exemplo

Para escanear as portas **22, 80 e 443** no IP **192.168.1.1**:

```bash
python scanner.py 192.168.1.1 -p 22,80,443
```

### 🔹 Saída Esperada

```plaintext
Varredura de portas TCP em 192.168.1.1:
  Porta TCP 22: Filtrada (sem resposta)
  Porta TCP 80: Aberta
  Porta TCP 443: Fechada ou Filtrada

Varredura de portas UDP em 192.168.1.1:
  Porta UDP 9: Aberta ou Filtrada (sem resposta)
  Porta UDP 80: Fechada
  Porta UDP 443: Fechada
```

## ⚠️ Aviso

- O uso indevido deste script para escanear redes sem permissão pode ser **ilegal**.
- Use apenas para **fins educacionais** ou **testes autorizados**.

## 📜 Licença

Este projeto é de código aberto e está sob a licença MIT.
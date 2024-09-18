# extrairDadosDiscord
# Projeto: Coleta de Mensagens do Discord e Exportação para CSV

Este projeto utiliza a biblioteca `discord.py` para criar um bot que coleta mensagens de servidores e canais do Discord. As informações das mensagens, como o conteúdo, data de criação, autor, função, canal, e outras, são armazenadas em um arquivo CSV para posterior análise.

## Funcionalidades

- Coleta mensagens de texto de canais e threads em servidores do Discord.
- Converte o horário das mensagens para o fuso horário de São Paulo (`America/Sao_Paulo`).
- Exporta os dados coletados para um arquivo CSV, contendo:
  - Conteúdo da mensagem.
  - Data e hora da mensagem.
  - Nome do autor e seu cargo no servidor.
  - Nome do canal, thread e servidor.
  - Categoria do canal.

## Pré-requisitos

Antes de rodar o bot, certifique-se de ter as seguintes dependências instaladas:

- **Python 3.x** ([Download](https://www.python.org/downloads/))
- **Bibliotecas Python necessárias**:
  - `discord.py`: Para integrar o bot com o Discord.
  - `pandas`: Para manipulação de dados e exportação para CSV.
  - `pytz`: Para gerenciar fuso horário.
  - `datetime`: Para trabalhar com datas e horários.

### Instalação das dependências

Você pode instalar todas as bibliotecas necessárias rodando o seguinte comando no terminal:

```bash
pip install discord.py pandas pytz
```

## Como usar

### 1. Crie o bot no Discord

1. Vá até o [Portal de Desenvolvimento do Discord](https://discord.com/developers/applications) e crie um novo aplicativo.
2. Crie um "Bot" dentro do aplicativo.
3. Copie o **token** do bot.

### 2. Modifique o script

No arquivo `bot.py`, substitua o valor de `bot.run('CHAVE_AQUI')` pela chave do seu bot Discord, por exemplo:

```python
bot.run('SEU_TOKEN_DE_BOT_AQUI')
```

### 3. Execute o script

No terminal, navegue até o diretório onde o arquivo `bot.py` está localizado e execute:

```bash
python bot.py
```

O bot irá:
1. Logar no servidor.
2. Coletar mensagens de canais e threads desde uma data específica (`2024-04-05` no código).
3. Exportar as mensagens coletadas para um arquivo CSV chamado `teste.csv`.

### Exemplo de CSV gerado

O arquivo CSV gerado (`teste.csv`) terá a seguinte estrutura:

| Message         | Message Datetime      | User    | Role      | Channel    | Thread  | Server Name | Category  |
|-----------------|-----------------------|---------|-----------|------------|---------|-------------|-----------|
| "Olá!"          | 2024-04-05 12:00:00   | João    | Admin     | geral      | None    | MeuServer   | Social    |
| "Bom dia"       | 2024-04-06 08:45:10   | Maria   | Moderator | avisos     | None    | MeuServer   | Informações |

### Personalização

- **Data de coleta de mensagens**: Você pode alterar a data a partir da qual deseja coletar as mensagens mudando o valor `datetime.fromisoformat('2024-04-05')`.
- **Formatação e filtros**: Adapte o script para coletar dados adicionais, como reações e anexos.

## Considerações Finais

Lembre-se de dar ao bot as permissões necessárias para acessar mensagens de texto em seus servidores e canais, como leitura de mensagens e histórico de mensagens.

Este projeto é útil para análise de dados de comunidades no Discord, permitindo a exportação fácil de mensagens para um arquivo CSV que pode ser manipulado posteriormente com ferramentas de análise de dados.


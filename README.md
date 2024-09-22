# Nota de Update -- Versão 0.15
- Correção de bugs no Daily e Work
- Adição da fase BETA da funcionalidade de Tickets
- Criação da roleta e da rinha de galo ( Roleta ainda não concluída )

  **Em caso de Bugs ou má funcionalidade de algum desses, contatar `yuchironozora`, no Discord.





## DOCUMENTATION

![EchoSol Banner](https://i.imgur.com/am2iFn6.jpeg)


# EchosSol

EchosSol é um bot criado por **yuchironozora**, com o intuito de ajudar a comunidade de criação de bots de Discord que usam a linguagem de programação Python. Ele engloba todos os comandos necessários para um bot multiuso e funcional, como:

## Ferramentas usadas
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Comandos

- **Econômicos**: `pay`, `work`, `balance`, `dep` e, futuramente, muito mais.
- **Administrativos**: `ban`, `kick`, `unban`, `mute`, `unmute`.
- **Controle geral**: `purge`, `send embeds`, `tickets` e outros.

Esses comandos citados são apenas uma parcela dos comandos que EchosSol englobará. Afinal, ele ainda está na versão **0.1**, e futuramente, com a vinda de novas versões, se tornará um dos bots mais completos **Open Source** do Discord.

## Como Contribuir

Contribuições são sempre bem-vindas! Aqui estão algumas maneiras de você ajudar a tornar o EchosSol ainda melhor:

1. **Relatar Bugs**: Se você encontrar um bug, por favor, abra um **issue** detalhando o problema.

2. **Solicitar Recursos**: Tem uma ideia para um novo recurso? Sinta-se à vontade para abrir uma **issue** com sua sugestão.

3. **Fazer Fork do Repositório**:
   - Faça um fork do repositório.
   - Crie uma nova branch com sua feature ou correção:  
     ```bash
     git checkout -b minha-feature
     ```
   - Faça suas alterações e commit:  
     ```bash
     git commit -m "Adicionando uma nova feature"
     ```

4. **Enviar um Pull Request**: Após fazer suas alterações, envie um pull request para que possamos revisar suas contribuições.

5. **Documentação**: Ajude a melhorar a documentação do projeto, seja corrigindo erros ou adicionando novas informações.

### Requisitos
- Conhecimento em Python e na criação de bots para Discord.
- Familiaridade com Git e GitHub.

Agradecemos a sua contribuição!

## Como Usar

Para utilizar o EchosSol, siga as instruções abaixo:

### Pré-requisitos

1. **MySQL**: Certifique-se de ter o MySQL instalado em seu sistema.
2. **Criar Banco de Dados**:
   - Crie um banco de dados e uma tabela chamada `users` com os seguintes campos:
     - `member_id`
     - `id_discord`
     - `current_balance`
     - `date_daily`
     - `work_date`

### Instalação de Dependências

Certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install discord.py mysql-connector-python python-dotenv
```

### Configuração do Bot
1. **Token do Bot**: Crie um bot no Portal do Discord Developer e obtenha o token.

2. **Criar um arquivo .env:** Na raiz do seu projeto, crie um arquivo chamado .env e adicione as seguintes informações:

```makefile
DISCORD_TOKEN=seu_token_aqui
MYSQL_HOST=seuhost
MYSQL_USER=seuuser
MYSQL_PASSWORD=seupassword
MYSQL_DATABASE=nome_do_banco
```
Substitua as informações pelas **suas** informações de conexão e o token do bot.

### Exemplo de Conexão
Aqui está um exemplo de como carregar as variáveis do ``.env`` e configurar a conexão com o MySQL:

```python
import os
from dotenv import load_dotenv
import mysql.connector

# Carregar variáveis do .env
load_dotenv()

# Configurar conexão com MySQL
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

# Verificar a conexão
if db.is_connected():
    print("Conexão com o MySQL estabelecida com sucesso!")
```
Agora você está pronto para rodar o bot EchosSol! Se precisar de mais assistência, consulte a documentação ou entre em contato com a comunidade.


### Links Importantes.
[MYSQL Oficial Installer](https://dev.mysql.com/downloads/installer/) 
[MYSQL Documentation](https://www.bing.com/search?q=mysql+documentation&qs=n&form=QBRE&sp=-1&lq=0&pq=mys+documentation&sc=9-17&sk=&cvid=9ED486C814234473951ACB7D84712EB3&ghsh=0&ghacc=0&ghpl=)
[Discord Developer Portal](https://www.bing.com/search?pglt=2083&q=discord+developer+portal&cvid=a2fca08d781a4d16bb4095169612a574&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDI1MDhqMGoxqAIAsAIA&FORM=ANNTA1&PC=U531)
[Tutorial MYSQL In Portuguese Brasil For Beginners](https://www.youtube.com/watch?v=XQkf-6Yl3WM)

Este projeto está licenciado por ``MIT LICENSE`` 

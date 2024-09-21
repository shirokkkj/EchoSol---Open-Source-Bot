import discord
from discord.ext import commands
import os



# Carrega as variáveis de configuração
from configs.informations import TOKEN

# Inicializa o bot com intents e com o objecto de comandos
intents = discord.Intents.all()
intents.message_content = True  # Habilita o acesso ao conteúdo das mensagens

bot = commands.Bot(command_prefix="!", intents=intents)

# Sincroniza slash commands em todos os servidores do bot
async def sync_commands():
    for guild in bot.guilds:
        await bot.tree.sync(guild=guild)
    print("Slash commands sincronizados.")

# Evento que ocorre quando o bot está pronto
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sincroniza os slash commands
    print(f"Bot conectado como {bot.user}")

# Carrega os módulos (cogs) dinamicamente
loaded_cogs = []

async def load_cogs():
    for root, dirs, files in os.walk("./cogs"):
        for filename in files:
            if filename.endswith(".py"):
                cog_name = f"{os.path.relpath(os.path.join(root, filename), './').replace(os.path.sep, '.').rstrip('.py')}"
                if cog_name not in loaded_cogs:
                    await bot.load_extension(cog_name)
                    loaded_cogs.append(cog_name)
                    print(f"Cog {filename} carregada.")
                else:
                    print(f"Cog {filename} já carregada, ignorando.")


# Inicializa e roda o bot
async def main():
    await load_cogs()  # Carrega os cogs
    await bot.start(TOKEN)  # Inicia o bot


import asyncio
asyncio.run(main())

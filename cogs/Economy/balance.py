import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()


host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_NAME')

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

class BalanceUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="current_balance", description="Checa o dinheiro atual na sua conta.")
    async def check_current_balance(self, interaction: discord.Interaction):  # Renomeado
            
        cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
        result = cursor.fetchone()
        
        if result:
            current_balance = result[0]
        else:
            embed_model = EmbedsModel(title='Você precisa se registrar!', description='Antes de usufruir da economia, faça o seu registro!', color=0xff0000)
            embed = embed_model.CreateEmbed()
            
            await interaction.response.send_message(embed=embed)
            return
        
        connection.commit()  
        
        embed_model = EmbedsModel(title='💸 Dinheiro atual', description=f'Atualmente você tem {current_balance} EchosSolares', color=0x00ff00)
        embed = embed_model.CreateEmbed()
        
        await interaction.response.send_message(embed=embed)
               
async def setup(bot):
    await bot.add_cog(BalanceUser(bot))

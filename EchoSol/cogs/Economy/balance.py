import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import mysql.connector

connection = mysql.connector.connect(
    host='.',
    user='.',
    password='.',
    database='.'
)

cursor = connection.cursor()

class BalanceUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="current_balance", description="Checa o dinheiro atual na sua conta.")
    async def check_current_balance(self, interaction: discord.Interaction):  # Renomeado
        try:
            
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
            
            result = cursor.fetchone()
            
            if result:
                current_balance = result[0]
            else:
                print('fail')
            connection.commit()  # Confirma a transação
            embed_model = EmbedsModel(title='💸 Dinheiro atual', description=f'Atualmente você tem {current_balance} EchosSolares', color=0x00ff00)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            
            
        except Exception as e:  # Tratamento de erro específico
            print(f"Erro ao registrar no banco de dados: {e}")
        
async def setup(bot):
    await bot.add_cog(BalanceUser(bot))

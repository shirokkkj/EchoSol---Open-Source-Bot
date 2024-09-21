import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import mysql.connector

connection = mysql.connector.connect(
    host='.',
    user='root',
    password='.',
    database='.'
)

cursor = connection.cursor()

class RegistrationUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register_economy", description="Registre-se na economia do servidor.")
    async def register_economy(self, interaction: discord.Interaction):  # Renomeado
        try:
            cursor.execute(f'INSERT INTO members (id_discord, current_balance) VALUES(%s, %s)', (interaction.user.id, 0))
            connection.commit()  # Confirma a transação
            embed_model = EmbedsModel(title=':white_check_mark: Registro feito', description='Agora você já faz parte da nossa economia.', color=0x00ff00)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
        except Exception as e:  # Tratamento de erro específico
            print(f"Erro ao registrar no banco de dados: {e}")
            await interaction.response.send_message("Houve um erro ao tentar se registrar na economia.")
        
async def setup(bot):
    await bot.add_cog(RegistrationUser(bot))

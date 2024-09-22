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

class RegistrationUser(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register_economy", description="Registre-se na economia do servidor.")
    async def register_economy(self, interaction: discord.Interaction):  # Renomeado
        cursor.execute(f'INSERT INTO members (id_discord, current_balance, date_daily, work_date) VALUES(%s, %s, %s, %s)', (interaction.user.id, 0, '0', '0'))
        connection.commit()
        
        embed_model = EmbedsModel(title=':white_check_mark: Registro feito', description='Agora você já faz parte da nossa economia.', color=0x00ff00)
        embed = embed_model.CreateEmbed()
        
        await interaction.response.send_message(embed=embed)
    
async def setup(bot):
    await bot.add_cog(RegistrationUser(bot))

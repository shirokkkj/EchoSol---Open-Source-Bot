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

class CloseTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="close_ticket", description="Fecha o ticket")
    
    
    async def create_ticket(self, interaction: discord.Interaction):  
            
            if interaction.channel.name[0:6] != 'ticket':
                embed_model = EmbedsModel(title='Este chat não é um ticket.', description='Para usar este comando, é necessário estar em um ticket..', color=0xff0000)
                embed = embed_model.CreateEmbed()
                await interaction.response.send_message(embed=embed)
                return
            
            await interaction.channel.send("🔒 Este ticket está sendo fechado e bloqueado. Obrigado por usar o suporte!")
            
            await interaction.channel.set_permissions(interaction.user, view_channel=False)
            
        
async def setup(bot):
    await bot.add_cog(CloseTicket(bot))

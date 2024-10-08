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

class Pay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="pay", description="Envie dinheiro para alguém.")
    async def check_current_balance(self, interaction: discord.Interaction, user: discord.User, quantity: float = 0.0):  # Renomeado
            
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
            payer = cursor.fetchone()
            
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(user.id)})')
            receiver = cursor.fetchone()
            
            if payer and receiver:
                if quantity < payer[0]:
                    cursor.execute(f'UPDATE members SET current_balance = {receiver[0] + quantity} WHERE (id_discord = {str(user.id)})')
                    connection.commit()
                    
                    cursor.execute(f'UPDATE members SET current_balance = {payer[0] - quantity} WHERE (id_discord = {str(interaction.user.id)})')
                    connection.commit()
                    
                else:
                    embed_model = EmbedsModel(title='Transação não realizada', description=f'Você não tem tanto dinheiro assim...', color=0xff0000)
                    embed = embed_model.CreateEmbed()
                    
                    await interaction.response.send_message(embed=embed)
                    return
            else:
                embed_model = EmbedsModel(title='Transação não realizada', description=f'Você ou quem deseja realizar a transferência não possui registro em nossa economia.', color=0xff0000)
                embed = embed_model.CreateEmbed()
                
                await interaction.response.send_message(embed=embed)
            connection.commit()
            embed_model = EmbedsModel(title='💸 Transação feita', description=f'Você fez uma transação de {quantity} EchosSolaris para {user.mention} e agora tem {payer[0] - quantity}', color=0x00ff00)
            
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            
async def setup(bot):
    await bot.add_cog(Pay(bot))

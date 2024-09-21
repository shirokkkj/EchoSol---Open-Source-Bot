import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import datetime
import mysql.connector
from random import choice


connection = mysql.connector.connect(
    host='.',
    user='.',
    password='.',
    database='.'
)

cursor = connection.cursor()


    
possible_values = [10, 12, 15, 23, 25, 15, 11, 1, 0, 50]

class Daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="daily", description="Receba algumas moedinhas...")
    async def daily(self, interaction: discord.Interaction):  # Renomeado
        
        def get_current_date():
            cursor.execute(f'SELECT date_daily FROM members WHERE (id_discord = {str(interaction.user.id)})')
            result = cursor.fetchone()[0]
            return result
        
        def update_balance():
            cursor.execute(f'UPDATE members SET current_balance = {result[0] + choosed_value} WHERE (id_discord = {str(interaction.user.id)})')
            connection.commit()
            
        def update_date_daily():
            cursor.execute(f'UPDATE members SET date_daily = "{datetime.datetime.now().hour}" WHERE (id_discord = {str(interaction.user.id)})')
            connection.commit()
        
        def get_current_balance():
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
                
            current_balance = cursor.fetchone()[0]
            
            return current_balance
        try:
            
            choosed_value = choice(possible_values)
            
            if not get_current_date() == None:
                if datetime.datetime.now().hour - int(get_current_date()) < 24:
                    embed_model = EmbedsModel(title='Apressadinho você, não é...?', description='Você ainda não pode resgatar o seu daily, somente amanhã.', color=0xff0000)
                    embed = embed_model.CreateEmbed()
                    await interaction.response.send_message(embed=embed)
                    return
                
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
            
            result = cursor.fetchone()
            
            if result:
                update_balance()
                
                update_date_daily()
            
                current_balance = get_current_balance()
            else:
                embed_model = EmbedsModel(title='Você precisa se registrar!', description='Antes de usufruir da economia, faça o seu registro!', color=0xff0000)
                embed = embed_model.CreateEmbed()
                await interaction.response.send_message(embed=embed)
                return

            embed_model = EmbedsModel(title='💸 Daily', description=f'Parabéns! Você recebeu exatos: {choosed_value} EchosSolaris. Atualmente você tem {current_balance} EchosSolares', color=0x00ff00)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            
            
        except Exception as e:  # Tratamento de erro específico
            print(f"Error in: {e}")
        
async def setup(bot):
    await bot.add_cog(Daily(bot))

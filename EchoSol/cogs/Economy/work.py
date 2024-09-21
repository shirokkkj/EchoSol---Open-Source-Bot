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

class Work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="work", description="Trabalhe para receber moedas.")
    async def work(self, interaction: discord.Interaction):  # Renomeado
        
        def get_current_date():
            cursor.execute(f'SELECT work_date FROM members WHERE (id_discord = {str(interaction.user.id)})')
            result = cursor.fetchone()[0]
            return result
        
        def update_balance():
            cursor.execute(f'UPDATE members SET current_balance = {result[0] + choosed_value} WHERE (id_discord = {str(interaction.user.id)})')
            connection.commit()
            
        def update_date_work():
            cursor.execute(f'UPDATE members SET work_date = "{datetime.datetime.now().hour}" WHERE (id_discord = {str(interaction.user.id)})')
            connection.commit()
        
        def get_current_balance():
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
                
            current_balance = cursor.fetchone()[0]
            
            return current_balance
        try:
            
            choosed_value = choice(possible_values)
            work_messages = [
            f"Você trabalhou como jardineiro e ganhou {choosed_value} moedas!",
            f"Como entregador de pizzas, você recebeu {choosed_value} moedas por seu trabalho!",
            f"Você se tornou um assistente administrativo e ganhou {choosed_value} moedas!",
            f"Trabalhou como desenvolvedor freelance e adicionou {choosed_value} moedas à sua conta.",
            f"Você fez um bico como fotógrafo e ganhou {choosed_value} moedas!",
            f"Como vendedor de limonada, você arrecadou {choosed_value} moedas!",
            f"Você foi um mentor de programação e recebeu {choosed_value} moedas!",
            f"Trabalhou como artista e ganhou {choosed_value} moedas por suas criações!",
        ]
            choosed_message = choice(work_messages)
            
            if not get_current_date() == '3':
                if datetime.datetime.now().hour - int(get_current_date()) < 1:
                    embed_model = EmbedsModel(title='Apressadinho você, não é...?', description='Seu turno acabou, somente amanhã.', color=0xff0000)
                    embed = embed_model.CreateEmbed()
                    await interaction.response.send_message(embed=embed)
                    return
                
            cursor.execute(f'SELECT current_balance FROM members WHERE (id_discord = {str(interaction.user.id)})')
            
            result = cursor.fetchone()
            
            if result:
                update_balance()
                
                update_date_work()
            
                current_balance = get_current_balance()
            else:
                embed_model = EmbedsModel(title='Você precisa se registrar!', description='Antes de usufruir da economia, faça o seu registro!', color=0xff0000)
                embed = embed_model.CreateEmbed()
                await interaction.response.send_message(embed=embed)
                return

            embed_model = EmbedsModel(title='💸 Work', description=f'{choosed_message}', color=0x00ff00)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            
            
        except Exception as e:  # Tratamento de erro específico
            print(f"Error in: {e}")
        
async def setup(bot):
    await bot.add_cog(Work(bot))

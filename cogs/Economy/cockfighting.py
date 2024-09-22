import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import mysql.connector
from dotenv import load_dotenv
import os
from asyncio import sleep
from random import choice

load_dotenv()

# Configuração do banco de dados
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

class CockFight(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="cockfight", description="UMA RINHA DE GALO!?")
    async def cockfight(self, interaction: discord.Interaction, opponent: discord.Member, bet_value: int = 0):
        async def cockfight_callback(interaction: discord.Interaction):
            try:
                
                if interaction.user.id != opponent.id:
                    await interaction.response.send_message(f'Ei, você não é {opponent.mention} para fazer isso.')
                    return
                
                roosters = [
                    'Galo Um',
                    'Galo Dois'
                ]
                
                if user_balance < bet_value:
                    await interaction.response.send_message('Você não tem dinheiro para isso.')
                    return
                
                if opponent_balance < bet_value:
                    await interaction.response.send_message('O seu parceiro não tem dinheiro para isso.')
                    return
                
                chosen_winner = choice(roosters)
                accept_bet_view.remove_item(button_accept_bet)
                
                if chosen_winner == 'Galo Um':
                    print('Vencedor: ', user_balance)
                    cursor.execute(f'UPDATE members SET current_balance = {user_balance + bet_value} WHERE (id_discord = {str(rooster_owner.get("rooster1"))})')
                    connection.commit()
                    
                    cursor.execute(f'UPDATE members SET current_balance = {opponent_balance - bet_value / 2} WHERE (id_discord = {str(opponent.id)})')
                    connection.commit()
                    await interaction.response.send_message(f'{roosters_info.get("rooster1")} foi o vencedor e ganhou {bet_value}. {opponent.mention} perdeu {bet_value / 2}')
                else:
                    print('Vencedor: ', opponent_balance)
                    cursor.execute(f'UPDATE members SET current_balance = {opponent_balance + bet_value} WHERE (id_discord = {str(opponent.id)})')
                    connection.commit()
                    
                    cursor.execute(f'UPDATE members SET current_balance = {user_balance - bet_value / 2} WHERE (id_discord = {str(rooster_owner.get("rooster1"))})')
                    connection.commit()
                    
                    await interaction.response.send_message(f'{opponent.mention} foi o vencedor e ganhou {bet_value}. {roosters_info.get("rooster1")} perdeu {bet_value / 2}')
            except Exception as e:
                print(e)
                
        roosters_info = {
            'rooster1': interaction.user.mention,
            'rooster2': opponent.mention,     
        }
        
        rooster_owner = {
            'rooster1': interaction.user.id
        }
            
        cursor.execute('SELECT current_balance FROM members WHERE id_discord = %s', (str(interaction.user.id),))
        fetch_user_balance = cursor.fetchone()
        user_balance = fetch_user_balance[0]
        
        cursor.execute('SELECT current_balance FROM members WHERE id_discord = %s', (str(opponent.id),))
        fetch_opponent_balance = cursor.fetchone()
        opponent_balance = fetch_opponent_balance[0]
        
        if user_balance and opponent_balance:
            await interaction.channel.send(f"**🐔💥 | {interaction.user.mention}, você está prestes a entrar em uma RINHA DE GALO épica contra {opponent.mention}! 💣⚔️\n\n💰 Aposte {bet_value} EchosSolaris e prove que seu galo é o mais forte! 💪🐓\n\n🔥 {opponent.mention}, está pronto para aceitar o desafio? 🔥**"
        )
            accept_bet_view = discord.ui.View()
            button_accept_bet = discord.ui.Button(label='Você quer entrar na rinha de galo?', style=discord.ButtonStyle.danger)
            
            accept_bet_view.add_item
            accept_bet_view.add_item(button_accept_bet)
            button_accept_bet.callback = cockfight_callback
        
            await interaction.channel.send(view=accept_bet_view)

async def setup(bot):
    await bot.add_cog(CockFight(bot))

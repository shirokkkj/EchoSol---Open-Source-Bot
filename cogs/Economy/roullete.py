import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel
import mysql.connector
from dotenv import load_dotenv
import os
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

class Roullete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roullete", description="Que tal uma aposta?")
    async def roullete(self, interaction: discord.Interaction, number: int = 0):
        possible_values = [10, 30, 55, 20, 11, 21, 12, 50, 100, 20, 10, 20, 30, 35, 42]
        choosed_value = choice(possible_values)
        
        randomized_number = choice(range(26))

        user_balance = self.get_member_balance(interaction.user.id)

        if user_balance is None:
            await self.send_message(interaction, 'Você precisa se registrar!', 'Antes de usufruir da economia, faça o seu registro!', 0xff0000)
            return

        pre_game_balance = user_balance[0]

        if pre_game_balance <= 1:
            await self.send_message(interaction, 'Roleta impossibilitada', 'Você não tem tanto dinheiro assim...', 0xff0000)
            return

        if number == randomized_number:
            new_balance = pre_game_balance + choosed_value
            self.update_member_balance(interaction.user.id, new_balance)
            current_balance = self.get_member_balance(interaction.user.id)[0]
            await self.send_message(interaction, '💸 Ganhos!', f'Parabéns! Você ganhou {choosed_value} e agora tem {current_balance} EchosSolaris', 0x00ff00)
        else:
            await self.send_message(interaction, 'Que azar...', f'Você não ganhou nada... Mas pelo menos não perdeu. O número era: {randomized_number}!', 0xff0000)

    def get_member_balance(self, user_id):
        cursor.execute('SELECT current_balance FROM members WHERE id_discord = %s', (str(user_id),))
        return cursor.fetchone()

    def update_member_balance(self, user_id, new_balance):
        cursor.execute('UPDATE members SET current_balance = %s WHERE id_discord = %s', (new_balance, str(user_id)))
        connection.commit()

    async def send_message(self, interaction, title, description, color):
        embed_model = EmbedsModel(title=title, description=description, color=color)
        embed = embed_model.CreateEmbed()
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Roullete(bot))

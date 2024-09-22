import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel

class Whisper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sussuro", description="Mande uma mensagem secreta para alguém.")
    async def whisper(self, interaction: discord.Interaction, member_id: str = '', message: str = ''):
         
        invited_message = interaction.client.get_user(int(member_id))
        
        if invited_message:
            await invited_message.send(f'{message}. By: <@{interaction.user.id}')
            await interaction.response.send_message(f'Uma mensagem secreta acaba de ser enviada para {invited_message.mention}', ephemeral=True)
            
        else:
            await interaction.response.send_message(f'Não foi possível encontrar um membro com o ID {member_id}')
        
async def setup(bot):
    await bot.add_cog(Whisper(bot))

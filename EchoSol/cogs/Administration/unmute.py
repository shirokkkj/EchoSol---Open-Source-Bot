import discord
from discord import app_commands
from discord.ext import commands
import datetime
from utils.embeds import EmbedsModel

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="unmute", description="Desmuta um usuário")
    async def mute(interaction: discord.Interaction, member: discord.Member, reason: str):
        
        if not interaction.user.guild_permissions.mute_members:
            await interaction.response.send_message('Você não tem permissão para fazer isso!')
        
        if not member.is_timed_out():
            await interaction.response.send_message(f'O usuário: {member.mention} não está mutado atualmente.')
            
        if interaction.user.id == member.id:
            embed_model = EmbedsModel(title='Passáros malditos, espera...',
            description=f'Uffh, os passáros estão enchendo o nosso saco com tantas bicadas na fiação... Pelo menos impediram você de fazer o que ia fazer, né?!',
            color=0xff0000)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            return
        
        await member.edit(timeout=None)
        
        embed_model = EmbedsModel(
            title='🔨 Retirada de castigo!',
            description=f'O usuário **{member}** acaba de ser desmutado por: **{interaction.user.mention}** com o motivo: ___{reason}___',
            color=0xff0000
        )
        
        embed = embed_model.CreateEmbed()
        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Unmute(bot))

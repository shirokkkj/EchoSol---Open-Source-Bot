import discord
from discord import app_commands
from discord.ext import commands
import datetime
from utils.embeds import EmbedsModel

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mute", description="Muta um usuário")
    async def mute(interaction: discord.Interaction, member: discord.Member, reason: str = '', seconds: int = 0, minutes: int = 0, hours: int = 0, weeks: int = 0):
        duration = datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours, weeks=weeks)
        
        if not interaction.user.guild_permissions.mute_members:
            await interaction.response.send_message('Você não tem permissão para fazer isso!')
        
        if interaction.user.id == member.id:
            embed_model = EmbedsModel(title='Passáros malditos, espera...',
            description=f'Uffh, os passáros estão enchendo o nosso saco com tantas bicadas na fiação... Pelo menos impediram você de fazer o que ia fazer, né?!',
            color=0xff0000)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            return
        
        await member.timeout(duration)
        
        embed_model = EmbedsModel(
            title='🔨 Novo Castigo!',
            description=f'O usuário **{member}** acaba de ser mutado por: **{interaction.user.mention}** com o motivo: ___{reason}___',
            color=0xff0000
        )
        
        embed = embed_model.CreateEmbed()
        
        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Mute(bot))

import discord
from discord import app_commands
from discord.ext import commands
from utils.embeds import EmbedsModel

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Expulsa um usuário do servidor")
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = ''):
         
        if not interaction.user.guild_permissions.kick_members:
            await interaction.response.send_message('**Você não tem permissão para fazer isto!**')
            
        if interaction.user.id == member.id:
            embed_model = EmbedsModel(title='Passáros malditos, espera...',
            description=f'Uffh, os passáros estão enchendo o nosso saco com tantas bicadas na fiação... Pelo menos impediram você de fazer o que ia fazer, né?!',
            color=0xff0000)
            embed = embed_model.CreateEmbed()
            await interaction.response.send_message(embed=embed)
            return
        
        await interaction.guild.kick(member)
        
        embed_model = EmbedsModel(
            title='🔨 Nova Expulsão!',
            description=f'O usuário **{member}** acaba de ser expulso por: **{interaction.user.mention}** com o motivo: ___{reason}___',
            color=0xff0000
        )
        
        embed = embed_model.CreateEmbed()
        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Kick(bot))

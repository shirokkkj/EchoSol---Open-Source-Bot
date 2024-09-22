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

class CreateTicket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="generate_ticket", description="Seta o embed de criação de tickets.")
    
    
    async def create_ticket(self, interaction: discord.Interaction):  
                
            if not interaction.user.guild_permissions.manage_channels:
                embed_model = EmbedsModel(title='Lhe falta permissão.', description='Você não tem permissão para fazer isto.', color=0xff0000)
                embed = embed_model.CreateEmbed()
                await interaction.response.send_message(embed=embed)
                return
            
            async def callback_create_chat(interaction: discord.Interaction):
                try:
                    discord_category = discord.utils.get(interaction.guild.categories, name='CURIO')
                    
                    ticket_channel = await interaction.guild.create_text_channel(category=discord_category, name=f'ticket-{interaction.user.name}')
                    
                    
                    await ticket_channel.set_permissions(interaction.guild.default_role, view_channel=False)
        
                    await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
                    
                    await ticket_channel.send(f"""
🎫 **Bem-vindo(a) ao seu ticket, {interaction.user.mention}!**

Nossa equipe estará com você em breve. Enquanto isso, por favor, descreva seu problema ou questão com o máximo de detalhes possível para que possamos ajudar da melhor forma.

🔒 **Importante**:
- Apenas você e a equipe de suporte têm acesso a este canal.
- Quando o suporte acabar, VOCÊ deve usar o comando **/close**

Agradecemos pela paciência e colaboração! 😊
                        """)
                    
                    await interaction.response.send_message(f'Ticket ticket-{interaction.user.name} has been created > {ticket_channel.mention}')
                except Exception as e:
                    print(e)
                    

                
            view_ticket = discord.ui.View()
            
            button = discord.ui.Button(label='Criar ticket', style=discord.ButtonStyle.green)
            
            view_ticket.add_item(button)
            
            button.callback = callback_create_chat
            
            await interaction.response.send_message(view=view_ticket)
        
async def setup(bot):
    await bot.add_cog(CreateTicket(bot))

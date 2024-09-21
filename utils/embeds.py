from discord import Embed

class EmbedsModel():
    def __init__(self, title, description, color):
        self.title = title
        self.description = description
        self.color = color
    
    def CreateEmbed(self):
        embed = Embed(
            title=self.title,
            description=self.description,
            color=self.color
        )
        
        return embed
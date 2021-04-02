import discord
from discord.ext import commands

intents = discord.Intents.none()
intents.guilds = True
intents.members = True
intents.emojis = True
intents.guild_messages = True
intents.guild_reactions = True

class TestBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="^", help_command=None, max_messages=None, intents=intents)
        self.load_extension('test_cog')

if __name__ == "__main__":
    bot = TestBot()
    bot.run("[TOKEN HERE]", bot=True)
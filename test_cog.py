import discord
from discord.ext import commands
import asyncio

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.channel.type.name != 'text':
            return

        def check(reaction, user):
            print('a')
            return user == message.author and str(reaction.emoji) == "👍"

        try:        
            reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=10)
            print('success!')

        except asyncio.exceptions.TimeoutError:
            print('timed out :(')

        except Exception as e:
            print(f'other error: {repr(e)}')

def setup(bot):
    bot.add_cog(TestCog(bot))
    print("Test Cog loaded")
import discord
from discord.ext import commands
import json


class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Test Command are online!')

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Commands working!")


def setup(client):
    client.add_cog(Test(client))

import discord
from discord.ext import commands
import json
import os
from main import client
from main import developers


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Clear Command are online!')

    @commands.command(aliases=['purge', 'delete'])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.bot_has_permissions(send_messages=True)
    async def clear(self, ctx, *, amount: int):
        if amount <= 1000:
            await ctx.channel.purge(limit=amount + 1)
            print(f'clear command by {ctx.message.author} in {ctx.channel.name}, in the {ctx.guild.name} server'
                  f'\n       Cleared {str(amount)} messages')

            # Clears the desired amount of messages
            # Has a cap of 1000

        if amount > 1000:
            Embed_A = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**I have a cap of 1000 messages**\n\n"
            )
            await ctx.send(embed=Embed_A)

        # Makes a cap of 200
        # Prevents accidental DDOS

    # Errors for clear command

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            Embed_B_1 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**You need the `manage messages` permission to execute this command.**"
            )
            await ctx.send(embed=Embed_B_1)
            print('Clear error...\n      Author missing permissions')
        if isinstance(error, commands.MissingRequiredArgument):
            Embed_B_2 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**You need to specify a `number` of message for me to clear.**\n\n"
                            "**Example** `50`"
            )
            await ctx.send(embed=Embed_B_2)
            print('Clear error...\n      Missing required argument')
        if isinstance(error, commands.BotMissingPermissions):
            Embed_B_3 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**I need the `manage messages` permission to execute this command.**"
            )
            await ctx.send(embed=Embed_B_3)
            print('Clear error...\n     Bot missing permissions')
        if isinstance(error, commands.BadArgument):
            Embed_B_4 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**You need to specify a `number` of message for me to clear.**\n\n"
                            "**Example** `50`"
            )
            await ctx.send(embed=Embed_B_4)
            print('Clear error...\n      Bad argument')


def setup(client):
    client.add_cog(Clear(client))

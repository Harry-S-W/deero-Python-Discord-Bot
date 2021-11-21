import discord
from discord.ext import commands
import json
import os
from main import client
from main import developers


class Kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kick Command are online!')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.bot_has_permissions(send_messages=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if member.guild_permissions.administrator:
            Embed_A = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title='Error',
                description=f"**{member.mention} is an `administrator`.**\n\n"
                            "**Their role could also `rank higher` than mine.**"
            )
            await ctx.send(embed=Embed_A)

        else:
            await member.kick(reason=reason)
            Embed_B = discord.Embed(
                colour=discord.Colour.from_rgb(26, 255, 0),
                title="Success",
                description=f"**{member.mention} Has been kicked**\n\n"
                            f"**Author: {ctx.author.mention}**\n\n"
                            f"**Reason:** {reason}"
            )
            await ctx.send(embed=Embed_B)
            # Sends a message to the server ^^^
            print(f'Kick command by {ctx.message.author} in {ctx.channel.name}, in the {ctx.guild.name} server')

    # Kick errors

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            Embed_C_1 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**Please mention a user that is in this `server`.**\n\n"
                            "**If they do not have access to this channel, I can not kick them.**"
            )
            await ctx.send(embed=Embed_C_1)
            print('Kick error...\n      Missing required argument')
        if isinstance(error, commands.MissingPermissions):
            Embed_B_2 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**You need the `kick members` permission to execute this command.**"
            )
            await ctx.send(embed=Embed_B_2)
            print('Kick error...\n      Author missing permissions')
        if isinstance(error, commands.BotMissingPermissions):
            Embed_B_3 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**I need the `kick members` permission to execute this command.**"
            )
            await ctx.send(embed=Embed_B_3)
            print('Kick error...\n      Bot missing permissions')
        if isinstance(error, commands.BadArgument):
            Embed_C_4 = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error",
                description="**Please mention a user that is in this `server`.**\n\n"
                            "**If they do not have access to this channel, I can not kick them.**"
            )
            await ctx.send(embed=Embed_C_4)
            print('Kick error...\n      Bad argument')


def setup(client):
    client.add_cog(Kick(client))

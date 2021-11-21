import discord
from discord.ext import commands
import json
import os
from main import client
from main import developers
from cryptography.fernet import Fernet


class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Prefix Command are online!')

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def prefix(self, ctx, *, choice):
        with open('data/bot-data/prefixes.json', 'r')as f:
            prefixes = json.load(f)

        if ctx.channel.type is discord.ChannelType.private:
            embed_D = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title='Error',
                description="This command can't be used in private messages."
            )
            await ctx.send(embed=embed_D)

        else:

            if choice.lower() == 'add':
                def check(message):
                    return message.author == ctx.author

                embed_A = discord.Embed(
                    colour=discord.Colour.from_rgb(229, 255, 0),
                    title="Hi there!",
                    description="Please type a prefix you would like to add!"
                )
                embed_A.set_footer(text='Warning: It is cap sensitive!')
                await ctx.send(embed=embed_A)
                message = await client.wait_for('message', check=check)
                if str(ctx.guild.id) in prefixes:
                    if len(list(prefixes[str(ctx.guild.id)])) >= 3:
                        embed_B = discord.Embed(
                            colour=discord.Colour.from_rgb(255, 0, 0),
                            title='Error!',
                            description='You already have 3 prefixes saved. (Not including @ mention) 4+ prefixes are only'
                                        ' available to premium users of Deero.'
                        )
                        embed_B.add_field(name='Prefixes:', value=f'`' + ', '.join(prefixes[str(ctx.guild.id)]) + '`')
                        embed_B.set_footer(text='Remove a prefix to add new ones.')
                        await ctx.send(embed=embed_B)

                    if len(prefixes[str(ctx.guild.id)]) < 3:
                        prefixes[str(ctx.guild.id)].append(message.content)

                        with open('data/bot-data/prefixes.json', 'w')as f:
                            json.dump(prefixes, f, indent=4)

                        embed_C = discord.Embed(
                            colour=discord.Colour.from_rgb(26, 255, 0),
                            title='Great!',
                            description=f'`{message.content}` is now a registered prefix for this server!'
                        )
                        embed_C.add_field(name='Registered Prefixes:',
                                          value=f'`' + ', '.join(prefixes[str(ctx.guild.id)]) + '`')
                        await ctx.send(embed=embed_C)

                if str(ctx.guild.id) not in prefixes:
                    prefixes[str(ctx.guild.id)] = [message.content]

                    with open('data/bot-data/prefixes.json', 'w')as f:
                        json.dump(prefixes, f, indent=4)

                    embed_C = discord.Embed(
                        colour=discord.Colour.from_rgb(26, 255, 0),
                        title='Great!',
                        description=f'`{message.content}` is now a registered prefix for this server!'
                    )
                    embed_C.add_field(name='Registered Prefixes:',
                                      value=f'`' + ', '.join(prefixes[str(ctx.guild.id)]) + '`')
                    await ctx.send(embed=embed_C)

            if choice.lower() == 'remove':
                def check(message):
                    return message.author == ctx.author

                embed_E = discord.Embed(
                    colour=discord.Colour.from_rgb(229, 255, 0),
                    title="Hello!",
                    description="Please type the prefix you wish to remove!"
                )
                embed_E.set_footer(text='Warning: It is cap sensitive!')
                await ctx.send(embed=embed_E)
                message = await client.wait_for('message', check=check)

                if str(ctx.guild.id) not in prefixes:
                    embed_H = discord.Embed(
                        colour=discord.Colour.from_rgb(255, 0, 0),
                        title='Error!',
                        description='It seems like your server/guild does not have any registered prefixes.\n\n'
                                    '**FYI: You can not remove default prefixes `D. and d.`**'
                    )
                    embed_H.set_footer(text='If this information is wrong, please report this error with the error command!')
                    await ctx.send(embed=embed_H)

                if str(ctx.guild.id) in prefixes:
                    if message.content in prefixes[str(ctx.guild.id)]:
                        prefixes[str(ctx.guild.id)].remove(message.content)

                        with open('data/bot-data/prefixes.json', 'w')as f:
                            json.dump(prefixes, f, indent=4)

                        embed_F = discord.Embed(
                            colour=discord.Colour.from_rgb(26, 255, 0),
                            title="Great!",
                            description=f'I have successfully removed {message.content} from your registered prefixes!'
                        )

                        if not prefixes[str(ctx.guild.id)]:
                            if [''] not in prefixes[str(ctx.guild.id)]:
                                del prefixes[str(ctx.guild.id)]

                                with open('data/bot-data/prefixes.json', 'w')as f:
                                    json.dump(prefixes, f, indent=4)
                            embed_F.add_field(name='Prefixes:', value='`D., d.`')

                        else:
                            embed_F.add_field(name='Prefixes:', value='`' + ', '.join(prefixes[str(ctx.guild.id)]) + '`')

                        await ctx.send(embed=embed_F)

                    else:
                        embed_G = discord.Embed(
                            colour=discord.Colour.from_rgb(255, 0, 0),
                            title='Error!',
                            description=f"It seems that `{message.content}` isn't a registered prefix in your server/guild.\n\n"
                                        f"**Prefixes:** " + ', '.join(prefixes[str(ctx.guild.id)])
                        )
                        await ctx.send(embed=embed_G)

            # if choice.lower() != 'add' or 'remove':
            #     embed_G = discord.Embed(
            #         colour=discord.Colour.from_rgb(255, 0, 0),
            #         title='Oh No!',
            #         description=f"Looks like **`{choice}`** isn't a valid argument, try `add` to add a prefix or `remove` to remove a prefix!"
            #     )
            #     await ctx.send(embed=embed_G)

    @prefix.error
    async def prefix_error(self, ctx, error):
        with open('data/bot-data/prefixes.json', 'r')as f:
            prefixes = json.load(f)
        if isinstance(error, commands.MissingRequiredArgument):
            embed_A = discord.Embed(
                colour=discord.Colour.from_rgb(229, 255, 0),
                title='Prefixes!',
                description='Prefixes are a unique key to access my commands!'
            )
            if str(ctx.guild.id) in prefixes:
                embed_A.add_field(name='Prefixes:', value='`' + ', '.join(prefixes[str(ctx.guild.id)]) + '`')

            else:
                embed_A.add_field(name='Prefixes:', value='D., d.')

            embed_A.add_field(name='Arguments:', value='`add` adds a prefix.\n`remove` removes a prefix.')
            embed_A.set_footer(text='Type prefix add or remove use these arguments')

            await ctx.send(embed=embed_A)

        if isinstance(error, commands.MissingPermissions):
            embed_B = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error!",
                description="You're missing the `Administrator` permission to use this command.\n\n"
                            "Contact a mod or admin for help!"
            )
            embed_B.set_footer(text=f'If this information is wrong, please Private Message {developers}')
            await ctx.send(embed=embed_B)


def setup(client):
    client.add_cog(Prefix(client))

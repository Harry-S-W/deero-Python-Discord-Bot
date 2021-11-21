import discord
from discord.ext import commands
import json
from main import client


class Newsletter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Newsletter Command are online!')

    @commands.command()
    async def newsletter(self, ctx):
        with open('data/grouped-user-data/newsletter.json', 'r')as f:
            newsletter_data = json.load(f)

        embed_A = discord.Embed(
            colour=discord.Colour.from_rgb(229, 255, 0),
            title="Deero Newsletter!",
            description="Welcome to the Deero newsletter! \nThis a system to send out information about me quickly and efficiently!\n\n"
                        "**Why should I subscribe?** Subscribing gives you up-to-date information to help manage your servers and server staff!\n\n"
                        "**How much is it?** Subscribing is free! You can also unsubscribe at any moment!\n\n"
                        "**To subscribe**, simply type `sub` below this message! :smile:\n\n"
                        "**To unsubscribe**, simply type `unsub` or below this message! :smile:"
        )
        embed_A.set_footer(text="Type 'cancel' or ignore this message to cancel your request!")
        await ctx.send(embed=embed_A)

        def check(message):
            return message.author == ctx.author

        message = await client.wait_for('message', check=check)

        # Cancelling message

        if message.content.lower() == 'cancel':
            embed_B = discord.Embed(
                title="Okie Dokie!",
                description="Your request was cancelled, have a great day!"
            )
            await ctx.send(embed=embed_B)

        if message.content.lower() == 'sub' and 'subscribe':
            if str(ctx.author.id) not in newsletter_data:
                newsletter_data[str(ctx.author.id)] = 'subscribed'

                with open('data/grouped-user-data/newsletter.json', 'w')as f:
                    json.dump(newsletter_data, f, indent=4)

                embed_D = discord.Embed(
                    colour=discord.Colour.from_rgb(26, 255, 0),
                    title="Hooray!",
                    description="You've successfully subscribed to my newsletter!\n\n"
                                "**Expect DMs from me every so often regarding major updates and or changes!**\n\n"
                                "*If we do not share a server, you will not be able to receive updates*!"
                )
                return await ctx.send(embed=embed_D)

            if str(ctx.author.id) in newsletter_data:
                embed_C_error = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 0, 0),
                    title="Error!",
                    description="It seems you're already subsribed to the newsletter!\n\n"
                                "**To unsubscribe**, simply type `unsub` or `unsubscribe` below this message! :smile:"
                )
                embed_C_error.set_footer(text="Type 'cancel' to cancel this request")
                await ctx.send(embed=embed_C_error)
                messageA = await client.wait_for('message', check=check)

                if messageA.content.lower() == 'cancel':
                    embed_C_error_C = discord.Embed(
                        colour=discord.Colour.from_rgb(26, 255, 0),
                        title="Okie Dokie!",
                        description="Your request was cancelled, have a great day!"
                    )
                    await ctx.send(embed=embed_C_error_C)

                if messageA.content.lower() == 'unsub' and 'unsubscribe':
                    del newsletter_data[str(ctx.author.id)]

                    with open('data/grouped-user-data/newsletter.json', 'w')as f:
                        json.dump(newsletter_data, f, indent=4)

                        embed_C_error_A = discord.Embed(
                            colour=discord.Colour.from_rgb(26, 255, 0),
                            title='Bye Bye!',
                            description="You've successfully unsubscribed from our newsletter, you will **no** longer continue to get messages from us.\n\n"
                                        "`If you continue to get updates, please message a developer.`"
                        )
                        embed_C_error_A.set_footer(text='Use command "developer" to see a list of developers and contacts!')
                        await ctx.send(embed=embed_C_error_A)

        if message.content.lower() == 'unsub' and 'unsubscribed':

            if str(ctx.author.id) in newsletter_data:
                del newsletter_data[str(ctx.author.id)]

                with open('data/grouped-user-data/newsletter.json', 'w')as f:
                    json.dump(newsletter_data, f, indent=4)

                embed_A = discord.Embed(
                    colour=discord.Colour.from_rgb(26, 255, 0),
                    title='Bye Bye!',
                    description="You've successfully unsubscribed from our newsletter, you will **no** longer continue to get messages from us.\n\n"
                                "`If you continue to get updates, please message a developer.`"
                    )
                return await ctx.send(embed=embed_A)

            if str(ctx.author.id) not in newsletter_data:
                embed_C_error = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 0, 0),
                    title="Error!",
                    description="It seems you're already unsubscribed from the newsletter!\n\n"
                                "**To subscribe**, simply type `sub` or `subscribe` below this message! :smile:"
                )
                embed_C_error.set_footer(text="Type 'cancel' to cancel this request")
                await ctx.send(embed=embed_C_error)
                messageB = await client.wait_for('message', check=check)

                if messageB.content.lower() == 'cancel':
                    embed_C_error_C = discord.Embed(
                        colour=discord.Colour.from_rgb(26, 255, 0),
                        title="Okie Dokie!",
                        description="Your request was cancelled, have a great day!"
                    )
                    await ctx.send(embed=embed_C_error_C)

                if messageB.content.lower() == 'sub' and 'subscribe':
                    newsletter_data[str(ctx.author.id)] = 'subscribed'

                    with open('data/grouped-user-data/newsletter.json', 'w')as f:
                        json.dump(newsletter_data, f, indent=4)

                    embed_C_error_A = discord.Embed(
                        colour=discord.Colour.from_rgb(26, 255, 0),
                        title="Hooray!",
                        description="You've successfully subscribed to my newsletter!\n\n"
                                    "**Expect DMs from me every so often regarding major updates and or changes!**\n\n"
                                    "*If we do not share a server, you will not be able to receive updates*!"
                    )
                    embed_C_error_A.set_footer(text='Use command "developer" to see a list of developers and contacts!')
                    await ctx.send(embed=embed_C_error_A)


    # @newsletter.error
    # async def newsletter_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         embed_C = discord.Embed(
    #             colour=discord.Colour.from_rgb(229, 255, 0),
    #             title="Newsletter!",
    #             description="The Deero newsletter is a system to make sure you receive relevant and up to date information"
    #                         " related to Deero. Why should I subscribe? Subscribing will give you up to date updates and even special gifts"
    #                         " for your custom profile, as well as unique features you can use whilst using Deero."
    #                         " Subscribing will also give you a 20% discount on premium subscriptions and gifts! `(not yet available)`"
    #         )
    #         embed_C.add_field(name="Subscribing:", value='type `"subscribe"` or `"sub"` to continue with subscribing!')
    #         embed_C.add_field(name="Unsubscribing:", value='type `"unsubscribe"` or `"unsub"` to unsubscribe!')
    #         await ctx.send(embed=embed_C)


def setup(client):
    client.add_cog(Newsletter(client))


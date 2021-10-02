import discord
from discord.ext import commands
import json


class Newsletter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Newsletter Command are online!')

    @commands.command()
    async def newsletter(self, ctx, option):
        with open('data/grouped-user-data/newsletter.json', 'r')as f:
            newsletter_data = json.load(f)

        if option.lower() == 'join':

            if str(ctx.author.id) in newsletter_data:
                embed_A = discord.Embed(
                    colour=discord.Colour.from_rgb(255, 0, 0),
                    title="Error!",
                    description=f"{ctx.author.mention}, you're already subscribed to the newsletter. If you'd like to edit your subscription "
                                f"please use the `newsletter edit` command. If you'd like to cancel your subscription, please "
                                f"use the `newsletter stop` command."
                )
                embed_A.set_footer(text="Use the newsletter command to get a more in depth tutorial.")
                await ctx.send(embed=embed_A)

    @newsletter.error
    async def newsletter_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed_C = discord.Embed(
                colour=discord.Colour.from_rgb(229, 255, 0),
                title="Newsletter!",
                description="The Deero newsletter is a system to make sure you receive relevant and up to date information"
                            " related to Deero. Why should I subscribe? Sunscribing will give you up to date updates and even special gifts"
                            " for your custom profile, as well as unique features you can use whilst using Deero."
                            " Subscribing will also give you a 20% discount on premium and premium gifts. `(not yet available)`"
            )
            embed_C.add_field(name="Subscribing:", value='type `"subscribe"` or `"sub"` to continue with subscribing!')
            embed_C.add_field(name="Unsubscribing:", value='type `"unsubscribe"` or `"unsub"` to unsubscribe!')
            await ctx.send(embed=embed_C)


def setup(client):
    client.add_cog(Newsletter(client))


import discord
from discord.ext import commands
import json
import os
from cryptography.fernet import Fernet

developers = 'eal#2402, ronin#3880'


async def command_prefix(client, message):
    with open('data/bot-data/prefixes.json', 'r')as f:
        command__prefix = json.load(f)

    if message.channel.type is discord.ChannelType.private or str(message.guild.id) not in command__prefix:
        prefix = ['d.', 'D.']
        return prefix

    if str(message.guild.id) in command__prefix:
        return command__prefix[str(message.guild.id)]


client = commands.Bot(command_prefix=command_prefix, case_insensitive=True)


@client.event
async def on_guild_join(guild):
    if os.path.isdir(f'data/dataer-per-server/{guild.id}'):
        print('In this server before!')

    if not os.path.isdir(f'data/dataer-per-server/{guild.id}'):
        os.makedirs(f'data/dataer-per-server/{guild.id}')  # info_counts.json
        os.makedirs(f'data/dataer-per-server/{guild.id}/server')  # messages_sent.json
        os.makedirs(f'data/dataer-per-server/{guild.id}/server/channels')  # categories-channels--permissions.json
        os.makedirs(f'data/dataer-per-server/{guild.id}/members')  # permissions_per_member.json # messages_per_member.json

        with open(f'data/dataer-per-server/{guild.id}/server/messages_sent.json', 'x'):
            pass
        with open(f'data/dataer-per-server/{guild.id}/info_counts.json', 'x'):
            pass
        with open(f'data/dataer-per-server/{guild.id}/server/channels/categories-channels--permissions.json', 'x'):
            pass
        with open(f'data/dataer-per-server/{guild.id}/members/permissions_per_member.json', 'x'):
            pass
        with open(f'data/dataer-per-server/{guild.id}/members/messages_per_member.json', 'x'):
            pass

        # Info Counts:
        # Counts members, text channels and voice channels.

        member_counts = len(guild.members)
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)

        info_counts = {
            "members ONLY": member_counts,
            "text channels": text_channels,
            "voice channels": voice_channels
        }

        # Message counter
        # Counts text and media messages

        txt_messages = 0
        media_messages = 0

        messages_sent = {
            "text messages": txt_messages,
            "media messages": media_messages
        }

        # permissions per member
        # This gets each members permission. They are only in this sytem when they send a message.

        # Yet to be coded

        # Channel/Categories Permissions

        # messages per person.
        # This adds up the messages sent from each person

        placeholder = {}

        # Message per author
        # Tracks all messages said by a person

        with open(f'data/dataer-per-server/{guild.id}/members/permissions_per_member.json', 'w')as f:
            json.dump(placeholder, f, indent=4)

        with open(f'data/dataer-per-server/{guild.id}/server/channels/categories-channels--permissions.json', 'w')as f:
            json.dump(placeholder, f, indent=4)

        with open(f'data/dataer-per-server/{guild.id}/members/messages_per_member.json', 'w')as f:
            json.dump(placeholder, f, indent=4)

        with open(f'data/dataer-per-server/{guild.id}/info_counts.json', 'w')as f:
            json.dump(info_counts, f, indent=4)

        with open(f'data/dataer-per-server/{guild.id}/server/messages_sent.json', 'w')as f:
            json.dump(messages_sent, f, indent=4)


@client.command()
async def test_newsletter_announcement(ctx):
    with open('data/grouped-user-data/newsletter.json', 'r')as f:
        newsletter_data = json.load(f)

    newsletter_list = list(newsletter_data.keys())

    Newsletter_Message = discord.Embed(
        title="Introducing A New Update!",
        description="***This update includes the following:***\n\n"
                    "   🔵 New clear command limiter\n\n"
                    "   🔵 More advanced server storage\n\n"
                    "   🔵 Kick command now kicks multiple people\n\n"
                    "   🔵 Unban command now working"
    )
    Newsletter_Message.set_footer(text="This is simply a test")

    def check(message):
        return message.author == ctx.author

    await ctx.send("Are you sure you want to send this message? type `YES` in all caps")
    await ctx.send(embed=Newsletter_Message)

    message = await client.wait_for('message', check=check)
    if message.content == "YES":

        for user_id in newsletter_list:
            user = await client.fetch_user(user_id)
            await user.send(embed=Newsletter_Message)

            Embed_A = discord.Embed(
                title="Great!",
                description=f"**I sent a message to this user:**\n*{user}*"
            )
            await ctx.send(embed=Embed_A)

    else:
        await ctx.send("||**REQUEST CANCELLED** -- Error In Confirmation||\n\n"
                       "**||TRY - AGAIN||**")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODg2MDM1Mjc1NzU3Nzg5MjM1.YTvupw.V7DLFLiuu5465LUKl_F5tyX2toA')

import discord
from discord.ext import commands
import json
import os

developers = 'eal#2402'


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

        placeholder = {
            "placeholder": 0
        }

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


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('ODg2MDM1Mjc1NzU3Nzg5MjM1.YTvupw.urDdgbcjQnup82iND-0Cv2ir-No')

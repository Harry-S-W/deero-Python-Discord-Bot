import discord
from discord.ext import commands
import json
import os
from main import client
from main import developers
import os


class MessageTracking(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Message Trackers are online!')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == client.user:
            return

        # Logging user messaging

        with open(f'data/dataer-per-server/{message.guild.id}/members/messages_per_member.json', 'r')as f:
            mpm = json.load(f)

        def cust_id():
            return os.urandom(10)

        if cust_id() in mpm:
            cust_id()

        messages = message.content
        timeSent = message.created_at
        author = message.author
        memberId = message.author.id
        channelId = message.channel.id
        channelName = message.channel
        message_database_ID = cust_id()

        mpm[str(message_database_ID)] = {
            "message": messages,
            "time sent": str(timeSent),
            "author": str(author),
            "member ID": str(memberId),
            "channel ID": str(channelId),
            "channel name": str(channelName)
        }

        with open(f'data/dataer-per-server/{message.guild.id}/members/messages_per_member.json', 'w')as f:
            json.dump(mpm, f, indent=4)


def setup(client):
    client.add_cog(MessageTracking(client))

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

        if len(mpm) < 1000:
            messages = message.content
            timeSent = message.created_at
            author = message.author
            memberId = message.author.id
            channelId = message.channel.id
            channelName = message.channel

            mpm.append({
                "message ID": f"**Message ID:** {str(message.id)}\n",
                "message": f"**Message:** {messages}\n",
                "time sent": f"**Time Sent:** {str(timeSent)}\n",
                "author": f"**Author:** {str(author)}\n",
                "member ID": f"**Author ID:** {str(memberId)}\n",
                "channel ID": f"**Channel ID:** {str(channelId)}\n",
                "channel name": f"**Channel Name:** {str(channelName)}\n",
                "message link": f"**Message Link:** [to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})"
            })

            with open(f'data/dataer-per-server/{message.guild.id}/members/messages_per_member.json', 'w')as f:
                json.dump(mpm, f, indent=4)

        if len(mpm) >= 1000:

            del mpm[0]

            messages = message.content
            timeSent = message.created_at
            author = message.author
            memberId = message.author.id
            channelId = message.channel.id
            channelName = message.channel

            mpm.append({
                "message ID": f"**Message ID:** {str(message.id)}\n",
                "message": f"**Message:** {messages}\n",
                "time sent": f"**Time Sent:** {str(timeSent)}\n",
                "author": f"**Author:** {str(author)}\n",
                "member ID": f"**Author ID:** {str(memberId)}\n",
                "channel ID": f"**Channel ID:** {str(channelId)}\n",
                "channel name": f"**Channel Name:** {str(channelName)}\n",
                "message link": f"**Message Link:** [to message](https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id})"
            })

            with open(f'data/dataer-per-server/{message.guild.id}/members/messages_per_member.json', 'w')as f:
                json.dump(mpm, f, indent=4)

            print("Message Storage Limit Reached")

    @commands.command()
    async def message(self, ctx):
        with open(f'data/dataer-per-server/{ctx.guild.id}/members/messages_per_member.json', 'r')as f:
            mpm = json.load(f)

        mpm11 = []
        mpm22 = []
        mpm33 = []
        mpm44 = []
        mpm55 = []
        mpm66 = []
        mpm77 = []
        mpm88 = []
        mpm99 = []
        mpm00 = []
        mpm010 = []
        mpm011 = []
        mpm012 = []
        mpm013 = []
        mpm014 = []
        mpm015 = []
        mpm016 = []
        mpm017 = []
        mpm018 = []
        mpm019 = []
        mpm020 = []

        if len(mpm) >= 15:
            # Last in JSON

            for a in [mpm[-1]['message']]:
                mpm11.append(a)
            for aa in [mpm[-1]['author']]:
                mpm11.append(aa)
            for aaa in [mpm[-1]['message link']]:
                mpm11.append(f"{aaa}\n\n")
            mpm1 = ' | '.join(str(a) for a in mpm11)

            # 2nd last in JSON

            for b in [mpm[-2]['message']]:
                mpm22.append(b)
            for bb in [mpm[-2]['author']]:
                mpm22.append(bb)
            for bbb in [mpm[-2]['message link']]:
                mpm22.append(f"{bbb}\n\n")
            mpm2 = ' | '.join(str(b) for b in mpm22)

            # 3rd last in JSON

            for c in [mpm[-3]['message']]:
                mpm33.append(c)
            for cc in [mpm[-3]['author']]:
                mpm33.append(cc)
            for ccc in [mpm[-3]['message link']]:
                mpm33.append(f"{ccc}\n\n")
            mpm3 = ' | '.join(str(c) for c in mpm33)

            # 4th last in JSON

            for d in [mpm[-4]['message']]:
                mpm44.append(d)
            for dd in [mpm[-4]['author']]:
                mpm44.append(dd)
            for ddd in [mpm[-4]['message link']]:
                mpm44.append(f"{ddd}\n\n")
            mpm4 = ' | '.join(str(d) for d in mpm44)

            # 5th last in JSON

            for e in [mpm[-5]['message']]:
                mpm55.append(e)
            for ee in [mpm[-5]['author']]:
                mpm55.append(ee)
            for eee in [mpm[-5]['message link']]:
                mpm55.append(f"{eee}\n\n")
            mpm5 = ' | '.join(str(e) for e in mpm55)

            # 6th last in JSON

            for f in [mpm[-6]['message']]:
                mpm66.append(f)
            for ff in [mpm[-6]['author']]:
                mpm66.append(ff)
            for fff in [mpm[-6]['message link']]:
                mpm66.append(f"{fff}\n\n")
            mpm6 = ' | '.join(str(f) for f in mpm66)

            # 7th last in JSON

            for g in [mpm[-7]['message']]:
                mpm77.append(g)
            for gg in [mpm[-7]['author']]:
                mpm77.append(gg)
            for ggg in [mpm[-7]['message link']]:
                mpm77.append(f"{ggg}\n\n")
            mpm7 = ' | '.join(str(f) for f in mpm77)

            # 8th last in JSON

            for h in [mpm[-8]['message']]:
                mpm88.append(h)
            for hh in [mpm[-8]['author']]:
                mpm88.append(hh)
            for hhh in [mpm[-8]['message link']]:
                mpm88.append(f"{hhh}\n\n")
            mpm8 = ' | '.join(str(f) for f in mpm88)

            # 9th last in JSON

            for i in [mpm[-9]['message']]:
                mpm99.append(i)
            for ii in [mpm[-9]['author']]:
                mpm99.append(ii)
            for iii in [mpm[-9]['message link']]:
                mpm99.append(f"{iii}\n\n")
            mpm9 = ' | '.join(str(f) for f in mpm99)

            # 10th last in JSON

            for j in [mpm[-10]['message']]:
                mpm010.append(j)
            for jj in [mpm[-10]['author']]:
                mpm010.append(jj)
            for jjj in [mpm[-10]['message link']]:
                mpm010.append(f"{jjj}\n\n")
            mpm10 = ' | '.join(str(f) for f in mpm010)

            # 11th last in JSON

            for k in [mpm[-11]['message']]:
                mpm011.append(k)
            for kk in [mpm[-11]['author']]:
                mpm011.append(kk)
            for kkk in [mpm[-11]['message link']]:
                mpm011.append(f"{kkk}\n\n")
            mpm0011 = ' | '.join(str(f) for f in mpm011)

            # 12th last in json

            for l in [mpm[-12]['message']]:
                mpm012.append(l)
            for ll in [mpm[-12]['author']]:
                mpm012.append(ll)
            for lll in [mpm[-12]['message link']]:
                mpm012.append(f"{lll}\n\n")
            mpm0012 = ' | '.join(str(f) for f in mpm012)

            # 13th last in json

            for m in [mpm[-13]['message']]:
                mpm013.append(m)
            for mm in [mpm[-13]['author']]:
                mpm013.append(mm)
            for mmm in [mpm[-13]['message link']]:
                mpm013.append(f"{mmm}\n\n")
            mpm0013 = ' | '.join(str(f) for f in mpm013)

            # 14th last in json

            for n in [mpm[-14]['message']]:
                mpm014.append(n)
            for nn in [mpm[-14]['author']]:
                mpm014.append(nn)
            for nnn in [mpm[-14]['message link']]:
                mpm014.append(f"{nnn}\n\n")
            mpm0014 = ' | '.join(str(f) for f in mpm014)

            # 15th last in json

            for o in [mpm[-15]['message']]:
                mpm015.append(o)
            for oo in [mpm[-15]['author']]:
                mpm015.append(oo)
            for ooo in [mpm[-15]['message link']]:
                mpm015.append(f"{ooo}\n\n")
            mpm0015 = ' | '.join(str(f) for f in mpm015)

            mpm1 = ' | '.join(str(a) for a in mpm11)
            mpm2 = ' | '.join(str(b) for b in mpm22)
            mpm3 = ' | '.join(str(c) for c in mpm33)
            mpm4 = ' | '.join(str(d) for d in mpm44)
            mpm5 = ' | '.join(str(e) for e in mpm55)
            mpm6 = ' | '.join(str(f) for f in mpm66)
            mpm7 = ' | '.join(str(f) for f in mpm77)
            mpm8 = ' | '.join(str(f) for f in mpm88)
            mpm9 = ' | '.join(str(f) for f in mpm99)
            mpm10 = ' | '.join(str(f) for f in mpm010)
            mpm0011 = ' | '.join(str(f) for f in mpm011)
            mpm0012 = ' | '.join(str(f) for f in mpm012)
            mpm0013 = ' | '.join(str(f) for f in mpm013)
            mpm0014 = ' | '.join(str(f) for f in mpm014)
            mpm0015 = ' | '.join(str(f) for f in mpm015)

            embed_A = discord.Embed(
                colour=discord.Colour.from_rgb(229, 255, 0),
                title="Last 15 Messages",
                description=f'{mpm0015}'
                            f'{mpm0014}'
                            f'{mpm0013}'
                            f'{mpm0012}'
                            f'{mpm0011}'
                            f'{mpm10}'
                            f'{mpm9}'
                            f'{mpm8}'
                            f'{mpm7}'
                            f'{mpm6}'
                            f'{mpm5}'
                            f'{mpm4}'
                            f'{mpm3}'
                            f'{mpm2}'
                            f'{mpm1}'
            )
            await ctx.send(embed=embed_A)

        if len(mpm) < 15:
            embed_B = discord.Embed(
                colour=discord.Colour.from_rgb(255, 0, 0),
                title="Error!",
                description="There needs to be at least 15 messages sent in this server to view recent messages!"
            )
            embed_B.set_footer(text="Messages from me do not count!")
            await ctx.send(embed=embed_B)

    # @message.error
    # async def message_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         pass


def setup(client):
    client.add_cog(MessageTracking(client))

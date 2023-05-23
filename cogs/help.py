import discord
from discord.ext import commands
import json


def load_changelog():
    with open('storage/changelog.json', 'r') as f:
        data = json.load(f)
        recent_version = data[-1]
    return recent_version['version'], recent_version['date']


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.version, self.date = load_changelog()

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title='Help',
            description='*Need help?*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png')
        embed.set_footer(text=f'Version {self.version} as of {self.date}.')
        embed.set_author(
            name='ToonTown Corporate Clash Bot',
            icon_url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png'
        )
        embed.add_field(
            name='My prefix:',
            value='\"`/`\"',
            inline=True
        )
        embed.add_field(
            name='About Me:',
            value='Type `/about` to learn more!',
            inline=True
        )
        embed.add_field(
            name='/cog',
            value='Returns information about a specified cog',
            inline=False
        )
        embed.add_field(
            name='/districts',
            value='Returns online districts with population information',
            inline=False
        )
        embed.add_field(
            name='/game',
            value='Returns the current status of the ToonTown Corporate Clash servers',
            inline=False
        )
        embed.add_field(
            name='/help',
            value='Returns this message',
            inline=False
        )
        embed.add_field(
            name='/hq',
            value='Returns information about a specified HQ',
            inline=False
        )
        embed.add_field(
            name='/news',
            value='Returns the latest news from the ToonTown Corporate Clash team',
            inline=False
        )
        embed.add_field(
            name='/npc',
            value='Returns information about a specified NPC',
            inline=False
        )
        embed.add_field(
            name='/invasions',
            value='Returns a list of current invasions',
            inline=False
        )
        embed.add_field(
            name='/ping',
            value='Returns the bot\'s latency',
            inline=False
        )
        embed.add_field(
            name='/playground',
            value='Returns information about a specified playground',
            inline=False
        )
        embed.add_field(
            name='/street',
            value='Returns information about a specified street',
            inline=False
        )
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Help(client))

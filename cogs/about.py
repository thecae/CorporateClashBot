import discord
from discord.ext import commands
import json


def load_changelog():
    with open('storage/changelog.json', 'r') as f:
        data = json.load(f)
        recent_version = data[-1]
    return recent_version['version'], recent_version['date']


class AboutMe(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.version, self.date = load_changelog()

    @commands.command(name='about')
    async def about(self, ctx):
        embed = discord.Embed(
            title='Lord Lowden Clear',
            description='*Head of the ToonTown Resistance Task Force*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png')
        embed.set_footer(text=f'Version {self.version} as of {self.date}.')
        embed.set_author(name='Lord Lowden Clear', icon_url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png')
        embed.add_field(name='My prefix:', value='\"`/`\"', inline=True)
        embed.add_field(name='Need help?', value='Type `/help` for assistance!', inline=True)
        embed.add_field(name='List of Commands', value='* cog\n* department\n* districts\n* game\n* headquarters\n* invasions\n* news\n* npc\n* percentages\n* ping\n* playground\n* street', inline=False)

        await ctx.reply(embed=embed, mention_author=False)


async def setup(client):
    await client.add_cog(AboutMe(client))

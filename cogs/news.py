import discord
from discord.ext import commands
import requests
from datetime import datetime

class News(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def news(self, ctx):
        api_response = requests.get('https://corporateclash.net/api/v1/launcher/news').json()
        embed = discord.Embed(
            title='News',
            description='*Latest news from the ToonTown Corporate Clash team!*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=api_response[0]['image_url'])
        embed.set_footer(text=f'Queried at {datetime.now().strftime("%H:%M:%S")}')
        embed.set_author(
            name='ToonTown Corporate Clash Bot',
            icon_url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png'
        )
        for news in api_response:
            embed.add_field(
                name=news['title'],
                value=news['summary'],
                inline=False
            )

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(News(client))

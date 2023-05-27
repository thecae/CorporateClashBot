import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class NPC(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def npc(self, ctx, *, name):
        # NPC Toons follow Title_Case
        url_term = name.title().replace(' ', '_')
        url = f'https://toontown-corporate-clash.fandom.com/wiki/{url_term}'
        page = BeautifulSoup(requests.get(url).content, 'html.parser')

        try:
            # pull NPC data
            image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
            species = page.find('div', {'data-source': 'species'}).find('div').text
            color = page.find('div', {'data-source': 'color(s)'}).find('div').text
            building = page.find('div', {'data-source': 'building'}).find('a').text
            try:
                street = page.find('div', {'data-source': 'street'}).find('a').text
            except AttributeError:
                street = 'N/A'
            playground = page.find('div', {'data-source': 'playground'}).find('a').text

            # build embed
            embed = discord.Embed(
                title=f'{name.title()}',
                description=f'*{color} {species}*',
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=image)
            embed.add_field(name='Building', value=building, inline=True)
            embed.add_field(name='Street', value=street, inline=True)
            embed.add_field(name='Playground', value=playground, inline=True)
            await ctx.reply(embed=embed, mention_author=False)
        except (AttributeError, TypeError):
            await ctx.reply(embed=discord.Embed(
                title='NPC Not Found',
                description=f'NPC **{name.title()}** was not found.',
                color=discord.Color.red()
            ), mention_author=False)


async def setup(client):
    await client.add_cog(NPC(client))

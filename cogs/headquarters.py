import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Headquarters(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hq'])
    async def headquarters(self, ctx, *, name):
        # make the request
        url_term = name.title().replace(' ', '_')
        url = f'https://toontown-corporate-clash.fandom.com/wiki/{url_term}_Headquarters'
        page = BeautifulSoup(requests.get(url).content, 'html.parser')

        # get hq information
        try:
            image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
            playground = page.find('div', {'data-source': 'connecting_playground'}).find('div').text
            facilties = page.find('div', {'data-source': 'cog_facility'}).find('div').text
            boss = page.find('div', {'data-source': 'cog_boss'}).find('div').text
            skelecog = page.find('div', {'data-source': 'skelecog'}).find('div').text
            executive = page.find('div', {'data-source': 'executive'}).find('div').text
            min_level = page.find('td', {'data-source': 'minimum_level'}).text
            max_level = page.find('td', {'data-source': 'maximum_level'}).text

            # build embed
            embed = discord.Embed(
                title=f'{name.title()} Headquarters',
                description=f'*Connecting to {playground}*',
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=image)
            embed.add_field(name='Facilities', value=facilties, inline=True)
            embed.add_field(name='Boss', value=boss, inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Skelecog Chance', value=skelecog, inline=True)
            embed.add_field(name='Executive Chance', value=executive, inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Min Level', value=min_level, inline=True)
            embed.add_field(name='Max Level', value=max_level, inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            await ctx.reply(embed=embed, mention_author=False)
        except (AttributeError, TypeError):
            await ctx.reply(embed=discord.Embed(
                title='Headquarters Not Found',
                description=f'Headquarters **{name.title()}** was not found.',
                color=discord.Color.red()
            ), mention_author=False)


async def setup(client):
    await client.add_cog(Headquarters(client))

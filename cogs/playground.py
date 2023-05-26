import discord
from discord.ext import commands
import requests
import json
from bs4 import BeautifulSoup

class Playground(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['pg'])
    async def playground(self, ctx, *, name):
        # check if playground is an abbreviation
        if len(name) < 5:
            with open('storage/playgrounds.json') as f:
                data = json.load(f)
            for pg in data:
                for key, values in pg.items():
                    if name.lower() in values:
                        name = key
                        break
        # make the request
        url_term = name.title().replace(' ', '_')
        url = f'https://toontown-corporate-clash.fandom.com/wiki/{url_term}'
        page = BeautifulSoup(requests.get(url).content, 'html.parser')

        # get playground information
        try:
            image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
            abbreviation = page.find('div', {'data-source': 'abbreviation'}).find('div').text
            treasure = page.find('div', {'data-source': 'treasure'}).find('div').text
            streets = []
            for connection in range(4):
                try:
                    streets.append(page.find('div', {'data-source': f'street{connection}'}).find('div').text)
                except AttributeError:
                    pass
            miniboss = page.find('div', {'data-source': 'miniboss'})
            if miniboss:
                miniboss = miniboss.find('div').text
            street_mgr = page.find('div', {'data-source': 'street_mgr'}).find('div').text
            kudos_mgr = page.find('div', {'data-source': 'kudos_mgr'}).find('div').text

            # build the embed
            embed = discord.Embed(
                title=f'{name.title()}',
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=image)
            embed.add_field(name='Abbreviation', value=abbreviation, inline=True)
            embed.add_field(name='Treasure', value=treasure, inline=True)
            embed.add_field(name='Streets', value='\n'.join(streets), inline=False)
            if miniboss:
                embed.add_field(name='Taskline Manager', value=miniboss, inline=True)
            embed.add_field(name='Street Manager', value=street_mgr, inline=True)
            embed.add_field(name='Kudos Manager', value=kudos_mgr, inline=True)
            embed.set_footer(text='Use [/street <name>] to learn more about a street!')
        except (AttributeError, TypeError):
            embed = discord.Embed(title='Error', description=f'{name.title()} is not a valid playground.', color=0xff0000)

        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Playground(client))

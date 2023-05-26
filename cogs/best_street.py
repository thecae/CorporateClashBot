import discord
from discord.ext import commands
import json
import requests
from bs4 import BeautifulSoup

def load_streets():
    # load the streets
    with open('storage/streets.json', 'r') as f:
        return json.load(f)

def get_icon(dept):
    # get the page
    url = f'https://toontown-corporate-clash.fandom.com/wiki/{dept}s'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')

    return page.find('img', {'alt': f'{dept.title()}emblem'})['src']

def process(name, index):
    percentages = {}
    for street in load_streets():
        for key, values in street.items():
            percentages[key] = values['Percentages'][index]

    # get the icon
    icon = get_icon(name)

    # minor fix
    for key, value in percentages.items():
        if value == '5%':
            percentages[key] = '05%'

    # sort the percentages
    percentages = {k: v for k, v in sorted(percentages.items(), key=lambda item: item[1], reverse=True)}

    # replacing the fix
    for key, value in percentages.items():
        if value == '05%':
            percentages[key] = '5%'

    # build the embed
    embed = discord.Embed(
        title=f'{name}s',
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    for key, value in percentages.items():
        embed.add_field(
            name=key,
            value=f'{value}'
        )
    return embed

class BestStreet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['p'])
    async def percentages(self, ctx, *, dept):
        if dept.title() in ['Sellbot', "Sellbots"]:
            await ctx.send(embed=process('Sellbot', 0))
        elif dept.title() in ['Cashbot', "Cashbots"]:
            await ctx.send(embed=process('Cashbot', 1))
        elif dept.title() in ['Lawbot', "Lawbots"]:
            await ctx.send(embed=process('Lawbot', 2))
        elif dept.title() in ['Bossbot', "Bossbots"]:
            await ctx.send(embed=process('Bossbot', 3))
        elif dept.title() in ['Boardbot', "Boardbots"]:
            await ctx.send(embed=process('Boardbot', 4))
        else:
            await ctx.send(embed=discord.Embed(
                title='Department Not Found',
                description=f'Department **{dept.title()}** was not found.',
                color=discord.Color.red()
            ))


async def setup(client):
    await client.add_cog(BestStreet(client))
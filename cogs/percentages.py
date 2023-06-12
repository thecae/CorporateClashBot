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

def process(name, index, playground=None):
    percentages = {}
    for street in load_streets():
        print(street)
        for key, values in street.items():
            if playground is None:
                percentages[key] = values['Percentages'][index]
            else:
                if playground in values['Playground']:
                    percentages[key] = values['Percentages'][index]

    print()
    print(percentages)

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

    title = f'{name}s' if playground is None else f'{name}s in {playground.upper()}'

    # build the embed
    embed = discord.Embed(
        title=title,
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
        ## get the playground
        if dept.__contains__(' '):
            dept, playground = dept.split(' ')
        else:
            playground = None

        ## run the process to get the percentages
        if dept.title() in ['Sellbot', "Sellbots"]:
            await ctx.reply(embed=process('Sellbot', 0, playground), mention_author=False)
        elif dept.title() in ['Cashbot', "Cashbots"]:
            await ctx.reply(embed=process('Cashbot', 1, playground), mention_author=False)
        elif dept.title() in ['Lawbot', "Lawbots"]:
            await ctx.reply(embed=process('Lawbot', 2, playground), mention_author=False)
        elif dept.title() in ['Bossbot', "Bossbots"]:
            await ctx.reply(embed=process('Bossbot', 3, playground), mention_author=False)
        elif dept.title() in ['Boardbot', "Boardbots"]:
            await ctx.reply(embed=process('Boardbot', 4, playground), mention_author=False)
        else:
            await ctx.reply(embed=discord.Embed(
                title='Department Not Found',
                description=f'Department **{dept.title()}** was not found.',
                color=discord.Color.red()
            ), mention_author=False)


async def setup(client):
    await client.add_cog(BestStreet(client))
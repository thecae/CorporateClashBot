import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

def get_cog_table(page):
    # iterate across the cogs table
    tbody = page.find('tbody')
    cogs = []

    # if table is found, get all the data
    if tbody:
        rows = tbody.find_all('tr')
        for cog in rows:
            cog_data = cog.find_all('td')
            cog_arr = [item.text.strip() for item in cog_data]
            cogs.append(cog_arr)
        # split the list by title delimiters
        result, sublist = [], []
        for item in cogs:
            if len(item) > 0:
                sublist.append(item)
            else:
                result.append(sublist)
                sublist = []
        if sublist:
            result.append(sublist)
        return result
    else:
        raise AttributeError

class Department(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['dept'])
    async def department(self, ctx, *, name):
        # get the page
        url = f'https://toontown-corporate-clash.fandom.com/wiki/{name.title()}s'
        page = BeautifulSoup(requests.get(url).content, 'html.parser')

        try:
            # get the department image
            image = page.find('img', {'alt': f'{name.title()}emblem'})['src']

            # get the cog table
            cog_table = get_cog_table(page)

            # build the embed
            embed = discord.Embed(
                title=f'The {name.title()}s',
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=image)

            # iterate through the cogs
            for cog in cog_table[1]:
                embed.add_field(
                    name=f'{cog[0]} ({cog[1]})',
                    value=f'Level: {cog[2]} - {cog[3]} // Damage Range: {cog[4]}',
                    inline=False
                )

            # iterate through the bosses
            for cog in cog_table[2]:
                embed.add_field(
                    name=f'{cog[0]} ({cog[1]})',
                    value=f'Level: {cog[2]} // Damage Range: {cog[3]}',
                    inline=False
                )

            await ctx.send(embed=embed)
        except (AttributeError, TypeError):
            await ctx.send(embed=discord.Embed(
                title='Department Not Found',
                description=f'Department **{name.title()}** was not found.',
                color=discord.Color.red()
            ))



async def setup(client):
    await client.add_cog(Department(client))

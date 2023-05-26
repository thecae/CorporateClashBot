import discord
from discord.ext import commands
import json

def load_streets(street):
    with open('storage/streets.json') as f:
        data = json.load(f)
    for street_data in data:
        if street in street_data:
            return street_data[street]
    raise LookupError(f'{street} is not a valid street.')

class Street(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['st'])
    async def street(self, ctx, *, name):
        try:
            # load street data
            street_data = load_streets(name.title())

            # get header information
            playground = street_data['Playground'][0]
            connects = street_data['Connects']

            if connects == 'Dead-End':
                # build the embed
                embed = discord.Embed(
                    title=f'{name.title()}',
                    description=f'***{playground}**. {connects} street.*',
                    color=discord.Color.blue()
                )
            else:
                # build the embed
                embed = discord.Embed(
                    title=f'{name.title()}',
                    description=f'***{playground}**. Connects to {connects}.*',
                    color=discord.Color.blue()
                )
            embed.set_thumbnail(url=street_data['Source'])
            embed.add_field(name='Cog Levels', value=street_data['Levels'], inline=True)
            embed.add_field(name='.exe Percentage', value=street_data['ExeChance'], inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name='Sellbot Perc.', value=street_data['Percentages'][0], inline=True)
            embed.add_field(name='Cashbot Perc.', value=street_data['Percentages'][1], inline=True)
            embed.add_field(name='Lawbot Perc.', value=street_data['Percentages'][2], inline=True)
            embed.add_field(name='Bossbot Perc.', value=street_data['Percentages'][3], inline=True)
            embed.add_field(name='Boardbot Perc.', value=street_data['Percentages'][4], inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.set_footer(text='Use [/playground <name>] to get information about a playground!')
            await ctx.send(embed=embed)
        except LookupError as e:
            await ctx.send(embed=discord.Embed(title='Error', description=str(e), color=0xff0000))
            return


async def setup(client):
    await client.add_cog(Street(client))

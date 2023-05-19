import discord
from discord.ext import commands
import requests
from datetime import datetime

class Districts(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('* Districts cog is online.')

    @commands.command()
    async def districts(self, ctx):
        api_response = requests.get('https://corporateclash.net/api/v1/districts.js').json()
        # sort districts by name
        api_response = sorted(api_response, key=lambda k: k['name'])
        embed = discord.Embed(
            title='Corporate Clash Districts',
            description='*Current districts in Corporate Clash.*',
            color=discord.Color.blue()
        )
        one_district = False
        for district in api_response:
            if district['online']:
                one_district = True
                embed.add_field(
                    name=f'{district["name"]}',
                    value=f'*Population*: {district["population"]}\n *Invasion*: {district["cogs_attacking"]}',
                    inline=False
                )
        if not one_district:
            embed.add_field(
                name='No districts!',
                value='No districts are currently online.',
                inline=False
            )
        embed.set_footer(text=f'Queried at {datetime.now().strftime("%H:%M:%S")}.')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Districts(client))

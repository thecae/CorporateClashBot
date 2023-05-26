import discord
from discord.ext import commands
import requests
from datetime import timedelta, datetime


class Invasions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['inv'])
    async def invasions(self, ctx, *, search_term=None):
        api_response = requests.get('https://corporateclash.net/api/v1/districts.js').json()
        api_response = sorted(api_response, key=lambda k: k['name'])
        embed = discord.Embed(
            title='Corporate Clash Invasions',
            description='*Current invasions in Corporate Clash.*',
            color=discord.Color.blue()
        )
        one_invasion = False
        for district in api_response:
            if district['invasion_online'] and (
                    search_term is None or search_term.lower() == district['name'].lower() or search_term.lower() ==
                    district['cogs_attacking'].lower()):
                one_invasion = True
                embed.add_field(
                    name=f'{district["name"]}',
                    value=f"*{district['cogs_attacking']}*: {district['count_defeated']}/{district['count_total']} defeated ({timedelta(seconds=district['remaining_time'])} remaining)",
                    inline=False
                )
        if not one_invasion:
            if search_term is None:
                embed.add_field(
                    name='No invasions!',
                    value='No invasions are currently active.',
                    inline=False
                )
            else:
                embed.add_field(
                    name='No invasions found!',
                    value=f'No invasions were found for {search_term}.',
                    inline=False
                )
        embed.set_footer(text=f'Queried at {datetime.now().strftime("%H:%M:%S")}.')
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Invasions(client))
import discord
from discord.ext import commands
import requests
from datetime import datetime

class GameDetails(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def game(self, ctx):
        api_response = requests.get('https://corporateclash.net/api/v1/game_info.js').json()
        embed = discord.Embed(
            title='Corporate Clash Game Details',
            description='*Current game details for Corporate Clash.*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/733788698277052438/1109257208442658816/lord-lowden.png')
        embed.set_footer(text=f'Queried at {datetime.now().strftime("%H:%M:%S")}')
        embed.add_field(
            name='Toons Online',
            value=f'{api_response["num_toons"]}',
            inline=False
        )
        embed.add_field(
            name='Game Online',
            value=f'{not api_response["production_closed"]}',
            inline=False
        )
        if api_response['production_closed']:
            embed.add_field(
                name='Reason',
                value=f'{api_response["production_closed_reason"]}',
                inline=False
            )
        embed.add_field(
            name='Game Version',
            value=f'{api_response["version"]}',
            inline=False
        )
        await ctx.reply(embed=embed, mention_author=False)


async def setup(client):
    await client.add_cog(GameDetails(client))

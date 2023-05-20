import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

def parse_boss(search_term):
    # fix search term to remove the acronym
    if search_term.lower() == 'vp':
        search_term, health = 'Senior_Vice_President', '"100%"'
    elif search_term.lower() == 'cfo':
        search_term, health = 'Chief_Financial_Officer', '1500'
    elif search_term.lower() in ('clo', 'oclo'):
        search_term, health = 'Chief_Legal_Officer', '1500'
    elif search_term.lower() == 'ceo':
        search_term, health = 'Chief_Executive_Officer', '2000'
    elif search_term.lower() == 'coo':
        search_term, health = 'Chief_Operating_Officer', '???'
    else:
        raise LookupError

    # use this search term to find the page
    url = f'https://toontown-corporate-clash.fandom.com/wiki/{search_term}'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')

    try:
        # get information about the cog
        position = page.find('div', {'data-source': 'position'}).find('div').text
        department = page.find('div', {'data-source': 'department'}).find('div').text
        image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
        lowest_damage = page.find('td', {'data-source': 'lowest_damage'}).text
        highest_damage = page.find('td', {'data-source': 'highest_damage'}).text

        # build the embed
        embed = discord.Embed(
            title=f'{search_term.title().replace("_", " ")}',
            description=f'*{position}, {department}*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=image)
        embed.add_field(name='Health', value=health, inline=True)
        embed.add_field(name='Lowest Damage', value=lowest_damage, inline=True)
        embed.add_field(name='Highest Damage', value=highest_damage, inline=True)
        return embed
    except AttributeError:
        print(f'Boss AttributeError: {search_term}')
        raise AttributeError

def parse_cog(search_term):
    # cogs follow Title_Case for their search term
    url_term = search_term.title().replace(' ', '_')
    url = f'https://toontown-corporate-clash.fandom.com/wiki/{url_term}'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')

    try:
        # get information about the cog
        try:
            position = page.find('div', {'data-source': 'position'}).find('a').text
        except AttributeError:
            # if here, the cog is an exe. Their formatting is slightly different for position
            position = page.find('div', {'data-source': 'position'}).find('div').text
        department = page.find('div', {'data-source': 'department'}).find('a').text
        image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
        lowest_level = page.find('td', {'data-source': 'lowest_level'}).text
        highest_level = page.find('td', {'data-source': 'highest_level'}).text
        lowest_damage = page.find('td', {'data-source': 'lowest_damage'}).text
        highest_damage = page.find('td', {'data-source': 'highest_damage'}).text

        # build the embed
        embed = discord.Embed(
            title=f'{search_term.title()}',
            description=f'*{position}, {department}*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=image)
        embed.add_field(name='Lowest Level', value=lowest_level, inline=True)
        embed.add_field(name='Highest Level', value=highest_level, inline=True)
        embed.add_field(name='Lowest Dmg.', value=lowest_damage, inline=False)
        embed.add_field(name='Highest Dmg.', value=highest_damage, inline=True)
        return embed
    except AttributeError:
        raise AttributeError

def parse_mgr(search_term):
    # if manager, follow Title_Case and search
    url_term = search_term.title().replace(' ', '_')
    url = f'https://toontown-corporate-clash.fandom.com/wiki/{url_term}'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')

    try:
        # get information about the cog
        position = page.find('div', {'data-source': 'position'}).find('a').text
        department = page.find('div', {'data-source': 'department'}).find('a').text
        image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
        health = page.find('div', {'data-source': 'hp'}).find('div').text
        level = page.find('td', {'data-source': 'level'}).text
        defense = page.find('div', {'data-source': 'defense'}).find('div').text
        lowest_damage = page.find('td', {'data-source': 'lowest_damage'}).text
        highest_damage = page.find('td', {'data-source': 'highest_damage'}).text

        # build the embed
        embed = discord.Embed(
            title=f'{search_term.title()}',
            description=f'*{position}, {department}*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=image)
        embed.add_field(name='Health', value=health, inline=True)
        embed.add_field(name='Level', value=level, inline=True)
        embed.add_field(name='Defense', value=defense, inline=True)
        embed.add_field(name='Lowest Damage', value=lowest_damage, inline=True)
        embed.add_field(name='Highest Damage', value=highest_damage, inline=True)
        return embed
    except AttributeError:
        raise AttributeError

def parse_highroller():
    url = 'https://toontown-corporate-clash.fandom.com/wiki/High_Roller'
    page = BeautifulSoup(requests.get(url).content, 'html.parser')

    try:
        # get information about the cog
        position = page.find('div', {'data-source': 'position'}).find('a').text
        department = page.find('div', {'data-source': 'department'}).find('a').text
        image = page.find('img', {'class': 'pi-image-thumbnail'})['src']
        phase1_health = page.find('td', {'data-source': 'phase1_hp'}).text
        phase3_health = page.find('td', {'data-source': 'phase3_hp'}).text
        level = page.find('td', {'data-source': 'level'}).text
        defense = page.find('div', {'data-source': 'defense'}).find('div').text
        lowest_damage = page.find('td', {'data-source': 'lowest_damage'}).text
        highest_damage = page.find('td', {'data-source': 'highest_damage'}).text

        # build the embed
        embed = discord.Embed(
            title=f'High Roller',
            description=f'*{position}, {department}*',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=image)
        embed.add_field(name='Phase 1 Health', value=phase1_health, inline=True)
        embed.add_field(name='Phase 3 Health', value=phase3_health, inline=True)
        embed.add_field(name='Level', value=level, inline=True)
        embed.add_field(name='Defense', value=defense, inline=True)
        embed.add_field(name='Lowest Damage', value=lowest_damage, inline=True)
        embed.add_field(name='Highest Damage', value=highest_damage, inline=True)
        return embed
    except AttributeError:
        raise AttributeError


class Cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('* Cog cog is online.')

    @commands.command()
    async def cog(self, ctx, *, search_term):
        # try parsing it as a manager first
        try:
            embed = parse_mgr(search_term)
            await ctx.send(embed=embed)
            return
        except AttributeError:
            pass
        # try parsing it as a boss
        try:
            embed = parse_boss(search_term)
            await ctx.send(embed=embed)
            return
        except (LookupError, AttributeError):
            pass
        # try parsing it as a cog
        try:
            embed = parse_cog(search_term)
            await ctx.send(embed=embed)
            return
        except AttributeError:
            pass
        # if we're here, we may have the high roller
        if search_term.lower() == 'high roller':
            try:
                embed = parse_highroller()
                await ctx.send(embed=embed)
                return
            except AttributeError:
                pass

        # if it's not any of these, then it's not a valid cog
        await ctx.send(embed=discord.Embed(
            title='Error',
            description=f'**{search_term}** is not a valid cog.',
            color=discord.Color.red()
        ))


async def setup(client):
    await client.add_cog(Cog(client))

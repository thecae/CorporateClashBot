from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Bounceback time: {0}ms'.format(round(self.client.latency, 2) * 100))


async def setup(client):
    await client.add_cog(Ping(client))

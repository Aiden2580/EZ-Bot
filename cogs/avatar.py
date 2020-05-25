import discord
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command()
    async def 아바타(self, ctx):
        if (ctx.message.mentions.__len__() > 0):
            for user in ctx.message.mentions:
                pfp = str(user.avatar_url)
                embed = discord.Embed(title=user.name + "님의 아바타", description="[Link]" + "(" + pfp + ")",
                                      color=0xffffff)
                embed.set_image(url=pfp)
                embed.set_footer(text="Powered by Salt Cube#7951", icon_url="https://raw.githubusercontent.com/SaltCube7/CXT/master/n_images/saltcube.jpg")
                await ctx.send(embed=embed)
        else:
            pfp = ctx.author.avatar_url
            embed = discord.Embed(title="**" + ctx.author.name + "**님의 아바타", description="",
                                color=0xffffff)
            embed.set_image(url=pfp)
            embed.set_footer(text="Powered by Salt Cube#7951", icon_url="https://raw.githubusercontent.com/SaltCube7/CXT/master/n_images/saltcube.jpg")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Avatar(client))

from urlgrabber.grabber import URLGrabber
g = URLGrabber()
import json
@bot.command()
async def cat(ctx):
  catlink = g.urlread('http://aws.random.cat/meow')
  catjson = json.loads(catlink)
  embed = discord.Embed(title="Random Cat")
  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  embed.set_image(url=catjson["file"])
  await ctx.send(embed=embed)

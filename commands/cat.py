from urlgrabber.grabber import URLGrabber
g = URLGrabber()
import json
@bot.command()
async def cat(ctx):
  # define catlink as a var containing a URLread
  catlink = g.urlread('http://aws.random.cat/meow')
  # load the JSON we get back
  catjson = json.loads(catlink)
  # embed
  embed = discord.Embed(title="Random Cat")
  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # set embed image as the file we get back from the JSON reading
  embed.set_image(url=catjson["file"])
  # send embed
  await ctx.send(embed=embed)

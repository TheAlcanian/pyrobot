from saucenao_api import SauceNao
from saucenao_api.params import DB, Hide, Bgcolor
import json
@bot.command()
async def saucenao(ctx, arg):  
  if data["saucenao_search_enabled"] == "true":
# Parameters from https://saucenao.com/user.php?page=search-api
    sauce = SauceNao(api_key=data["saucenao_api_key"],
                    testmode=0,
                     dbmask=None,
                     dbmaski=None,
                     db=DB.ALL,
                     numres=3,
                     hide=Hide.NONE,
                     bgcolor=Bgcolor.NONE)
    
    results = sauce.from_url(arg)
    
    embed = discord.Embed(title="SauceNAO Search", description="Want some sauce with that? First three results from SauceNAO.")
  
    embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    # embed.add_field(name="Voice Latency", value=str(VoiceClient.latency))
    # set this field's value to the current latency
    for result in results:
      embed.add_field(name=result.title, value=result.url)
      # send embed
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed(title="SauceNAO Search", description="Error: SauceNAO searching has been disabled by the bot host.")
  
    embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    

from urlgrabber.grabber import URLGrabber
g = URLGrabber()
import json
@bot.command()
async def error(ctx, errorsystem, erroricon, errortitle, errortext, errorbutton):
  
  errorlink = 'http://atom.smasher.org/error/' + errorsystem + '.png.php?icon=' + erroricon + '&title=' + errortitle + '&text=' + errortext + '&b1=' + errorbutton
  escapederrorlink = re.sub(' ', '%20', errorlink)
  errorlinkurlgrab = g.urlgrab(escapederrorlink, filename="lasterror.png")
  print(errorlink)
  print(escapederrorlink)
  await ctx.send(file=discord.File('lasterror.png'))

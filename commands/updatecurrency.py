@bot.command(name='updatecurrency', aliases=['updc'], brief='Updates the currency file as a test', pass_ctx=True)
async def updatecurrency(ctx):
  currencyfile = open("./currency.json", 'r+')
  json.dump(amounts, currencyfile)
  await ctx.send('Currency updated :hahayes:')

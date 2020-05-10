@bot.command(brief='Buy something, will ya!', pass_ctx=True)
async def buy(ctx, arg1, arg2):
  if arg1 == 'testitem':
    amounttoadd = int(items[str(ctx.message.author.id)]["quantity"]) + int(arg2)
    items[str(ctx.message.author.id)]["quantity"] = str(amounttoadd)
    await ctx.send('You bought ' + str(arg2) + ' testitem(s).')

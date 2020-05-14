@bot.command(brief='Buy something, will ya!', pass_ctx=True)
async def buy(ctx, arg1, arg2):
  # if argument one is the string 'testitem'
  if arg1 == 'testitem':
    # add the amount of testitems from the number in argument two
    amounttoadd = int(items[str(ctx.message.author.id)]["quantity"]) + int(arg2)
    items[str(ctx.message.author.id)]["quantity"] = str(amounttoadd)
    # send embed
    await ctx.send('You bought ' + str(arg2) + ' testitem(s).')

@bot.command(brief='Gain 100-150 PyRolls with a cooldown of 30 seconds', pass_ctx=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
  currencyfile = open("./currency.json", 'r+')
  amounts = json.load(currencyfile)
  currencyfile.close()
  currencyfile = open("./currency.json", 'w+')
  gainedcurrency = str(random.randint(100, 150))
  addamount = int(amounts[str(ctx.message.author.id)]) + int(gainedcurrency)
  amounts[str(ctx.message.author.id)] = str(addamount)
  json.dump(amounts, currencyfile)
  currencyfile.close()
  await ctx.send('You worked at an unknown area and gained ' + str(gainedcurrency) + ' PyRolls!')




@bot.command(brief='Gain 100-150 PyRolls with a cooldown of 30 seconds', pass_ctx=True)
async def work(ctx):
  #currencyfile = open("./currency.json", 'r+')
  print(amounts)
  gainedcurrency = random.randint(0, 150000000)
  addamount = int(amounts[str(ctx.message.author.id)]) + gainedcurrency
  amounts[str(ctx.message.author.id)] = str(addamount)
  json.dump(amounts, currencyfile)
  print(amounts)
  await ctx.send('You worked at an unknown area and gained ' + str(gainedcurrency) + ' PyRolls!')

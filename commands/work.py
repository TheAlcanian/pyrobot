@bot.command(brief='Gain 100-150 PyRolls with a cooldown of 30 seconds', pass_ctx=True)
async def work(ctx):
  currencyfile = open("./currency.json", 'r+')
  amounts = json.load(currencyfile)
  currencyfile.close()
  currencyfile = open("./currency.json", 'w+')
  print(amounts)
  gainedcurrency = random.randint(100, 150)
  addamount = int(amounts[str(ctx.message.author.id)]) + gainedcurrency
  amounts[str(ctx.message.author.id)] = str(addamount)
  json.dump(amounts, currencyfile)
  currencyfile.close()
  await ctx.send('You worked at an unknown area and gained ' + str(gainedcurrency) + ' PyRolls!')



# pr.register code for use
#  id = ctx.message.author.id
#  if str(id) not in amounts:
#    currencyfile = open('./currency.json', 'r+')
#    json.load(currencyfile)
#    amounts[id] = str("100")
#    json.dump(amounts, currencyfile)
#    await ctx.send(embed=successEmbed)
#    currencyfile.close()
#    currencyfile = open('./currency.json', 'r')
#    currencyfile.read()
#    currencyfile.close()
#  else:
#    await ctx.send(embed=failiureEmbed)


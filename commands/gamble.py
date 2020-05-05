@bot.command(brief='Bet any amount of PyRolls and either lose them or 2x them', pass_ctx=True)
async def gamble(ctx, arg):

  badArgEmbed = discord.Embed(title="Gambling", description="That isn't a number!")
  badArgEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  
  if str.isdigit(arg):
    currencyfile = open('./currency.json', 'r')
    amounts = json.load(currencyfile)
    currencyfile.close()
    integerargument = int(arg)
    if random.randint(1, 2) == 2:
      gainedcurrency = int(arg) * 2
    else:
      gainedcurrency = 0

    #money gain embed
    moneyGainedEmbed = discord.Embed(title="Gambling", description="Gambling away your PyRolls got you...")
    moneyGainedEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    moneyGainedEmbed.add_field(name=str(gainedcurrency) + ' PyRolls!', value='Don\'t spend it all on one thing!')
    #money lost embed
    moneyLostEmbed = discord.Embed(title="Gambling", description="Gambling away your PyRolls got you...")
    moneyLostEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    moneyLostEmbed.add_field(name=str(gainedcurrency) + ' PyRolls...', value='Better luck next time!')
    #dont have enough money embed
    noMoneyEmbed = discord.Embed(title="Gambling", description="You don't have enough PyRolls!")
    noMoneyEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")


    #if user doesnt have enough pyrolls to fufill the requirement for the bet they chose then ignore it and tell them they dont have enough
    currentuseramount = int(amounts[str(ctx.message.author.id)])
    if int(currentuseramount) <= int(int(arg) - 1):
      await ctx.send(embed=noMoneyEmbed)
      return

    #debugging
    print(integerargument)
    
    amountlost = currentuseramount - int(arg)
    amounts[str(ctx.message.author.id)] = int(amountlost)
    addamount = int(amounts[str(ctx.message.author.id)]) + gainedcurrency
    amounts[str(ctx.message.author.id)] = str(addamount)
    currencyfile = open('./currency.json', 'w')
    json.dump(amounts, currencyfile)
    currencyfile.close()
    print(amounts)
    if gainedcurrency == 0:
      amountlost = currentuseramount - int(arg)
      amounts[str(ctx.message.author.id)] = int(amountlost)
      currencyfile = open('./currency.json', 'w')
      json.dump(amounts, currencyfile)
      currencyfile.close()
      await ctx.send(embed=moneyLostEmbed)
    else:
      await ctx.send(embed=moneyGainedEmbed)
  else:
    await ctx.send(embed=badArgEmbed)

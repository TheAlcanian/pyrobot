@bot.command(brief='Bet any amount of PyRolls and either lose them or 2x them', pass_ctx=True)
async def gamble(ctx, arg):

  badArgEmbed = discord.Embed(title="Gambling", description="That isn't a number!")
  badArgEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  
  if str.isdigit(arg):

    integerargument = int(arg)
    gainedcurrency = random.choice([integerargument * 2, 0])
    moneyGainedEmbed = discord.Embed(title="Gambling", description="Gambling away your PyRolls got you...")
    moneyGainedEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    moneyGainedEmbed.add_field(name=str(gainedcurrency) + ' PyRolls!', value='Don\'t spend it all on one thing!')
    moneyLostEmbed = discord.Embed(title="Gambling", description="Gambling away your PyRolls got you...")
    moneyLostEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    moneyLostEmbed.add_field(name=str(gainedcurrency) + ' PyRolls...', value='Better luck next time!')
    noMoneyEmbed = discord.Embed(title="Gambling", description="You don't have enough PyRolls!")
    noMoneyEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    
    currentuseramount = int(amounts[str(ctx.message.author.id)])
    if int(currentuseramount) <= int(int(arg) - 1):
      await ctx.send(embed=noMoneyEmbed)
      return
    print(integerargument)
    amountlost = currentuseramount - int(arg)
    amounts[str(ctx.message.author.id)] = int(amountlost)
    addamount = int(amounts[str(ctx.message.author.id)]) + gainedcurrency
    amounts[str(ctx.message.author.id)] = str(addamount)
    print(amounts)
    if gainedcurrency == 0:
      await ctx.send(embed=moneyLostEmbed)
    else:
      await ctx.send(embed=moneyGainedEmbed)
  else:
    await ctx.send(embed=badArgEmbed)

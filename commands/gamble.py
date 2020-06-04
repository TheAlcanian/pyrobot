@bot.command(brief='Bet any amount of PyRolls and either lose them or 2x them', pass_ctx=True)
async def gamble(ctx, arg):

  notRegisteredEmbed = discord.Embed(title="Error", description="PyRobot encountered an error!")
  notRegisteredEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  notRegisteredEmbed.add_field(name="Failiure...", value='Register your account first with `pr.register`!')
 
  badArgEmbed = discord.Embed(title="Gambling", description="That isn't a number!")
  badArgEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  # is the argument passed a digit or the word all?
  try:
    if str.isdigit(arg) or str(arg) == "all":
     # open the currency file, get the JSON data from it, and close the currency file
      #currencyfile = open('./currency.json', 'r')
      #amounts = json.load(currencyfile)
      #currencyfile.close()
     # is the argument passed the word all?
      if str(arg) == "all":
       # set the amount bet to everything the user has
        integerargument = int(str(database_read('currency.dbm', str(ctx.message.author.id))).strip("'"))
      else:
       # set the amount bet to the amount the user passed
        integerargument = int(arg)
      # does the user win back their pyrolls 2x or lose their pyrolls?
      if random.randint(1, 2) == 2:
        gainedcurrency = integerargument * 2
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
      currentuseramount = int(str(database_read('currency.dbm', str(ctx.message.author.id))).strip("'"))
      if int(currentuseramount) <= int(integerargument - 1):
        await ctx.send(embed=noMoneyEmbed)
        return 

    #debugging
      print(gainedcurrency)
      print(integerargument)

     #SPAGHETTI. i cant be bothered to comment this

     # amount lost is the current user's amount of pyrolls minus the amount of money they chose to bet
      amountlost = currentuseramount - integerargument
      # set user's balance to the amount of money lost. why does this work, i have no clue lol
      database_write('currency.dbm', str(ctx.message.author.id), str(amountlost))
      # add amount is the user's current amount of pyrolls plus the amount of pyrolls they gained
      addamount = int(str(database_read('currency.dbm', str(ctx.message.author.id))).strip("'")) + gainedcurrency
      # set the user's amount of pyrolls to the amount of money gained
      database_write('currency.dbm', str(ctx.message.author.id), str(addamount))
      # open the currency file to write the value, then close it
      #currencyfile = open('./currency.json', 'w')
      #json.dump(amounts, currencyfile)
      #currencyfile.close()
      # debugging
      print(int(str(database_read('currency.dbm', str(ctx.message.author.id))).strip("'")))
      # if the amount of currency the user gained was zero, set the amount of pyrolls they have to the amount lost
      if gainedcurrency == 0:
        amountlost = currentuseramount - integerargument
        database_write('currency.dbm', str(ctx.message.author.id), str(amountlost))
        # open currency file to write to it again, then close it again
        #currencyfile = open('./currency.json', 'w')
        #json.dump(amounts, currencyfile)
        #currencyfile.close()
        # send a special embed for losing money instead of gaining it
        await ctx.send(embed=moneyLostEmbed)
      else:
        # send a special embed for gaining money instead of losing it
        await ctx.send(embed=moneyGainedEmbed) 

    else:
  # send an embed which says that the user has provided a bad argument (not a digit nor the word all)
      await ctx.send(embed=badArgEmbed)
  except(KeyError):
    await ctx.send(embed=notRegisteredEmbed)

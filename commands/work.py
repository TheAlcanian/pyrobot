@bot.command(brief='Gain 100-150 PyRolls with a cooldown of 30 seconds', pass_ctx=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
  workstring = ['You worked as a frycook and gained ', 'You worked as a gas station sushi master and got paid ', 'You unclogged some toilets and gained ']

  try:
    currencyfile = open("./currency.json", 'r+')
    amounts = json.load(currencyfile)
    currencyfile.close()
    currencyfile = open("./currency.json", 'w')
    gainedcurrency = str(random.randint(100, 150))

    # we have to stick the embeds here because of how they're structured
                
    successEmbed = discord.Embed(title="Working", description=random.choice(workstring) + str(gainedcurrency) + ' PyRolls!')
                
    notRegisteredEmbed = discord.Embed(title="Error", description="PyRobot encountered an error!")
    notRegisteredEmbed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    notRegisteredEmbed.add_field(name="Failiure...", value='Register your account first with `pr.register`!')
    
    addamount = int(amounts[str(ctx.message.author.id)]) + int(gainedcurrency)
    amounts[str(ctx.message.author.id)] = str(addamount)
    json.dump(amounts, currencyfile)
    currencyfile.close()
    await ctx.send(embed=successEmbed)
  except KeyError:
    await ctx.send(embed=notRegisteredEmbed)


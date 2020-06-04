@bot.command(brief='Gain 100-150 PyRolls with a cooldown of 30 seconds', pass_ctx=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def work(ctx):
    workstring = ['You worked as a frycook and gained ', 'You worked as a gas station sushi master and got paid ', 'You unclogged some toilets and gained ']
    gainedcurrency = str(random.randint(100, 150))
    #print(database_read('currency.dbm', str(ctx.message.author.id)))
#    try:
    try:
        addamount = int(database_read('currency.dbm', str(ctx.message.author.id))) + int(gainedcurrency)
        database_write('currency.dbm', str(ctx.message.author.id), str(addamount))
    except:
        database_write('currency.dbm', str(ctx.message.author.id), str(100))
    finally:
        addamount = int(str(database_read('currency.dbm', str(ctx.message.author.id))).strip("'")) + int(gainedcurrency)
        database_write('currency.dbm', str(ctx.message.author.id), str(addamount))
    
    successEmbed = discord.Embed(title="Working", description=random.choice(workstring) + str(gainedcurrency) + ' PyRolls!')
    await ctx.send(embed=successEmbed)


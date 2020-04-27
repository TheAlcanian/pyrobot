@bot.command()
async def avatar(ctx, arg1, arg2):
  if arg1 == 'id':
    await ctx.send(ctx.guild.get_member(int(arg2)).avatar_url)
  else:
    await ctx.send(ctx.message.mentions[0].mention.avatar_url)

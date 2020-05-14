@bot.command()
async def avatar(ctx, arg1, arg2):
  # if argument one is the string 'id'
  if arg1 == 'id':
    # send user id's avatar
    await ctx.send(ctx.guild.get_member(int(arg2)).avatar_url)
  else:
    # send user's avatar from mention
    await ctx.send(ctx.message.mentions[0].mention.avatar_url)

@bot.command()
async def fortune(ctx, *args):
  fortune = subprocess.run(['fortune', 'mythical_linux'], stdout=subprocess.PIPE).stdout.decode('utf-8')
  await ctx.send("```\n" + fortune + "\n```")

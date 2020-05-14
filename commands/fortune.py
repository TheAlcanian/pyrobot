@bot.command()
async def fortune(ctx, *args):
  # runs a shell which runs Fortune. this is bad practice and i want to remove this.
  fortune = subprocess.run(['fortune', 'mythical_linux'], stdout=subprocess.PIPE).stdout.decode('utf-8')
  # send the fortune in a code block
  await ctx.send("```\n" + fortune + "\n```")

from discord.ext import commands
import discord
@bot.command()
async def eval(ctx, arg):
  varxc = compile(str(arg), '<string>', 'exec', flags=0, dont_inherit=False, optimize=-1)
  await exec(varxc)

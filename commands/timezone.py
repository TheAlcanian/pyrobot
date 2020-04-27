from discord.ext import commands
import discord
from pytz import all_timezones, common_timezones, timezone
import pytz
from datetime import datetime, date, time, timedelta
@bot.command()
async def timezone(ctx, arg1, arg2):
  if arg1 not in all_timezones:
    errorEmbed = discord.Embed(title="Error", description="Uh-oh! PyRobot encountered an error!", colour=discord.Colour(0xe04c4c))
    errorEmbed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
    errorEmbed.add_field(name="Error Description", value="One or more invalid timezones specified. Valid timezones are formatted like this: `America/Los_Angeles`. You can also use time zone names: `UTC`, `GMT`.")
    await ctx.send(embed=errorEmbed)
  embed = discord.Embed(title="Timezone Converter", description="Date and time are formatted in YYYY-mm-dd HH:MM:SS in 24-hr time.")
  embed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  embed.add_field(name=arg1, value=datetime.now(tz=pytz.timezone(arg1)))
  embed.add_field(name=arg2, value=datetime.now(tz=pytz.timezone(arg2)))
  await ctx.send(embed=embed)

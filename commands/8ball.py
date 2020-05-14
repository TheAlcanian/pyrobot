from discord.ext import commands
import discord
import random
@bot.command(name='8ball')
async def eightball(ctx, *, arg):

  # list of responses
  responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

  # embed
  embed = discord.Embed(title="Magic Eight-Ball", description="I asked the Magic Eight-Ball and they said...")

  embed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")

  embed.add_field(name="Query", value=str(arg)) 
  embed.add_field(name="Response", value=random.choice(responses))

  # send embed
  await ctx.send(embed=embed)

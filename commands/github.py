@bot.command()
async def github(ctx, arg):
  g = Github(str(data["github_api_access_token"]))
  # regex to take the argument, remove the URL portion, and strip leading forward slashes if there are any
  strarg = re.sub('https://.*.com/', '', str(arg).rstrip('/'))
  repo = g.get_repo(strarg)

  embed = discord.Embed(title="GitHub", description="GitHub repository information")

  embed.set_author(name="PyRobot", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  embed.add_field(name=strarg, value='The repo ' + strarg + ' has:\n⭐ ' + str(repo.stargazers_count) + ' Stars\n👁 ' + str(repo.watchers_count) + ' Watchers\n <:fork:714893400385781770> ' + str(repo.forks_count)  +' Forks') 
  # send embed
  await ctx.send(embed=embed)

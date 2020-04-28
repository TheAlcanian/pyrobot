from discord import Message as Message
from array import array
from discord import *
import discord
from discord import User as User
import subprocess
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import *
Client = discord.Client()
client = discord.Client()
bot = commands.Bot(command_prefix='pr.')
import os
import os.path
import re
import json
import pytz
import sys
import pycurl
from urlgrabber import urlopen

# # # Error Handler # # #

def my_exchandler(type, value, traceback):
  if type == RuntimeError:
    print("\n[SR] Recieved keyboard interrupt. Dumping currency and quitting...")
    json.dump(amounts, currencyfile)
    currencyfile.close()
    exit(0)
  if type == KeyboardInterrupt:
    print("\n[SR] Recieved keyboard interrupt. Dumping currency and quitting...")
    json.dump(amounts, currencyfile)
    currencyfile.close()
    exit(0)
  if type == SystemExit:
    print("\n[SR] Recieved keyboard interrupt. Dumping currency and quitting...")
    json.dump(amounts, currencyfile)
    currencyfile.close()
    exit(0)
  sys.__excepthook__(type, value, traceback)
print("[SR] Loading error handler...")
sys.excepthook = my_exchandler

# # # Error Handler # # #

# # # Config part # # #

# find XDG config directory from environment variable. otherwise, return current user's home directory plus /.config
config_home_incomplete = os.environ.get('XDG_CONFIG_HOME', os.environ['HOME'] + '/.config')

# take the userconfigdir variable and attatch /programname/ to it to get the dir that programname should create
config_home_complete = config_home_incomplete + '/pyrobot/'

# make program's config directory. if it already exists, don't panic. or exception.
try:
    os.mkdir(config_home_complete)
except FileExistsError:
    print('[PR] Config folder found at ' + config_home_complete + '.')
else:
    print('[PR] Config folder created at ' + config_home_complete + '.')

pathcheck = os.path.exists(config_home_complete + 'config.json')
if pathcheck:
    with open(config_home_complete + 'config.json') as json_data_file:
         data = json.load(json_data_file)
else:
    print('[PR] Uh oh! PyRobot could not start because you\'re missing a config file! Create ' + config_home_complete + 'config.json and fill it with this data:\n{\n   "token": "<bot account\'s token>"\n}')
    exit()
    
# # # Config part # # #

# # # currency # # #

currencyfile = open('./currency.json', 'r+')
amounts = json.load(currencyfile)
currencyfile.close()
currencyfile = open('./currency.json', 'w+')
print(amounts)
# json.dump(amounts, currencyfile)
# amounts = {"i":"i"}
# # # currency # # # 

# # # Dynamic loading part # # #

commands = os.listdir('./commands/')
for command in commands:
  exec(open('./commands/' + command).read())
  print('[PR] Loaded command ' + str(command).rstrip('.py') + ' from file ' + command + '.')

# # # Dynamic loading part # # #

# # # Functions # # #

async def setErrorEmbed(errorDescription):
  errorEmbed = discord.Embed(title="Error", description="Uh-oh! PyRobot encountered an error!", colour=discord.Colour(0xe04c4c))
  errorEmbed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be03dc7ac21f337884fbbe4516de.webp")
  errorEmbed.add_field(name="Error Description", value=errorDescription)
  
  
# # # Functions # # #

# # # Global code # # #

# # # Global code # # #

@bot.event
async def on_ready():
  print('[PR] PyRobot logging in as {0.user}'.format(bot))
      
bot.run(data["token"])      

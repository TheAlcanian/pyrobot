#we probably dont need this lol
#from array import array
import subprocess, os, re, json, pytz, sys, pycurl
from discord import *
from discord.ext import *
from discord.ext.commands import Bot
from urlgrabber import urlopen
from discord.ext import commands
#from commands import *
bot = commands.Bot(command_prefix='pr.')


# # # Error Handler # # #

#def my_exchandler(type, value, traceback):
#  if type == RuntimeError or KeyboardInterrupt or SystemExit:
#    print("\n[SR] Recieved keyboard interrupt. Quitting...")
#    exit(0)
#  sys.__excepthook__(type, value, traceback)
#sys.excepthook = my_exchandler

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

# # # Dynamic loading part # # #

# define the command directory as the commands variable
commands = os.listdir('./commands/')
# iterate over every command in the command directory
for command in commands:
  # run command file
  exec(open('./commands/' + command).read())
  # print a message which breaks for some reason i need to get on fixing that
  print('[PR] Loaded command ' + str(command).rstrip('.py') + ' from file ' + command + '.')

# # # Dynamic loading part # # #

# # # Functions # # #

# isnt used
#async def setErrorEmbed(errorDescription):
#  errorEmbed = discord.Embed(title="Error", description="Uh-oh! PyRobot encountered an error!", colour=discord.Colour(0xe04c4c))
#  errorEmbed.set_author(name="PyRobot", url="https://discordapp.com", icon_url="https://cdn.discordapp.com/avatars/503024140706643968/6b57be0#3dc7ac21f337884fbbe4516de.webp")
#  errorEmbed.add_field(name="Error Description", value=errorDescription)
    
# # # Functions # # #

# # # Global code # # #

# # # Global code # # #

# when bot is ready, print a message
@bot.event
async def on_ready():
  print('[PR] PyRobot logging in as {0.user}'.format(bot))

# log in as bot account defined by token in config file
bot.run(data["token"])      

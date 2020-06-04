import subprocess, os, re, json, pytz, sys, pycurl, dbm.gnu
from github import Github
from discord import *
from discord.ext import *
from discord.ext.commands import Bot
from urlgrabber import urlopen
from discord.ext import commands
bot = commands.Bot(command_prefix='pr.')

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
  # print a message for each command
    print('[PR] Loaded command file ' + command + '.')

# # # Dynamic loading part # # #

# # # Functions # # #

def database_write(database, user_id, value):
    with dbm.gnu.open(database, 'c') as db:
        db[user_id] = value

def database_read(database, user_id):
    with dbm.gnu.open(database, 'r') as db:
        return str(db.get(user_id)).lstrip('b')
        #print(db.get(user_id, 'Requested field ' + user_id + ' does not exist!'))

# # # Functions # # #


# when bot is ready, print a message
@bot.event
async def on_ready():
  print('[PR] PyRobot logging in as {0.user}'.format(bot))

# log in as bot account defined by token in config file
#await bot.change_presence(status=discord.Status.online)
bot.run(data["token"])      

# pyrobot

[![made-with-emacs](https://img.shields.io/badge/made%20with-emacs-993399.svg)](https://www.gnu.org/software/emacs/) ![contributors](https://img.shields.io/github/contributors/TheAlcanian/pyrobot?color=22BB22) ![closed-issues](https://img.shields.io/github/issues-closed-raw/TheAlcanian/pyrobot?color=00aa00) ![open-issues](https://img.shields.io/github/issues-raw/TheAlcanian/pyrobot?color=dd0000)
 
 ![stars](https://img.shields.io/github/stars/TheAlcanian/pyrobot) ![watchers](https://img.shields.io/github/watchers/TheAlcanian/pyrobot) ![forks](https://img.shields.io/github/forks/TheAlcanian/pyrobot)
 
An open-source general purpose bot with reverse image searching, a currency system, timezone conversion and a little more.

# How to host your own

Instructions:
~~install everything on pypi~~

Install `discord.py`, `urlgrabber` (i think), `pycurl` (probs dep for urlgrabber), `pytz` and `saucenao_api`

create `$XDG_CONFIG_HOME/pyrobot/config.json` (if you don't have a config_home it'll read from ~/.config)

Fill it with your token:

```
{
    "token": "<bot account token here>",
    "saucenao_api_key": "<either a SauceNAO API Key or absolutely nothing, not even a space.>",
    "saucenao_search_enabled": "<either one of true or false. this is so the bot doesnt post porn accidentially>"
}
```

Create `<pyrobot's install dir>/currency.json` and `<pyrobot's install dir>/inventory.json`

Fill those files with any dummy data so that the commands don't complain, personally I use `{"e": "e"}`.

Install [these fortunes](https://github.com/ncdulo/fortune-mod-mythical-linux) (or don't, but remember to disable the pr.fortune command, or modify it to your liking. pr.fortune doesn't work on Windows systems.)

Realise that i am not responsible for any shit that happens to your computer, check all the code you run, yada yada.

<sup>Made with emacs, the ech cat, the residents of the hackerden and incomprehensible amounts of coffee</sup>

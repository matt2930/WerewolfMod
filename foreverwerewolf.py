import datetime
import logging
import os
import discord

from discord.ext import commands


intents = discord.Intents(guilds=True, members=True, messages=True)

date = f'{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}'
logging.basicConfig(
    filename=f'logs/{date}.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot = commands.Bot(command_prefix=['wolf.', 'Wolf.'],
                   description='The wolfiest bot for discord-based Werewolf.\n'
                               'If you have questions, feel free to contact Cal.\n\n'
                               '* * * * * * * *\n'
                               'It\'s very exciting how the usage of this bot has grown, but that brings with it '
                               'added cost as it expands to more servers. If you like the bot, please consider '
                               'buying me a coffee to keep this one online: https://ko-fi.com/manticorum\n'
                               '* * * * * * * *\n',
                   case_insensitive=True,
                   intents=intents,
                   owner_id=258104532423147520)


@bot.event
async def on_ready():
    logging.info('Logged in as:')
    logging.info(bot.user.name)
    logging.info(bot.user.id)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            c = filename[:-3]
            try:
                bot.load_extension(f'cogs.{c}')
                logging.info(f'Loaded cog: {c}')
            except Exception as e:
                logging.info(f'******\nFailed to load cog: {c}')
                logging.info(f'{type(e).__name__} - {e}')


# Main
if __name__ == '__main__':
    bot.run("TOKEN_HERE")

import os
import discord
from discord.ext import commands
import aiocron
import random
from pymongo import MongoClient
from dotenv import load_dotenv 
from keep_alive import keep_alive

load_dotenv()


client = MongoClient(os.getenv('DATABASE_URL'))

CHANNEL_ID=os.getenv('CHANNEL_ID')
# members

savage_1="I'm not ready to have a conversation with you! If u want to know details use --help"
savage_2="Lol, wrong command! check --help"
savage_3="Check --help & help me not to repeat myself!"

savage_replies=[savage_1, savage_2, savage_3]

intents = discord.Intents.default()
intents.members = True

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(command_prefix='kid --', intents=intents, help_command = help_command)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.content.startswith('kid') and "Hello" in message.content:
        await message.channel.send(f'Hello <@{message.author.id}>')
    elif message.content.startswith('kid') and "--" not in message.content:
        await message.channel.send(f'<@{message.author.id}>, {savage_replies[random.randint(0,2)]}')
    else:
        await bot.process_commands(message)


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def register(ctx, user_id, mess_member=False):
    """Register an User"""
    try:
        existing_user=client.chill_xicz['users'].find_one({'user_id': user_id})
    except:
        existing_user=False
    if existing_user:
        await ctx.send(f'User: {user_id} already registered')
    else:
        gg = client.chill_xicz['users'].insert_one({
            'user_id' : user_id, 
            'mess_member': mess_member
        })
        if gg:
            await ctx.send(f'Registration successful for user: {user_id}')
        else:
            await ctx.send(f'Registration failed for user: {user_id}, please try again!')


@bot.command()
async def mention_all_registered_members(clx):
    "Mention all registerd members"
    users=client.chill_xicz['users'].distinct('user_id')
    res=f'Hello '
    for user in users:
        res+= user + ', '
    await clx.send(res)

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@aiocron.crontab('0 14,22 * * 1-7')
async def cornjob1():
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send('https://docs.google.com/spreadsheets/d/1IC3EKa-RGar6Hv7oG-ZC5fwY7-SL7QRnaigwiwx4g4s/edit?usp=sharing')
    members_list=client.chill_xicz['users'].distinct('user_id', {'mess_member':True})
    for member in members_list:
        await channel.send(f'Update your meal info <@{member}>')

keep_alive()
bot.run(os.getenv('TOKEN'))
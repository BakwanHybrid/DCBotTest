import discord
from discord.ext import commands
from pwmaker import gen_pass
import random
import os
import requests


description = "Bkwn prototype dsc bot #001"

intents = discord.Intents.default()
intents.message_content = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', description = description, intents = intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} / ID {bot.user.id}')
    print('-----LOGS BELOW-----')
 
@bot.command()
async def hello(ctx, member: discord.Member):
    """Greets the requesting user"""
    await ctx.send(f'Hello, {member.name}! {bot.user} here.')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Greets a new user joining"""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def ping(ctx):
    '''Pongs'''
    await ctx.send(f"Pong!")

@bot.command()
async def ai(ctx):
    '''This is not an AI bot bruv'''
    await ctx.send(f"This is not an AI bot bruv")

@bot.command()
async def coinflip(ctx):
    '''Flip a coin!'''
    flipped = random.choice('head','tail')
    await ctx.send(f'Coin flipped and landed on {flipped}')

@bot.command()
async def heh(ctx, count_heh = 5):
    '''hehehehehe'''
    await ctx.send("he" * count_heh)

@bot.command()
async def wordrep(ctx, times: int, content:str="Repetition in progress..."):
    '''Repeats a word input by user's request'''
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def pass_gen(ctx, pass_length=5):
    '''Generates a random password based on user's request'''
    await ctx.send(gen_pass(pass_length))

@bot.command()
async def randomimg(ctx):
    '''Sends a random image from the bot's collection'''
    with open(random.choice(random.choice(os.listdir('images'))), 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Duck'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    

bot.run('token)

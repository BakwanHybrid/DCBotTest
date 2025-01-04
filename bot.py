import discord
from pwmaker import gen_pass
import random


# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$gen_pass'):
        await message.channel.send('Generated password:', gen_pass(10))
    elif message.content.startswith('$flipcoin'):
        await message.channel.send('Coin flipped in', random.choice(['tail','head']))
    else:
        await message.channel.send(message.content)

client.run(#INSERT TOKEN HERE#)

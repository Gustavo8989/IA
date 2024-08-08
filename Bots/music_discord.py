import discord 

with open('key.txt', 'r') as key:
    key = key.read() 

intents = discord.Intents.default() 
intents.message_content = True 

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("O bot {} está logando no servidor".format(client.user)) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Olá'):
        await message.channel.send('Olá, como vai?!')

client.run(key) 

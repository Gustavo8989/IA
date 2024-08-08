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
    if massage.content.startwith('!entrar'):
        try:
            pass 


client.run(key) 
#https://discordpy.readthedocs.io/en/stable/api.html?highlight=message%20author#discord.Message.author

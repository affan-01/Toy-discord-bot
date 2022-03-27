import discord
import requests 
import json
import random

client = discord.Client()
commie = ["putin","red","comrade","commie","our","russia","ussr"]
bot_reply = ["hurrah comrade","I agree with you comrade","Karl Max would be happy to hear this"]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random/")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " " + json_data[0]['a']
  return quote
  
@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    msg = message.content
    if any(word in msg for word in commie):
        await message.channel.send(random.choice(bot_reply))


client.run('OTQ5NzA5NzQ3NzE4ODYwODAx.YiOUIA.5GYdunib6cwnxOgXZ-mY1ZvFkKU')

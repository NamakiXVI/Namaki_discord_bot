import os
import discord
from discord.ext import commands
import textwrap
import requests
import json
from server import Stay_Alive
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_message(message):
  if message.author.id == bot.user.id:
    return
  msg_content = message.content.lower()

  if "<@801759229001596937>" in message.content:
    await message.channel.send('deutsche Kartoffel wurde gepingt')

  if "<@852165907870253086>" in message.content:
    await message.channel.send('Der König wurde gepingt!')

  if "<@814477763360063499>" in message.content:
    await message.channel.send('baitet gerade in valo')

  if "<@1062010558523641866>" in message.content:
    await message.channel.send('ping nicht mich sondern die anderen')

  if "<@920346927894253600>" in message.content:
    await message.channel.send('mehr ex als die nachkommastellen von pi')

  if "<@819563812695834654>" in message.content:
    await message.channel.send('traded gerade mit stonks')

  if "<@821001543054131230>" in message.content:
    await message.channel.send('24/7 afk')

  curseWord = [
    'Nigga', 'nigga', 'Hurensohn', 'Huan', 'Bameninghong', 'ニガーニガー',
    'hurensohn', 'nuttensohn', 'bitch', 'kys', 'fick', 'b1tch', 'Bitch',
    'B1tch', 'Neger', 'Negro', 'neger', 'negro', 'huansohn', 'bastard', 'huan'
  ]

  asianWords = ['bing chilling', 'Bing Chilling', 'BING CHILLING']

  if any(word in msg_content for word in curseWord):
    await message.delete()
    await message.channel.send(
      'message got deleted cause of swearing. For more informations view the server guidelines.'
    )

  if any(word in msg_content for word in asianWords):
    await message.channel.send('du hast ein Bambusping')

  if "/meme" in message.content:
    response1 = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response1.text)
    await message.channel.send(json_data.get('url'))
    print('meme send message.channel')

  if "devmemes" in message.content:
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        'X-RapidAPI-Key': '0b2bd932d3mshc9d3922e8e75d40p1f9239jsn1c1d21dfd9e1',
        'X-RapidAPI-Host': 'programming-memes-images.p.rapidapi.com'
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        random_index = random.randint(0, len(data) - 1)
        random_image = data[random_index]["image"]
        await message.channel.send(random_image)
    else:
        await message.channel.send(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")

Stay_Alive()
bot.run(os.environ['DISCORD_TOKEN'])

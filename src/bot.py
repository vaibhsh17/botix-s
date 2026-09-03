import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

with open("data/responses.json", "r", encoding="utf-8") as file:
    data = json.load(file)

@bot.event
async def on_ready():
    print(f"Botix-S is online as {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user_message = message.context.lower()

    for item in data["resposes"]:
        if user_message == item["question"].lower():
            await message.channel.send(item["answer"])
            return


    await bot.process_commands(message)

bot.run(TOKEN)
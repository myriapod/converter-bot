import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from tools.converter import MilesToKm, KmToMiles, CtoF, FtoC

load_dotenv()
token = os.getenv('TOKEN')
print(token)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.role_channel = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'[LOG IN] We have logged in as {self.user}')

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name="milestokm", description="Convert Miles to Metric")
async def convertMilesToKm(interaction: discord.Interaction, miles:int, yards:int, feet:int, inches:int):
    result = MilesToKm(miles, yards, feet, inches)
    await interaction.response.send_message(result)

@tree.command(name="kmtomiles", description="Convert Metric to Miles")
async def convertKmToMiles(interaction: discord.Interaction, km:int, m:int, cm:int):
    result = KmToMiles(km, m, cm)
    await interaction.response.send_message(result)

@tree.command(name="ftoc", description="Convert Fahrenheit to Celsius")
async def convertFtoC(interaction: discord.Interaction, f:int):
    result = FtoC(f)
    await interaction.response.send_message(result)

@tree.command(name="ctof", description="Convert Celsius to Fahrenheit")
async def convertCtoF(interaction: discord.Interaction, c:float):
    result = CtoF(c)
    await interaction.response.send_message(result)


client.run(token)  # type:ignore
import asyncio
from discord.ext import commands
from discord import Member

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_voice_state_update(member: Member, before, after):
    if after.channel and member.id == YOUR_USER_ID:  # Replace YOUR_USER_ID with the ID of the user you want to disconnect
        await asyncio.sleep(10)  # Wait for 10 seconds
        await member.move_to(None)  # Disconnect the user from the voice channel

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("You are not connected to a voice channel.")

bot.run('YOUR_BOT_TOKEN')  # Replace YOUR_BOT_TOKEN with your Discord bot token

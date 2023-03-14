import asyncio
from discord.ext import commands
from discord import Member

bot = commands.Bot(command_prefix='!')

kick_user_id = None

@bot.event
async def on_voice_state_update(member: Member, before, after):
    global kick_user_id
    if after.channel and member.id == kick_user_id:
        await asyncio.sleep(10)
        await member.move_to(None)

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined {channel}")
    else:
        await ctx.send("You are not connected to a voice channel.")

@bot.command()
async def kick(ctx, user_id: int):
    global kick_user_id
    kick_user_id = user_id
    await ctx.send(f"User with ID {user_id} will be kicked from the voice channel after 10 seconds.")

bot.run('YOUR_BOT_TOKEN')

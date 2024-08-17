import discord
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

TOKEN = 'MTI3NDEzMjE4ODUzOTEyNTgxMA.GSZvQF.wAxALSWlsyU6UKVjmaQvagpOzxnAqxl4vaiQzg'


# Bot Event
# คําสั่ง bot พร้อมใข้งานเเล้ว

@bot.event
async def on_ready():
    print("Bot Online!")


# เเจ้งคนเข้า - ออกเซิฟเวอร์

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1270205046298251316) # idห้อง
    text = f"Welcome to the server, {member.mention}!"
    await channel.send(text) #ส่งข้อความไปที่ห้อง


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1274134507817144403) # idห้อง
    text = f"{member.name} has left the server!" 
    await channel.send(text) #ส่งข้อความไปที่ห้อง


# คําสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") #ส่งกลับไปที่ห้องนั้น

    elif mes == 'hi bot':
        await message.channel.send("Hello," + str(message.author.name))

    await bot.process_commands(message)  
    # ทําคําสั่ง evet เเล้วไปทําคําสั่ง bot command ต่อ   


# //////// commands ////////
# กําหนดคําสั่งให้บอท


@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx. author.name}!")

@bot.command()   
async def test(ctx, arg):
    await ctx.send(arg)


# Slash commands
# ยังอยู่ในช่วงฝึก


bot.run(TOKEN)   
import discord
from discord import embeds
from discord import Member
from discord import errors
from discord.ext import commands , tasks
from discord.ext.commands import cooldown
from discord.ext.commands import errors
from discord.ext.commands import check
from discord.utils import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext.commands import has_permissions, MissingPermissions
from decimal import *
import string
import time
import datetime
from itertools import cycle
import random,string,ctypes
from colorama import Fore
from datetime import datetime
from random import randint
import os
import json
import requests
import io
import aiohttp
import threading
import os
import json
import pytz, gratient
import subprocess
from discord import Member
from discord import user
from discord import embeds
from discord.embeds import Embed
from asyncio import sleep
import discord
from discord.ext import commands
import discord
from discord import embeds
from discord import Member
from discord import errors
from discord.ext import commands , tasks
from discord.ext.commands import cooldown
from discord.ext.commands import errors
from discord.ext.commands import check
from discord.utils import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
from asyncio import sleep
try:         
    os.system('color')
except: 
    print("Os Color Problem")    
    input()
    
try:
    config = json.load(open("setting.json", encoding="UTF-8"))
    prefix = config['PREFIX']
    givenrole = config['givenrole']
    money = config['money']
    stealperm = config['stealperm']
    checkperm = config['checkperm']
    buyperm = config['buyperm']
    
except: 
    print("Config Error")    
    input()
ctypes.windll.kernel32.SetConsoleTitleW(f"EZPLUS BOT")
def Clear():
    os.system("cls" if os.name == "nt" else 'clear')

activity = discord.Activity(type=discord.ActivityType.watching,name=f"EZPLUS BOT By Mrash" )
bot = commands.Bot(command_prefix=f'{prefix}', activity=activity)
bot.remove_command('help')

Start = gratient.blue(f"""
 ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ 
███████╗███████╗██████╗ ██╗     ██╗   ██╗███████╗    ██████╗  ██████╗ ████████╗
██╔════╝╚══███╔╝██╔══██╗██║     ██║   ██║██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
█████╗    ███╔╝ ██████╔╝██║     ██║   ██║███████╗    ██████╔╝██║   ██║   ██║   
██╔══╝   ███╔╝  ██╔═══╝ ██║     ██║   ██║╚════██║    ██╔══██╗██║   ██║   ██║   
███████╗███████╗██║     ███████╗╚██████╔╝███████║    ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝                          
━ Version 2.0 ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━
Current Command

    {prefix}buy GiftLink
    {prefix}steal ClothesID
    {prefix}checkname Letter Amount
""")
@bot.event
async def on_ready():
    Clear()
    print(Start)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
@commands.has_role(buyperm)    
@bot.command()
async def buy(ctx,*,url):
    
    reciver_phone_number = config['phonenumber']
    embed = discord.Embed(title="กำลังทำรายการ เติมเงิน✅", description=f"""
🥶โปรดรอ ดำเนินการซักครู่
    """, footer="Ez Plus", colour=0x7df9ff)
    embed.set_image(url="https://i.ytimg.com/vi/tU27H5a_rfs/maxresdefault.jpg")

    msg = await ctx.send(embed=embed)
    try:
        truewallet_gift_voucher_code = (url.split("https://gift.truemoney.com/campaign/?v=",1)[1])
        url = f'https://gift.truemoney.com/campaign/vouchers/{truewallet_gift_voucher_code}/verify?mobile={reciver_phone_number}'
        r = requests.get(url).json()
        json_str = json.dumps(r)
        resp = json.loads(json_str)
        truewallet_gift_owner = (resp['data']['owner_profile']['full_name'])
        truewallet_gift_message = (resp['status']['message'])
        truewallet_gift_amount = (resp['data']['voucher']['amount_baht'])
        truewallet_gift_amount_redeem = (resp['data']['voucher']['redeemed_amount_baht'])  
        truewallet_gift_status = (resp['data']['voucher']['status'])
        truewallet_gift_redeemed = (resp['data']['voucher']['redeemed'])
        truewallet_gift_redeemed_available = (resp['data']['voucher']['available'])
        truewallet_gift_url = (resp['data']['voucher']['link'])
        truewallet_gift_owner = truewallet_gift_owner.replace(' ***','')
        truewallet_gift_owner = truewallet_gift_owner.replace(' ','')
        truewallet_gift_amount_int = int(float(truewallet_gift_amount))
    except:     
        embed = discord.Embed(title="กำลังทำรายการ เติมเงิน✅", description=f"""
    🍂ลิ้งนี้ไม่สามารถใช้งานได้
        """, footer="Ez Plus", colour=0xffa6bb)
        embed.set_image(url="https://i.ytimg.com/vi/tU27H5a_rfs/maxresdefault.jpg")


    payload = {
                                    "Host": "gift.truemoney.com",
                                    "Content-Length": "59",
                                    "Sec-Ch-Ua": '" Not A;Brand";v="99", "Chromium";v="90"',
                                    "Accept": "application/json",
                                    "Sec-Ch-Ua-Mobile": "?0",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
                                    "Content-Type": "application/json",
                                    "Origin": "https://gift.truemoney.com",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Sec-Fetch-Mode": "cors",
                                    "Sec-Fetch-Dest": "empty",
                                    "Referer": f"https://gift.truemoney.com/campaign/?v={truewallet_gift_voucher_code}",
                                    "Accept-Encoding": "gzip, deflate",
                                    "Accept-Language": "en-US,en;q=0.9",
                                    "Connection": "close"
                            }
    
    get_url = (f"https://gift.truemoney.com/campaign/vouchers/{truewallet_gift_url}/redeem")
    data = {"mobile":f"{reciver_phone_number}","voucher_hash":f"{truewallet_gift_url}"}
    r = requests.post(get_url, data=json.dumps(data), headers=payload)
    if r.status_code != 200:
        embed = discord.Embed(title="รายการ เติมเงิน✅", description=f"""
🍂ทำรายการไม่สำเร็จ❌
    """, footer=" สร้างโดย Mrash#9088", colour=0x52FF00)
        embed.set_image(url="https://i.ytimg.com/vi/tU27H5a_rfs/maxresdefault.jpg")
        await msg.edit(embed=embed)
    elif r.status_code == 200:
        embed = discord.Embed(title="รายการ เติมเงิน✅", description=f"""
🍂ทำรายการสำเร็จ✅
🍂จำนวนเงินที่ได้รับ : {truewallet_gift_amount} บาท
🍂ชื่อคนสร้างซ่อง : {truewallet_gift_owner} | {ctx.author.mention}
    """, footer=" สร้างโดย Mrash#9088", colour=0x52FF00)
        embed.set_image(url="https://i.ytimg.com/vi/tU27H5a_rfs/maxresdefault.jpg")
        await msg.edit(embed=embed)
    if truewallet_gift_amount == money:
        role = discord.utils.get(ctx.guild.roles, name=givenrole)
        await ctx.author.add_roles(role)
        embed = discord.Embed(title="Auto Redeem Role", description=f"""
✅รับยศสำเร็จ✅
  """, footer=" สร้างโดย Mrash#9088", colour=0x52FF00)
        await ctx.send(embed=embed)
        

        
    
    
    
    
    
    
    
    
    await ctx.message.delete()    
@commands.has_role(stealperm)        
@bot.command()
async def steal(ctx, assetid : int):
  try:
    dataa = requests.get(f"http://api.roblox.com/Marketplace/ProductInfo?assetId={assetid}").json()
    name = dataa["Name"]
    templateid=(requests.get(f"https://assetdelivery.roblox.com/v1/asset/?id={assetid}").text.split("?id=")[1].split("</url>")[0])
    imageurl = requests.get(f"https://assetdelivery.roblox.com/v1/assetId/{templateid}").json()['location']
    image = requests.get(imageurl).content
    embed = discord.Embed(title=f"คำสั่งขโมย ไฟล์เสื้อ Roblox⭐", description=f"ขโมยสำเร็จ😎\nทำการส่งไฟล์เสื้อไปใน DM เรียบร้อย🎩", color=0x473c8b)
    
    
    async with aiohttp.ClientSession() as session:
      async with session.get(imageurl) as resp:
          if resp.status != 200:
              return await ctx.send('Failed to download files')
          data = io.BytesIO(await resp.read())
          msg = await ctx.send(embed=embed)
          await ctx.author.send(f"**{name}**",file=discord.File(data, f'{name}.png'))
        
  except Exception as e:
    embed = discord.Embed(title=f"Steal Clothes Files", description=f"Unaviable to steal **{name}**\nThe Shirts/Pant Might be Banned or Invalid ID\nor you don't have Sliver Role", color=0xe91e63)
    msg = await ctx.send(embed=embed)
    
    
@commands.has_role(checkperm)  
@bot.command() 
async def checkname(ctx, LetterAmount : int , ranges : int):
  valid = 0
  i = 0
  
  checked = 0
  Chars = string.ascii_letters + string.digits
  AllChars = string.ascii_letters + "_" + string.digits
  embed = discord.Embed(title=f"Name Check {LetterAmount} Letter", description=f"Status : Working\nCheck : {checked}\nValid : {valid}", color=0xe91e63)
  msg = await ctx.reply(embed=embed)
  for i in range(0 ,ranges):
    checked += 1
    FoundUsernames = ""
    Username = ""




    for i in range(0, int(LetterAmount)):
        if i != 0 and i != int(LetterAmount):
            Username = Username + random.choice(Chars)
        else:
            Username = Username + random.choice(Chars)

            
    dembed = discord.Embed(title=f"EzPlus Name Check {LetterAmount} Letter", description=f"Status : Working\nCheck : {checked}\nValid : {valid}\nUsername : {str(Username)}", color=0xe91e63)
    Payload = {
        "request.birthday": "08/09/2005",
        "request.context": "Unknown",
        "request.username": Username
    }
    RequestUrl = "https://auth.roblox.com/v1/usernames/validate"
    GetRequest = requests.get("https://auth.roblox.com/v1/usernames/validate", params = Payload)
    JsonResponse = GetRequest.json()

        
    if JsonResponse["message"] != "Username is already in use" and JsonResponse["message"] != "Username not appropriate for Roblox" and JsonResponse["message"] != "Usernames can be 3 to 20 characters long":
      if not Username in FoundUsernames:
        embed = discord.Embed(title=f"EzPlus Name Checker \nChecked : {checked}   Valid : {valid}", description=f"{Username}", color=0x1abc9c)
        await ctx.author.send(embed=embed)
        valid += 1
  vembed = discord.Embed(title=f"EzPlus Name Check {LetterAmount} Letter", description=f"Status : Done\nCheck : {checked}\nValid  : {valid}", color=0x2ecc71)
  await msg.edit(embed=vembed)


Token = config['bottoken']
try:
    bot.run(Token)
except:
    print("Token Error")
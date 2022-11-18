import discord
import importlib.resources
import json
from secord_modules import searchsploit
from secord_modules import scan_port
from secord_modules import check_ssl
from secord_modules import fetch_webpage

token = "OTI2Nzk5MjQ5ODUxNjk5MjIw.YdA7EA.minxADwzFmz6D382Swr420h6KDE"
client = discord.Client()

domains = {".com", ".net", ".edu", ".tr", ".org", ".int"}


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


# with importlib.resources.open_text("seccord", "config.json") as file: !keep for debug purposes! 
#     data = json.load(file)  
#     token = data['token'] 


@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    if message.content.startswith('!invite'):
        await message.channel.send('get secord for your server! https://discord.com/oauth2/authorize?client_id=926799249851699220&permissions=52224&scope=applications.commands%20bot')

    if  message.content.startswith('!exploit'): 
        response_init = message.content
        link = response_init.split(" ")[1]
        if("https" in link or "http" in link):
            response = searchsploit(link)
            embedVar = discord.Embed(title="Possible exploits for " + link, description="** please refer to exploit-db.com for more details **", color=0x00ff10)
            count = 1
            for x in response:
                embedVar.add_field(name="Exploit " + str(count), value=x[1], inline=False)
                count = count + 1
            await message.channel.send(embed=embedVar)
        else:
            if (check_ssl(link) != "err"):
                await message.channel.send("ssl certificate is not defined in " + link + " initating pyopenssl module for further investigation!")
                embedVar0 = discord.Embed(title="SSL certificate check for " + link, description="** certificate instance is obtained <:tada:933051057993568267> certificate chain is valid **", color=0x00ff10)
                embedVar0.add_field(name="certificate chain: ", value=check_ssl(link), inline=False)
                await message.channel.send(embed=embedVar0)
                str_bldr = "!exploit " + "http://" + link; 
                await message.channel.send(str_bldr)
            else:
                print("error")    

    
    if  message.content.startswith('!portscan'): 
        response_init = message.content
        link = response_init.split(" ")[1]
        response = scan_port(link)
        embedVar = discord.Embed(title="Scanned " + link + " for open ports", description="", color=0x00ff10)
        embedVar.add_field(name="Results: ", value=response, inline=False)
        await message.channel.send(embed=embedVar)    

    if  message.content.startswith('!html'): 
        response_init = message.content
        link = response_init.split(" ")[1]
        channelID = message.channel.id   
        channel = client.get_channel(channelID)
        if("https" in link or "http" in link):
            if(fetch_webpage(link) != "error"):
                await channel.send(file=discord.File("fetched_html.txt"))   
        else:
            new_link = "http://" + link
            if(fetch_webpage(new_link) != "error"):
                await channel.send(file=discord.File("fetched_html.txt"))
            else: 
                await message.channel.send("unvalid url, include http/https and/or try again")

    for x in domains:
        if x in message.content and ("!exploit" not in message.content) and ("!portscan" not in message.content) and ("!html" not in message.content) and ("secord" not in message.content) :
            await message.channel.send("@all - Please analyze links before opening them!")



client.run(token)

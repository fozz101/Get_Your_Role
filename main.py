import discord
import os
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents,command_prefix = '-')
client.remove_command("help")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="my master Fozz"))


@client.event
async def on_reaction_add(reaction, user):
  ChID = 878003089343410207
  guild_id=872576813661061160
  guild= client.get_guild(guild_id)
  if reaction.message.channel.id != ChID:
    return
  if user.id != 877920117827190784:
    if reaction.emoji == "💤":
      roleSB = discord.utils.get(guild.roles, name="Bureau")
      await user.add_roles(roleSB)
    elif reaction.emoji == "😴":
      roleSB = discord.utils.get(guild.roles, name="Member")
      await user.add_roles(roleSB)
    elif reaction.emoji == "🧡":
      roleCS = discord.utils.get(guild.roles, name="CS Bureau")
      await user.add_roles(roleCS)
    elif reaction.emoji == "💛":
      roleCS = discord.utils.get(guild.roles, name="CS Member")
      await user.add_roles(roleCS)
    elif  reaction.emoji == "💘":
      roleWIE = discord.utils.get(guild.roles, name="WIE Bureau")
      await user.add_roles(roleWIE)
    elif reaction.emoji == "💖":
      roleWIE = discord.utils.get(guild.roles, name="WIE Member")
      await user.add_roles(roleWIE)
    elif  reaction.emoji == "💚":
      roleIAS = discord.utils.get(guild.roles, name="IAS Bureau")
      await user.add_roles(roleIAS)
    elif reaction.emoji == "💙":
      roleIAS = discord.utils.get(guild.roles, name="IAS member")
      await user.add_roles(roleIAS)
    elif  reaction.emoji == "🖤":
      roleSIGHT = discord.utils.get(guild.roles, name="SIGHT Bureau")
      await user.add_roles(roleSIGHT)
    elif reaction.emoji == "🤍":
      roleSIGHT = discord.utils.get(guild.roles, name="SIGHT member")
      await user.add_roles(roleSIGHT)
    elif  reaction.emoji == "❤":
      rolePES = discord.utils.get(guild.roles, name="PES Bureau")
      await user.add_roles(rolePES)
    elif reaction.emoji == "💓":
      rolePES = discord.utils.get(guild.roles, name="PES member")
      await user.add_roles(rolePES)
    elif  reaction.emoji == "💜":
      roleRAS = discord.utils.get(guild.roles, name="RAS Bureau")
      await user.add_roles(roleRAS)
    elif reaction.emoji == "🤎":
      roleRAS = discord.utils.get(guild.roles, name="RAS Member")
      await user.add_roles(roleRAS)



@client.event
async def on_reaction_remove(reaction, user):
  ChID = 878003089343410207
  guild_id=872576813661061160
  guild= client.get_guild(guild_id)
  if reaction.message.channel.id != ChID:
    return
  if user.id != 877920117827190784:
    if reaction.emoji == "💤":
      roleSB = discord.utils.get(guild.roles, name="Bureau")
      await user.remove_roles(roleSB)
    elif reaction.emoji == "😴":
      roleSB = discord.utils.get(guild.roles, name="Member")
      await user.remove_roles(roleSB)
    elif reaction.emoji == "🧡":
      roleCS = discord.utils.get(guild.roles, name="CS Bureau")
      await user.remove_roles(roleCS)
    elif reaction.emoji == "💛":
      roleCS = discord.utils.get(guild.roles, name="CS Member")
      await user.remove_roles(roleCS)
    elif  reaction.emoji == "💘":
      roleWIE = discord.utils.get(guild.roles, name="WIE Bureau")
      await user.remove_roles(roleWIE)
    elif reaction.emoji == "💖":
      roleWIE = discord.utils.get(guild.roles, name="WIE Member")
      await user.remove_roles(roleWIE)
    elif  reaction.emoji == "💚":
      roleIAS = discord.utils.get(guild.roles, name="IAS Bureau")
      await user.remove_roles(roleIAS)
    elif reaction.emoji == "💙":
      roleIAS = discord.utils.get(guild.roles, name="IAS member")
      await user.remove_roles(roleIAS)
    elif  reaction.emoji == "🖤":
      roleSIGHT = discord.utils.get(guild.roles, name="SIGHT Bureau")
      await user.remove_roles(roleSIGHT)
    elif reaction.emoji == "🤍":
      roleSIGHT = discord.utils.get(guild.roles, name="SIGHT member")
      await user.remove_roles(roleSIGHT)
    elif  reaction.emoji == "❤":
      rolePES = discord.utils.get(guild.roles, name="PES Bureau")
      await user.remove_roles(rolePES)
    elif reaction.emoji == "💓":
      rolePES = discord.utils.get(guild.roles, name="PES member")
      await user.remove_roles(rolePES)
    elif  reaction.emoji == "💜":
      roleRAS = discord.utils.get(guild.roles, name="RAS Bureau")
      await user.remove_roles(roleRAS)
    elif reaction.emoji == "🤎":
      roleRAS = discord.utils.get(guild.roles, name="RAS Member")
      await user.remove_roles(roleRAS)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  
  await client.process_commands(message)


@client.command()
async def role(ctx):
    channel = ctx.message.channel
    if ctx.channel.id == 878003089343410207:
      messages = await ctx.history(limit=100).flatten()
      await channel.delete_messages(messages)
      embedSB = discord.Embed(
        title= "SB 🤔?",
        colour= discord.Colour.orange()
      )
      embedCS = discord.Embed(
        title= "CS 🤔?",
        colour= discord.Colour.orange()
      )
      embedWIE = discord.Embed(
        title= "WIE 🤔?",
        colour= discord.Colour.orange()
      )
      embedIAS = discord.Embed(
        title= "IAS 🤔?",
        colour= discord.Colour.orange()
      )
      embedRAS = discord.Embed(
        title= "RAS 🤔?",
        colour= discord.Colour.orange()
      )
      embedSIGHT = discord.Embed(
        title= "SIGHT 🤔?",
        colour= discord.Colour.orange()
      )
      embedPES = discord.Embed(
        title= "PES 🤔?",
        colour= discord.Colour.orange()
      )


      used_emojiSB=["💤","😴"]
      used_emojiCS=["🧡","💛"]
      used_emojiWIE=["💘","💖"]
      used_emojiIAS=["💚","💙"]
      used_emojiSIGHT=["🖤","🤍"]
      used_emojiPES=["❤","💓"]
      used_emojiRAS=["💜","🤎"]
      embedSB.add_field(name=f"💤\t SB ExCom",value="\u200b" ,inline=True)
      embedSB.add_field(name=f"😴\t SB Member",value="\u200b" ,inline=True)

      embedCS.add_field(name=f"🧡\t CS ExCom",value="\u200b" ,inline=True)
      embedCS.add_field(name=f"💛\t CS Member",value="\u200b" ,inline=True)

      embedWIE.add_field(name=f"💘\t WIE ExCom",value="\u200b" ,inline=True)
      embedWIE.add_field(name=f"💖\t WIE Member",value="\u200b" ,inline=True)

      embedIAS.add_field(name=f"💚\t IAS ExCom",value="\u200b" ,inline=True)
      embedIAS.add_field(name=f"💙\t IAS Member",value="\u200b" ,inline=True)

      embedSIGHT.add_field(name=f"🖤\t SIGHT ExCom",value="\u200b" ,inline=True)
      embedSIGHT.add_field(name=f"🤍\t SIGHT Member",value="\u200b" ,inline=True)

      embedPES.add_field(name=f"❤\t PES ExCom",value="\u200b" ,inline=True)
      embedPES.add_field(name=f"💓\t PES Member",value="\u200b" ,inline=True)

      embedRAS.add_field(name=f"💜\t RAS ExCom",value="\u200b" ,inline=True)
      embedRAS.add_field(name=f"🤎\t RAS Member",value="\u200b" ,inline=True)

      

      messageSB = await ctx.send(embed=embedSB)
      for emoji in used_emojiSB:
        await messageSB.add_reaction(emoji)
      
      messageCS = await ctx.send(embed=embedCS)
      for emoji in used_emojiCS:
        await messageCS.add_reaction(emoji)

      messageWIE = await ctx.send(embed=embedWIE)
      for emoji in used_emojiWIE:
        await messageWIE.add_reaction(emoji)

      messageIAS = await ctx.send(embed=embedIAS)
      for emoji in used_emojiIAS:
        await messageIAS.add_reaction(emoji)

      messageSIGHT = await ctx.send(embed=embedSIGHT)
      for emoji in used_emojiSIGHT:
        await messageSIGHT.add_reaction(emoji)

      messagePES = await ctx.send(embed=embedPES)
      for emoji in used_emojiPES:
        await messagePES.add_reaction(emoji)
      
      messageRAS = await ctx.send(embed=embedRAS)
      for emoji in used_emojiRAS:
        await messageRAS.add_reaction(emoji)

      await ctx.send("**DISCLAIMER1:** a5tar el bureau mte3ek\n")
      await ctx.send("**DISCLAIMER2:** fi ay la7dha el server eli mhosti 3lih el bot inajem irestarti => ekteb **-role** wa5tar el bureau mte3ek\n")
      await ctx.send("**DISCLAIMER3:** fi ay la7dha talga el bot offline :v , leya wlik rabi contacti el admin bech ya3tik el role wella stena nechla9 eli el server ta7 bech nraj3a\n")
      await ctx.send("**DISCLAIMER4:** mataba3 klem **DISCLAIMER1** ken matkoun met2aked eli el role matzadlekch\n")
    else:
      await ctx.send("Mech lahna !")
      messages = await channel.history(limit=3).flatten()
      await asyncio.sleep(2)
      await channel.delete_messages(messages)





keep_alive()
client.run(os.environ['TOKEN'])
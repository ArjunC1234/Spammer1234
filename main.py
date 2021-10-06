import os
import keep_alive
import discord
import randfacts
import shlex

client = discord.Client()
my_secret = os.environ('Token')


@client.event
async def on_message(message):

  param_list = shlex.split(message.content) 
  del param_list[0]
  print(param_list)

  if len(message.content) >= 2:

    if message.content.startswith("//help") and len(param_list) == 0:

      myEmbed = discord.Embed(title="Need Help With Spammer1234?",description="Spammer1234 is a spam bot that spams people when he wants.", color=0x8FFF00)
      myEmbed.add_field(name="How to use: ", value= "Use '//' as the keyword and add other keywords after, divided with a space, to use commands."), 
      myEmbed.add_field(name="Command List: ", value="//spam 'amount' 'message', //help, //surprise 'mention'(OPTIONAL)"), 
      myEmbed.set_footer(text="Spam for Life.")

      await message.channel.send(embed=myEmbed)
    elif message.content.startswith("//help") and len(param_list) != 0:

      await message.channel.send(f"This command takes 0 arguments and {len(param_list)} were given. Please try again.")
    
    elif message.content.startswith("//spam") and len(param_list) == 2 and int(param_list[0]) <= 20:
      for i in range(int(param_list[0])):
        await message.channel.send(param_list[1])

    elif message.content.startswith("//spam") and len(param_list) != 2 and int(param_list[0]) <= 20:

      await message.channel.send(f"This command takes 2 arguments and {len(param_list)} arguments were given. Please try again.")
    
    elif message.content.startswith("//surprise") and 0 <= len(param_list) <= 1:
      fact = randfacts.get_fact()
      if len(param_list) == 1:
        await message.channel.send(f"{param_list[0]} - {fact}")
      elif len(param_list) == 0:
        await message.channel.send(fact)

    elif message.content.startswith("//surprise") and len(param_list) >= 2 or len(param_list) < 0:

      await message.channel.send(f"This command takes 0 or 1 arguments and {len(param_list)} arguments were given. Please try again.")
    
    elif message.content[0] == "/" and message.content[1] == "/":

      await message.channel.send("Invalid Command.")

keep_alive.keep_alive()
client.run(os.getenv('Token'))

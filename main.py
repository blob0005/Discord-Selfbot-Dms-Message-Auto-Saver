anyerror = False
try:
  import discord
  from discord.ext import commands
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install discord")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Discord Selfbot Dms Auto Saver,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
import json
try:
  json_data = open("settings.json")
  json_data = json.load(json_data)
  token = str(json_data["discord_token"])
  save_diffrent = str(json_data["wanna_save_each_user_in_a_diffrent_txt_file_y_or_n"])
except Exception:
  print('Missing "settings.json" File, It Stores All Settings')
  input("")
  exit()

print("Will Not Work If Any Font In The Message, Name Of Server And Channel Names Cannot Include Fonts")

print("This Will Also Save Message And Content If You Got Pinged In An Server Too")

print("Starting Bot...")
bot = commands.Bot(command_prefix="", self_bot=True)








@bot.event
async def on_ready():
    print(f"{bot.user.name} Is Online")


@bot.event
async def on_message(self):
  if str(self.author.id) == str(bot.user.id):
    pass
  else:
    if str(self.content) == "":
      pass
    else:
      try:
        content = self.content
        id = self.author.id
        name = self.author.name
        n1 = "Discord Name: " + str(name)
        n2 = "Discord Id: " + str(id)
        n3 = "Message Content: " + str(content)
        print("--------")
        print(n1)
        print(n2)
        print(n3)
        
        if save_diffrent == "n":
          file = open("discord_dms_save.txt", "a")
        if save_diffrent == "y":
          file = open(f"discord_dms_save_{str(id)}.txt", "a")
        file.write(str(n1))
        file.write("\n")
        file.write(str(n2))
        file.write("\n")
        file.write(str(n3))
        file.write("\n")
        file.write("--------")
        file.write("\n")
        file.close()
      except:
        print("Message/Username Includes Some Type Of Font")





bot.run(token, bot=False)

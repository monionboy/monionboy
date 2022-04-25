"""
main.py

Created by monion#9370 on 6/16/21.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""
import discord
import os
from discord import app_commands
from keep_alive import keep_alive

my_secret = os.environ['Token']


class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await client.change_presence(self,
                                     activity=discord.Activity(
                                         type=discord.ActivityType.listening,
                                         name='lords talk about heroes!'))
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print('We have logged in as {0.user}')


bot = client()
tree = app_commands.CommandTree(bot)


@tree.command(name="astrid", description="Let me help lord!")
async def slash(interaction: discord.Interaction, lords_command: str):

    #--------base-----------

    if lords_command == "intro":
        await interaction.response.send_message(
            f"Im the Astrid build helper bot, its nice to meet you lord!",
            ephemeral=False)

    if lords_command == "help":
        await interaction.response.send_message(
            f"intro - gives the intro prompt. \n\nhero - displays all current shortcuts for characters also putting the first letter of the element -d,e,f,l,w- in front of the shortcut will display the build i will recommend -ex. fastrid displays fire astrid- \n\ninfo - brings up the info command talking about the developer. \n\nhelp - literally the command you just used....",
            ephemeral=False)

    if lords_command == "info":
        await interaction.response.send_message(
            f"The creator of the bot is monion#9370. \n\nHe built the bot so the officers could be lazy and not have to search for builds from discord messages. \n\nAstrids home server is NewZeiLand. if she is on other server it means the server owner liked her enough to add to the server you are seeing her on. \n\n special credit to Mahi#1691 for helping with the builds",
            ephemeral=False)

    if lords_command == "hero":
        await interaction.response.send_message(
            f"alev -Alev \naslan -Aslan \nastrid -Astrid \nbar -Baretta \nbianca -Bianca \nchar -Charlotte \ndhura -Dhurahan  \nfram -Fram \nhelga -Helga \njohan -Johan \njosh -Joshua  \nkrom -Krom \nlai -Lairei \nlaph -Laphlaes \nluci -Luccilicca \nlum -Lumie \nlyn -Lyn \nmei -Mei Ling \nmik -Mikhail \n9 -Nine \noliv -Olivia \nrash -Rashad \nrosa -Rosanna \npup -Scheider \nsol -Solphi \nvan -Vanessa \nwalt -walther \nzai -Zaira",
            ephemeral=False)

#-------Alev-------
    if lords_command == "dalev":
        await interaction.response.send_message(
            f"Dark Alev is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ealev":
        await interaction.response.send_message(
            f"Earth Alev \n\nBeginner 3 health, 2 defense and 1 speed \nAdvanced 4 health, 1 defense and 1 speed \nAlternate -3 to 4- health, -1 to 0- defense and 2 speed",
            ephemeral=False)

    if lords_command == "falev":
        await interaction.response.send_message(
            f"Fire Alev \n\n3 atttack, 1 defense and 2 crit damage \n-4 attack in certain situations-",
            ephemeral=False)

    if lords_command == "lalev":
        await interaction.response.send_message(
            f"Light Alev \n\n2 health, 2 defense and 2 speed", ephemeral=False)

    if lords_command == "walev":
        await interaction.response.send_message(
            f"Water Alev \n\n3 atttack, 1 defense and 2 crit damage \n-4 attack in certain situations-",
            ephemeral=False)

#-------Aslan-------
    if lords_command == "daslan":
        await interaction.response.send_message(
            f"Dark Aslan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "easlan":
        await interaction.response.send_message(
            f"Earth Aslan \n\n2 health, 2 defense and 2 speed -as much speed and resistance subs as possible-",
            ephemeral=False)

    if lords_command == "faslan":
        await interaction.response.send_message(
            f"Fire Aslan \n\n2 health, 2 defense and 2 speed -as much speed and resistance subs as possible-",
            ephemeral=False)

    if lords_command == "laslan":
        await interaction.response.send_message(
            f"Light Aslan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "waslan":
        await interaction.response.send_message(
            f"Water Aslan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Astrid-------
    if lords_command == "dastrid":
        await interaction.response.send_message(
            f"Dark Astrid \n\n3 attack, 1 defense and 2 crit damage -4 atk in light raid with enemy damage debuffers-",
            ephemeral=False)

    if lords_command == "eastrid":
        await interaction.response.send_message(
            f"Earth Astrid \n\nSupport 2 health, 2 defense and 2 speed \nDps 3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "fastrid":
        await interaction.response.send_message(
            f"Fire Astrid \n\nBeginner 2 attack, 1 health, 1 defense, 1 speed and 1 crit damage \nAdvanced 3 attack, 1 defense, 1 speed and 1 crit dmg \n-monions build when ran with wvan- 4 attack, 1 speed and 1 crit damage",
            ephemeral=False)

    if lords_command == "lastrid":
        await interaction.response.send_message(
            f"Light Astrid is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wastrid":
        await interaction.response.send_message(
            f"Water Astrid \n\n-1 to 3- health, -3 to 1- defense and 2 speed -debuff rate subs recommended-",
            ephemeral=False)

#-------Baretta-------
    if lords_command == "dbar":
        await interaction.response.send_message(
            f"Dark Baretta is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ebar":
        await interaction.response.send_message(
            f"Earth Baretta is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fbar":
        await interaction.response.send_message(
            f"Fire Baretta \n\n3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "lbar":
        await interaction.response.send_message(
            f"Light Baretta is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wbar":
        await interaction.response.send_message(
            f"Water Baretta \n\nUsual 2 attack, 2 health, 1 defense and 1 speed \nDps cleric 3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

#-------Bianca-------
    if lords_command == "dbianca":
        await interaction.response.send_message(
            f"Dark Bianca is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ebianca":
        await interaction.response.send_message(
            f"Earth Bianca is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fbianca":
        await interaction.response.send_message(
            f"Fire Bianca is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "lbianca":
        await interaction.response.send_message(
            f"Light Bianca is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wbianca":
        await interaction.response.send_message(
            f"Water Bianca \n\n-3 to 4- health, 1 defens and, -2 to 1- speed -as long as the build has +90 speed-",
            ephemeral=False)

#-------Charlotte-------
    if lords_command == "dchar":
        await interaction.response.send_message(
            f"Dark Charlotte \n\n3 attack, 1 defense and 2 speed -debuff and speed subs-",
            ephemeral=False)

    if lords_command == "echar":
        await interaction.response.send_message(
            f"Earth Charlotte \n\nUsual -3 to 5- health, -2 to 0- defense and 1 speed -speed subs- \n-Alternate- 4 health and 2 speed -defense subs-",
            ephemeral=False)

    if lords_command == "fchar":
        await interaction.response.send_message(
            f"Fire Charlotte is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "lchar":
        await interaction.response.send_message(
            f"Light Charlotte is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wchar":
        await interaction.response.send_message(
            f"Water Charlotte \n\n1 attack, -1 to 2- health, -3 to 2- defense and 1 speed",
            ephemeral=False)

#-------Dhurahan-------
    if lords_command == "ddhura":
        await interaction.response.send_message(
            f"Dark Dhurahan \n\n3 atttack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "edhura":
        await interaction.response.send_message(
            f"Earth Dhurahan \n\n3 atttack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "fdhura":
        await interaction.response.send_message(
            f"Fire Dhurahan \n\n3 atttack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "ldhura":
        await interaction.response.send_message(
            f"Light Dhurahan \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "wdhura":
        await interaction.response.send_message(
            f"Water Dhurahan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Fram-------
    if lords_command == "dfram":
        await interaction.response.send_message(
            f"Dark Fram is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "efram":
        await interaction.response.send_message(
            f"Earth Fram is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ffram":
        await interaction.response.send_message(
            f"Fire Fram \n\n2 health, 2 defense and 2 speed -debuff subs-",
            ephemeral=False)

    if lords_command == "lfram":
        await interaction.response.send_message(
            f"Light Fram \n\n3 Attack, 1 defense and 2 crit damage -4 attack in favorable cases-",
            ephemeral=False)

    if lords_command == "wfram":
        await interaction.response.send_message(
            f"Water Fram \n\nDebuffer 2 health, 2 defense and 2 speed -debuff speed- \nDps 3 attack, 1 defense and 2 crit dmg -4 attack in favorable situations-",
            ephemeral=False)

#-------Helga-------
    if lords_command == "dhelga":
        await interaction.response.send_message(
            f"Dark Helga \n\n3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "ehelga":
        await interaction.response.send_message(
            f"Earth Helga is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fhelga":
        await interaction.response.send_message(
            f"Fire Helga \n\n3 atttack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "lhelga":
        await interaction.response.send_message(
            f"LightHelga is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "whelga":
        await interaction.response.send_message(
            f"Water Helga \n\n3 atttack, 1 defense and 2 crit damage",
            ephemeral=False)

#-------Johan-------
    if lords_command == "djohan":
        await interaction.response.send_message(
            f"Dark Johan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ejohan":
        await interaction.response.send_message(
            f"Earth Johan is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fjohan":
        await interaction.response.send_message(
            f"Fire Johan \n\n3 atttack, 1 defense, 1 speed and 1 crit damage",
            ephemeral=False)

    if lords_command == "ljohan":
        await interaction.response.send_message(
            f"Light Johan \n\n2 attack, 1 health, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "wjohan":
        await interaction.response.send_message(
            f"Water Johan \n\nTank 4 health and 2 speed \nDps 4 health and 2 crit damage",
            ephemeral=False)

#-------Joshua-------
    if lords_command == "djosh":
        await interaction.response.send_message(
            f"Dark Joshua \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "ejosh":
        await interaction.response.send_message(
            f"Earth Joshua is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fjosh":
        await interaction.response.send_message(
            f"Fire Joshua \n\nSub Dps 2 attack, 1 health, 1 defense, 1 speed and 1 crit damage \nDebuffer 1 attack, 1 health, 2 defense, 1 speed and 1 crit damage",
            ephemeral=False)

    if lords_command == "ljosh":
        await interaction.response.send_message(
            f"Light Joshua is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wjosh":
        await interaction.response.send_message(
            f"Water Joshua \n\n2 health, 2 defense and 2 speed -as much speed and resistance subs as possible-",
            ephemeral=False)

#-------Krom-------
    if lords_command == "dkrom":
        await interaction.response.send_message(
            f"Dark Krom \n\n2 attack, 1 health, 1 defense, 1 speed and 1 crit damage",
            ephemeral=False)

    if lords_command == "ekrom":
        await interaction.response.send_message(
            f"Earth Krom is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "fkrom":
        await interaction.response.send_message(
            f"Fire Krom \n\n4 attack and 2 crit damage", ephemeral=False)

    if lords_command == "lkrom":
        await interaction.response.send_message(
            f"Light Krom is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wkrom":
        await interaction.response.send_message(
            f"Water Krom \n\n2 health, 2 defense and 2 speed -as much speed and resistance subs as possible-",
            ephemeral=False)

#-------Lairei-------
    if lords_command == "dlai":
        await interaction.response.send_message(
            f"Dark Lairei is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "elai":
        await interaction.response.send_message(
            f"Earth Lairei \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "flai":
        await interaction.response.send_message(
            f"Fire Lairei \n\nDebuffer 1 health, 3 defense and 2 speed -debuff subs-",
            ephemeral=False)

    if lords_command == "llai":
        await interaction.response.send_message(
            f"Light Lairei \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "wlai":
        await interaction.response.send_message(
            f"Water Lairei is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Laphlaes-------
    if lords_command == "dlaph":
        await interaction.response.send_message(
            f"Dark laphlaes is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "elaph":
        await interaction.response.send_message(
            f"Earth Laphlaes \n\nBeginner 2 attack, 1 health, 1 defense, 1 crit rate and 1 crit damage \n\nAdvanced 3 attack, 1 defense and 2 crit damage -4 attack in certain situations-",
            ephemeral=False)

    if lords_command == "flaph":
        await interaction.response.send_message(
            f"Fire laphlaes \n\n3 health, 2 defense and 1 speed -debuff rate subs-",
            ephemeral=False)

    if lords_command == "llaph":
        await interaction.response.send_message(
            f"Light Laphlaes is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wlaph":
        await interaction.response.send_message(
            f"Water Laphlaes is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Luccilicca-------
    if lords_command == "dluci":
        await interaction.response.send_message(
            f"Dark Luccilicca \n\n2 health, 2 defense and 2 speed -debuff subs-",
            ephemeral=False)

    if lords_command == "eluci":
        await interaction.response.send_message(
            f"Earth Luccilicca \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "fluci":
        await interaction.response.send_message(
            f"Fire Luccilicca \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "lluci":
        await interaction.response.send_message(
            f"Light Luccilicca is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wluci":
        await interaction.response.send_message(
            f"Water Luccilicca \n\n-2 to 3- health, -3 to 2- defense and 1 speed -40+ debuff rate and speed subs-",
            ephemeral=False)

#-------Lumie-------
    if lords_command == "dlum":
        await interaction.response.send_message(
            f"Dark Lumie \n\n4 attack and 2 crit damage", ephemeral=False)

    if lords_command == "elum":
        await interaction.response.send_message(
            f"Earth Lumie \n\n2 health, 3 defense and 1 speed -debuff rate subs-",
            ephemeral=False)

    if lords_command == "flum":
        await interaction.response.send_message(
            f"Fire Lumie \n\nSupport 2 health, 2 defense and 2 speed \n\nDps 3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "llum":
        await interaction.response.send_message(
            f"Light Lumie is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wlum":
        await interaction.response.send_message(
            f"Water Lumie \n\n2 health, 2 defense and 2 speed -debuff subs-",
            ephemeral=False)

#-------Lyn-------
    if lords_command == "dlyn":
        await interaction.response.send_message(
            f"Dark Lyn is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "elyn":
        await interaction.response.send_message(
            f"Earth Lyn \n\n2 health, 2 defense and 2 speed -debuff subs-",
            ephemeral=False)

    if lords_command == "flyn":
        await interaction.response.send_message(
            f"Fire Lyn is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "llyn":
        await interaction.response.send_message(
            f"Light Lyn is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wlyn":
        await interaction.response.send_message(
            f"Water Lyn \n\n2 health, 2 defense and 2 speed \nDps 4 defense and 2 crit damage",
            ephemeral=False)

#-------Mei Ling-------
    if lords_command == "dmei":
        await interaction.response.send_message(
            f"Dark Mei Ling \n\nBeginner 5 health and 1 speed \n\n6 health",
            ephemeral=False)

    if lords_command == "emei":
        await interaction.response.send_message(
            f"Earth Mei Ling \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "fmei":
        await interaction.response.send_message(
            f"Fire Mei Ling \n\n3 health, 2 defense and 1 speed -debuff rate subs-",
            ephemeral=False)

    if lords_command == "lmei":
        await interaction.response.send_message(
            f"Light Mei Ling \n\n2 health, 2 defense, 1 speed and 1 crit rate -2 speed if you can get enough crit rate from subs-",
            ephemeral=False)

    if lords_command == "wmei":
        await interaction.response.send_message(
            f"Water Mei ling is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Mikhail-------
    if lords_command == "dmik":
        await interaction.response.send_message(
            f"Dark Mikhail \n\n2 health, 2 defense and 2 speed \n-Dps build for those who want it 3 attack, 1 defense, 1 speed and 1 crit damage-",
            ephemeral=False)

    if lords_command == "emik":
        await interaction.response.send_message(
            f"Earth Mikhail \n\n3 attacks, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "fmik":
        await interaction.response.send_message(
            f"Fire Mikhail is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "lmik":
        await interaction.response.send_message(
            f"Light Mikhail is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wmik":
        await interaction.response.send_message(
            f"Water Mikhail is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Nine-------
    if lords_command == "d9":
        await interaction.response.send_message(
            f"Dark Nine \n\n-2 to 3- health, -3 to 2- defense and 1 speed -40+ debuff rate and speed subs-",
            ephemeral=False)

    if lords_command == "e9":
        await interaction.response.send_message(
            f"Earth Nine \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "f9":
        await interaction.response.send_message(
            f"Fire Nine \n\n2 health, 2 defense and 2 speed -debuff rate subs-",
            ephemeral=False)

    if lords_command == "l9":
        await interaction.response.send_message(
            f"Light Nine is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "w9":
        await interaction.response.send_message(
            f"Water Nine \n\n-2 to 3- attack, 1 health, 1 defense and -2 to 1- speed",
            ephemeral=False)

#-------Olivia-------
    if lords_command == "doliv":
        await interaction.response.send_message(
            f"Dark Olivia is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "eoliv":
        await interaction.response.send_message(
            f"Earth Olivia \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "foliv":
        await interaction.response.send_message(
            f"Fire Olivia is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "loliv":
        await interaction.response.send_message(
            f"Light Olivia \n\n3 attack, 1 defense and 2 crit damage -4 attack with tanky subs also works-",
            ephemeral=False)

    if lords_command == "woliv":
        await interaction.response.send_message(
            f"Water Olivia \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

#-------Rashad-------
    if lords_command == "drash":
        await interaction.response.send_message(
            f"Dark Rashad is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "erash":
        await interaction.response.send_message(
            f"Earth Rashad is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "frash":
        await interaction.response.send_message(
            f"Fire Rashad \n\n2 health, 2defense and 2 speed", ephemeral=False)

    if lords_command == "lrash":
        await interaction.response.send_message(
            f"Light Rashad is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wrash":
        await interaction.response.send_message(
            f"Water Rashad \n\nTank 2health, 2 defense and 2 speed \nDps 2 attack, 1 health, 1 defense, 2 crit damage \n-Alternate dps- 3 attack, 1 defense with lots of health sub stats",
            ephemeral=False)

#-------Rosanna-------
    if lords_command == "drosa":
        await interaction.response.send_message(
            f"Dark Rosanna \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "erosa":
        await interaction.response.send_message(
            f"Earth Rosanna is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "frosa":
        await interaction.response.send_message(
            f"Fire Rosanna \n\n3 attack, 1 defense and 2 speed",
            ephemeral=False)

    if lords_command == "lrosa":
        await interaction.response.send_message(
            f"Light Rosanna is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wrosa":
        await interaction.response.send_message(
            f"Water Rosanna is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

#-------Scheider-------
    if lords_command == "dpup":
        await interaction.response.send_message(
            f"Dark Schneider \n\n3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "epup":
        await interaction.response.send_message(
            f"Earth Schneider \n\n2 health, 3 defense and 1 speed",
            ephemeral=False)

    if lords_command == "fpup":
        await interaction.response.send_message(
            f"Fire Schneider \n\n3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "lpup":
        await interaction.response.send_message(
            f"Light Schneider is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "wpup":
        await interaction.response.send_message(
            f"Water Schneider \n\n3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

#-------Solphi-------
    if lords_command == "dsol":
        await interaction.response.send_message(
            f"Dark Solphi \n\nBeginner 2 attack, 1 health, 1 defense, 1 speed and 1 crit damage \nAdvanced 3 attack, 1 defense, 1 speed and 1 crit damage",
            ephemeral=False)

    if lords_command == "esol":
        await interaction.response.send_message(
            f"Earth Solphi \n\n2 health, 2 defense and 2 speed -debuff rate subs-",
            ephemeral=False)

    if lords_command == "fsol":
        await interaction.response.send_message(
            f"Fire Solphi is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "lsol":
        await interaction.response.send_message(
            f"Light Solphi \n\nBeginner 2 attack, 1 health, 1 defense, 1 crit rate and 1 crit damage \nAdvanced 3 attack, 1 defense and 2 crit damage",
            ephemeral=False)

    if lords_command == "wsol":
        await interaction.response.send_message(
            f"Water Solphi \n\n2 health, 2 defense 2 speed -debuff subs-",
            ephemeral=False)

#-------Vanessa-------
    if lords_command == "dvan":
        await interaction.response.send_message(
            f"Dark Vanessa is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "evan":
        await interaction.response.send_message(
            f"Earth Vanessa \n\n4 defense and 2 crit damage", ephemeral=False)

    if lords_command == "fvan":
        await interaction.response.send_message(
            f"Fire Vanessa \n\n3 health, 2 defense and 1 speed",
            ephemeral=False)

    if lords_command == "lvan":
        await interaction.response.send_message(
            f"Light Vanessa \n\n2 health, 2 defense and 2 speed",
            ephemeral=False)

    if lords_command == "wvan":
        await interaction.response.send_message(
            f"Water Vanessa \n\nBeginner 1 attack, 2 health, 2 defense and 1 speed \nAdvanced 2 health, 3 defense and 1 speed \n-monions speed striker support build- 1 health, 3 defense and 2 speed with speed and resistance subs",
            ephemeral=False)

#-------walther-------
    if lords_command == "dwalt":
        await interaction.response.send_message(
            f"Dark Walther is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ewalt":
        await interaction.response.send_message(
            f"Earth Walther \n\n2 health, -2 to 3- defense, 1 speed and -0 to 1- debuff rate",
            ephemeral=False)

    if lords_command == "fwalt":
        await interaction.response.send_message(
            f"Fire Walther is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "lwalt":
        await interaction.response.send_message(
            f"Light Walther \n\n1 attack, 2 health, 2 defense and 1 crit damage",
            ephemeral=False)

    if lords_command == "wwalt":
        await interaction.response.send_message(
            f"Water Walther \n\nBeginner 2 attack, 1 health, 1 defense, 1 speed and 1 crit damage \nAdvanced 3 attack, 1 defense, 1 speed and 1 crit dmg \n-monions build when ran with wvan- 4 attack, 1 speed and 1 crit damage",
            ephemeral=False)


#-------Zaira-------
    if lords_command == "dzai":
        await interaction.response.send_message(
            f"Dark Zaira is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

    if lords_command == "ezai":
        await interaction.response.send_message(
            f"Earth Zaira \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations- \nDebuffer 1 health, 3 defense and 2 speed -debuff subs-",
            ephemeral=False)

    if lords_command == "fzai":
        await interaction.response.send_message(
            f"Fire Zaira \n\n3 attack, 1 defense and 2 crit damage -debuff subs-",
            ephemeral=False)

    if lords_command == "lzai":
        await interaction.response.send_message(
            f"Light Zaira \n\n3 attack, 1 defense and 2 crit damage -4 attack in favorable situations-",
            ephemeral=False)

    if lords_command == "wzai":
        await interaction.response.send_message(
            f"Water Zaira is currently not playable in the game yet, sorry Lord!",
            ephemeral=False)

keep_alive()
bot.run(my_secret)

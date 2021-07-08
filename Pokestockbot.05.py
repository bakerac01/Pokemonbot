#       Version Log 
#   .01 = start
#   .02 added best buy chilling reign outputs
#   .03 added pokemoncenter / gamestop SF
#   .04 added best buy sf
#   .05 added target SF and gamestop evolving sky preorders
# 
# 
#  TO - DO
# Fix timestamp on embed
# have bot auto assign roles
# set up subscription payments
# automate role selection thing
# 
# 
# 
# 
# 
# 
# 
# 
# 
from collections import namedtuple
from time import time
from typing import Text

import discord
from discord import role
from discord import message
import discord_webhook
import requests
from discord import Embed, channel
from discord.colour import Color
from discord_webhook import DiscordEmbed, DiscordWebhook
from requests.models import Response
from discord.ext import commands

client = discord.Client()     #connection to discord


# Formatting for webhook embed (Alerts Channel)




#ready in terminal when bot is online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))    

#@client.event
#async def on_raw_reaction_add(payload):
#    message_id = payload.message_id
#    if message_id == 856899197096951808:
#        guild_id = payload.guild_id
#        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

#        if payload.emoji.name == ':thumbsup:' :
#            role =discord.utils.get(guild.roles, name='Not Subscribed')
#        if role is not None:
#            print(role.name)
            
#@client.event
#async def on_raw_reaction_remove(payload):
#    pass

###################################################################on message to the input channel the webhook is triggered.#######################################
@client.event        
async def on_message(message):
    
    if message.channel.id == 855948044070420540:
        channel = client.get_channel(855551324003368972)
        embed=discord.Embed(title="Darkness Ablaze Booster Pack", url="https://bakerbreaks.com/products/1x-darkness-ablaze-booster-pack?variant=37658375258269", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://cdn.shopify.com/s/files/1/0527/5900/3293/products/image_322a4da6-4058-4e69-8abc-75e048c34cb1_1024x1024.png?v=1611233553")
        embed.add_field(name="Website", value="Bakerbreaks.com", inline=True)
        embed.add_field(name="Price", value="$7.00", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

##############################################################################^^^^This Works | Test Channels ^^^^################################################################################
    #cr_packs_pokemon_center
    if message.channel.id == 856317024661012480:
        channel = client.get_channel(856321780116750351)
        embed=discord.Embed(title="Chilling Reign Packs", url="https://www.pokemoncenter.com/product/177-80847/pokemon-tcg-sword-and-shield-chilling-reign-sleeved-booster-pack-10-cards", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P7036/177-80847/P7036_177-80847_02_thumb.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$3.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    #cr_snorlax_blister_pokemon
    if message.channel.id == 856318567829733416:
        channel = client.get_channel(856321780116750351)
        embed=discord.Embed(title="Chilling Reign Snorlax Blister", url="https://www.pokemoncenter.com/product/699-17093/pokemon-tcg-sword-and-shield-chilling-reign-3-booster-packs-snorlax-promo-card-and-coin", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P7036/699-17093/P7036_699-17093_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$12.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    #cr_eevee_blister_pokemon
    if message.channel.id == 856584385352695809:
        channel = client.get_channel(856321780116750351)
        embed=discord.Embed(title="Chilling Reign Eevee Blister", url="https://www.pokemoncenter.com/product/699-17092/pokemon-tcg-sword-and-shield-chilling-reign-3-booster-packs-eevee-promo-card-and-coin", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P7036/699-17092/P7036_699-17092_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$12.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    #cr_ETB_pokemon_center - ETB ISNT ON POKEMON CENTER 6/21 *NEEDS TO BE ADDED*
    #if message.channel.id == 856319326046126150:
    #    channel = client.get_channel(856321780116750351)
    #    embed=discord.Embed(title="Chilling Reign Eevee Blister", url="https://www.pokemoncenter.com/product/699-17092/pokemon-tcg-sword-and-shield-chilling-reign-3-booster-packs-eevee-promo-card-and-coin", description="Item Restocked!", color=0x1ca625)
    #    embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P7036/699-17092/P7036_699-17092_01.jpg")
    #    embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
    #    embed.add_field(name="Price", value="$12.99", inline=True)
    #    embed.set_footer(text="Bakerbreaks.com Monitors")
    #    embed.timestamp = FIX THIS SOMETIME
        
    #    await channel.send(embed=embed)

    #CR_Booster_box_Monitor
    if message.channel.id == 856319486860853288:
        channel = client.get_channel(856321780116750351)
        embed=discord.Embed(title="Chilling Reign BoosterBox", url="https://www.pokemoncenter.com/product/699-81846/pokemon-tcg-sword-and-shield-chilling-reign-booster-display-box-36-packs", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P7036/699-81846/P7036_699-81846_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$143.64", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    
    #CR_buildandbattle_gamestop
    if message.channel.id == 856601877101805598:
        channel = client.get_channel(856601452574801930)
        embed=discord.Embed(title="Chilling Reign Build and Battle", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield-chilling-reign-build-and-battle-box/11136947.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11136947/Pokemon-Trading-Card-Game-Sword-and-Shield-Chilling-Reign-Build-and-Battle-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$19.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #CR_packs_gamestop
    if message.channel.id == 856601959431143465:
        channel = client.get_channel(856601452574801930)
        embed=discord.Embed(title="Chilling Reign Booster Pack", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield-chilling-reign-booster-pack/11136945.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11136945/Pokemon-Trading-Card-Game-Sword-and-Shield-Chilling-Reign-Booster-Pack?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$3.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    
    #cr_etb_gamestop
    if message.channel.id == 856601986539061283:
        channel = client.get_channel(856601452574801930)
        embed=discord.Embed(title="Chilling Reign ETB", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield-chilling-reign-elite-trainer-box/11136946.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11136946/Pokemon-Trading-Card-Game-Sword-and-Shield-Chilling-Reign-Elite-Trainer-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$39.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)
    
    #cr_packs_bestbuy
    if message.channel.id == 856664996992516176:
        channel = client.get_channel(856664829410017281)
        embed=discord.Embed(title="Chilling Reign Booster Pack", url="https://www.bestbuy.com/site/pokemon-pokemon-tcg-sword-shield-chilling-reign-sleeved-booster/6462769.p?skuId=6462769", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6462/6462769_sd.jpg;maxHeight=640;maxWidth=550")
        embed.add_field(name="Website", value="bestbuy.com", inline=True)
        embed.add_field(name="Price", value="$3.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #cr_etb_bestbuy
    if message.channel.id == 856665073644994580:
        channel = client.get_channel(856664829410017281)
        embed=discord.Embed(title="Chilling Reign ETB", url="https://www.bestbuy.com/site/pokemon-pokemon-tcg-sword-shield-chilling-reign-elite-trainer-box/6462771.p?skuId=6462771", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6462/6462771_sd.jpg;maxHeight=640;maxWidth=550")
        embed.add_field(name="Website", value="bestbuy.com", inline=True)
        embed.add_field(name="Price", value="$39.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Boltund_tin_monitor
    if message.channel.id == 856988717855145984:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Boltund Tin", url="https://www.pokemoncenter.com/product/699-17062/pokemon-tcg-shining-fates-tin-boltund-v", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6954/699-17062/P6954_699-17062_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$29.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Cramorant_tin_monitor
    if message.channel.id == 856990997212561508:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Cramorant Tin", url="https://www.pokemoncenter.com/product/699-17061/pokemon-tcg-shining-fates-tin-cramorant-v", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6954/699-17061/P6954_699-17061_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$29.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Eldegoss_tin_monitor_pokemoncenter
    if message.channel.id == 856991175444660224:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Eldegoss Tin", url="https://www.pokemoncenter.com/product/699-17060/pokemon-tcg-shining-fates-tin-eldegoss-v", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6954/699-17060/P6954_699-17060_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$29.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_MPP_Dedenne_monitor_pokemoncenter
    if message.channel.id == 856994740468973588:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Mad Party Pin Collection (Dedenne)", url="https://www.pokemoncenter.com/product/699-17064/pokemon-tcg-shining-fates-mad-party-pin-collection-dedenne", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6953/699-17064/P6953_699-17064_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_MPP_MrRime_monitor_pokemoncenter
    if message.channel.id == 856994842735411221:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Mad Party Pin Collection (Galarian Mr_Rime)", url="https://www.pokemoncenter.com/product/699-17063/pokemon-tcg-shining-fates-mad-party-pin-collection-galarian-mr-rime", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6953/699-17063/P6953_699-17063_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_MPP_MrRime_monitor_pokemoncenter
    if message.channel.id == 856994935248126012:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Mad Party Pin Collection (Polteageist)", url="https://www.pokemoncenter.com/product/699-17065/pokemon-tcg-shining-fates-mad-party-pin-collection-polteageist", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6953/699-17065/P6953_699-17065_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_MPP_MrRime_monitor_pokemoncenter
    if message.channel.id == 856995025643896942:
        channel = client.get_channel(856990341361172480)
        embed=discord.Embed(title="Shining Fates Mad Party Pin Collection (Bunnelby)", url="https://www.pokemoncenter.com/product/699-17066/pokemon-tcg-shining-fates-mad-party-pin-collection-bunnelby", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.pokemoncenter.com/products/images/P6953/699-17066/P6953_699-17066_01.jpg")
        embed.add_field(name="Website", value="PokemonCenter.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_ETB_monitor_Gamestop
    if message.channel.id == 857000155260780585:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates ETB", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-elite-trainer-box/11112932.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112932/Pokemon-Trading-Card-Game-Shining-Fates-Elite-Trainer-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$49.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_mpp_monitor_Gamestop
    if message.channel.id == 857000228254515240:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates Mad Party Pin Collection", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-mad-party-pin-collection/11112937.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112937/Pokemon-Trading-Card-Game-Shining-Fates-Mad-Party-Pin-Collection?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_v-tin_monitor_Gamestop
    if message.channel.id == 857000324815126568:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates V-tin", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-v-tin/11112935.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112935/Pokemon-Trading-Card-Game-Shining-Fates-V-Tin?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$29.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Premium-collection_monitor_Gamestop
    if message.channel.id == 857000399642296330:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates Premium Collection", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-premium-collection/11112933.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112933/Pokemon-Trading-Card-Game-Shining-Fates-Premium-Collection?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$49.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Minitin_monitor_Gamestop
    if message.channel.id == 857000447038718003:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates Premium Collection", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-mini-tin/11112936.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112936/Pokemon-Trading-Card-Game-Shining-Fates-Mini-Tin?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$8.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pikachu-box_monitor_Gamestop
    if message.channel.id == 857000528139386880:
        channel = client.get_channel(856990475705778227)
        embed=discord.Embed(title="Shining Fates Pikachu Box", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-shining-fates-pikachu-box/11112934.html", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11112934/Pokemon-Trading-Card-Game-Shining-Fates-Pikachu-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price", value="$19.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_ETB_monitor_bestbuy.com
    if message.channel.id == 857370667820515388:
        channel = client.get_channel(856990527920930846)
        embed=discord.Embed(title="Shining Fates ETB", url="https://www.bestbuy.com/site/pokemon-pokemon-tcg-shining-fates-elite-trainer-box-/6445827.p?skuId=6445827", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6445/6445827_sd.jpg;maxHeight=640;maxWidth=550")
        embed.add_field(name="Website", value="Bestbuy.com", inline=True)
        embed.add_field(name="Price", value="$49.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_minitin_monitor_bestbuy.com
    if message.channel.id == 857370798352367636:
        channel = client.get_channel(856990527920930846)
        embed=discord.Embed(title="Shining Fates Mini tin", url="https://www.bestbuy.com/site/pokemon-pokemon-tcg-shining-fates-mini-tin/6445823.p?skuId=6445823", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6445/6445823_sd.jpg;maxHeight=640;maxWidth=550")
        embed.add_field(name="Website", value="Bestbuy.com", inline=True)
        embed.add_field(name="Price", value="$8.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pikachu box_monitor_bestbuy.com
    if message.channel.id == 857370866856493127:
        channel = client.get_channel(856990527920930846)
        embed=discord.Embed(title="Shining Fates Pikachu Box", url="https://www.bestbuy.com/site/pokemon-pokemon-tcg-shining-fates-pikachu-v/6445824.p?skuId=6445824", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://pisces.bbystatic.com/image2/BestBuy_US/images/products/6445/6445824_sd.jpg;maxHeight=640;maxWidth=550")
        embed.add_field(name="Website", value="Bestbuy.com", inline=True)
        embed.add_field(name="Price", value="$19.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pin Collection Polteageist_target.com
    if message.channel.id == 857654404718395422:
        channel = client.get_channel(856990500845387826)
        embed=discord.Embed(title="Shining Fates Pin Collection - Polteageist", url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-polteageist/-/A-82384071#lnk=sametab", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-polteageist/-/A-82384071#")
        embed.add_field(name="Website", value="target.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pin Collection Dedenne_target.com
    if message.channel.id == 857654491825831936:
        channel = client.get_channel(856990500845387826)
        embed=discord.Embed(title="Shining Fates Pin Collection - Dedenne", url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-dedenne/-/A-82384072#lnk=sametab", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-dedenne/-/A-82384072#")
        embed.add_field(name="Website", value="target.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pin Collection Bunnelby_target.com
    if message.channel.id == 857654546775015456:
        channel = client.get_channel(856990500845387826)
        embed=discord.Embed(title="Shining Fates Pin Collection - Bunnelby", url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-8211-bunnelby/-/A-82384064#lnk=sametab", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-8211-bunnelby/-/A-82384064#")
        embed.add_field(name="Website", value="target.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #SF_Pin Collection Mr. Rime_target.com
    if message.channel.id == 857655963943174144:
        channel = client.get_channel(856990500845387826)
        embed=discord.Embed(title="Shining Fates Pin Collection - Mr. Rime", url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-8211-galarian-mr-rime/-/A-82384067#lnk=sametab", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://www.target.com/p/pok-233-mon-trading-card-game-shining-fates-pin-collection-8211-galarian-mr-rime/-/A-82384067#")
        embed.add_field(name="Website", value="target.com", inline=True)
        embed.add_field(name="Price", value="$14.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #ES_Booster Pack_Gamestop
    if message.channel.id == 857736518731169792:
        channel = client.get_channel(857739200836796456)
        embed=discord.Embed(title="Evolving Skies booster(PREORDER Release: 8/27)", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield---evolving-skies-sleeved-booster/11149900.html?condition=New", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11149900/Pokemon-Trading-Card-Game-Sword-and-Shield---Evolving-Skies-Sleeved-Booster?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price(PREORDER)", value="$3.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #ES_ETB_Gamestop
    if message.channel.id == 857736589970767912:
        channel = client.get_channel(857739200836796456)
        embed=discord.Embed(title="Evolving Skies ETB(PREORDER Release: 8/27)", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield---evolving-skies-elite-trainer-box/11149899.html?condition=New", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11149899/Pokemon-Trading-Card-Game-Sword-and-Shield---Evolving-Skies-Elite-Trainer-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price(PREORDER)", value="$39.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #ES_Buildandbattle_Gamestop
    if message.channel.id == 857736665589612554:
        channel = client.get_channel(857739200836796456)
        embed=discord.Embed(title="Evolving Skies Build and battle Stadium (PREORDER Release: 9/10)", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield---evolving-skies-build-and-battle-stadium/11149898.html?condition=New", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11149898/Pokemon-Trading-Card-Game-Sword-and-Shield---Evolving-Skies-Build-and-Battle-Stadium?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price(PREORDER)", value="$59.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #ES_Build and battle_Gamestop
    if message.channel.id == 857736722074959902:
        channel = client.get_channel(857739200836796456)
        embed=discord.Embed(title="Evolving Skies Build and battle (PREORDER Release: 9/10)", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield---evolving-skies-build-and-battle-box/11149901.html?condition=New", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11149901/Pokemon-Trading-Card-Game-Sword-and-Shield---Evolving-Skies-Build-and-Battle-Box?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price(PREORDER)", value="$19.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

    #ES_Blister_Gamestop
    if message.channel.id == 857737904431300618:
        channel = client.get_channel(857739200836796456)
        embed=discord.Embed(title="Evolving Skies blister (PREORDER Release: 8/27)", url="https://www.gamestop.com/toys-collectibles/games-puzzles/trading-card-games/products/pokemon-trading-card-game-sword-and-shield---evolving-skies-three-booster-packs-assortment/11149902.html?condition=New", description="Item Restocked!", color=0x1ca625)
        embed.set_thumbnail(url="https://media.gamestop.com/i/gamestop/11149902/Pokemon-Trading-Card-Game-Sword-and-Shield---Evolving-Skies-Three-Booster-Packs-Assortment?$pdp$")
        embed.add_field(name="Website", value="Gamestop.com", inline=True)
        embed.add_field(name="Price(PREORDER)", value="$12.99", inline=True)
        embed.set_footer(text="Bakerbreaks.com Monitors")
        #embed.timestamp = FIX THIS SOMETIME
        
        await channel.send(embed=embed)

client.run('ODU1OTEyMjk2NTkyMDQ4MTU4.YM5YcQ.NiTnY-veod8cUPtci21xvMcFyjE')


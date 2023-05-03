import discord
from discord.ext import commands
import subprocess

from config import listening_channel, execute_user, commentaire, TOKEN

# Création des intents permettant la lecture des messages
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(intents=intents)

# Au lancement
@bot.event
async def on_ready():
    print(f"Et hop je suis en ligne {bot.user}")


# A chaque message envoyé
@bot.event
async def on_message(message):
    if message.channel.id == listening_channel and message.author.id == execute_user:
        if message.content:
            content = message.content


            # Savoir si c'est un commentaire :
            debut_msg = content[:int(len(commentaire))]
            if debut_msg == commentaire:
                return

            # Définition du channel d'envoi
            channel = bot.get_channel(listening_channel)

            print("Exécution de : " + content)  

            try:
            # Exécution de la commande
                output = subprocess.check_output(content, shell=True, text=True, stderr=subprocess.STDOUT, encoding='cp1252')
            except subprocess.CalledProcessError as e:
            # En cas d'erreur, récupération de la sortie d'erreur
                output = e.output + "\n(Il s'agit d'une erreur d'excution, de commande, ou de synthaxe)"
                    

            # Récupérer la taille pour savoir si il faut le divisier
            taille = len(output)
            if taille <= 1900:
                await channel.send("```\n" + output + "```")
            else:
                while taille > 0:
                    partie = output[:1900].strip()
                    output = output[1900:]

                    if partie:
                        # Envoyer chaque partie en tant que message distinct
                        await channel.send("```\n" + partie + "```")
        else:
            print("Le message ne contient pas de contenu texte.")



bot.run(TOKEN)

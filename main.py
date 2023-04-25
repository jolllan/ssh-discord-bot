import discord
import subprocess

client = discord.Client()

CHANNEL_ID = 123456789 # Remplacez ce nombre par l'ID du canal où vous souhaitez que votre bot écoute

@client.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID:
        try:
            result = subprocess.check_output(message.content, shell=True, stderr=subprocess.STDOUT, timeout=10)
            result = result.decode("cp1252", errors="ignore").strip()
            if len(result) > 2000:
                # Si la sortie est trop longue pour Discord, envoyez-la en plusieurs messages
                chunks = [result[i:i+1994] for i in range(0, len(result), 1994)]
                for chunk in chunks:
                    await message.channel.send(f"```\n{chunk}\n```")
            else:
                await message.channel.send(f"```\n{result}\n```")
        except subprocess.CalledProcessError as e:
            await message.channel.send(f"La commande a renvoyé une erreur : ```\n{e.output.decode('cp1252').strip()}\n```")
        except subprocess.TimeoutExpired:
            await message.channel.send("La commande a pris trop de temps à s'exécuter.")

client.run("token")
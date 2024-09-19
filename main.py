import discord
from discord.ext import commands
import pandas as pd
from pytz import timezone
from datetime import datetime
from dotenv import load_dotenv
import os
 

load_dotenv() # Carrega as variáveis de ambiente do arquivo .env

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') # Obtém a token do bot a partir da variável de ambiente


intents = discord.Intents.all()  # Habilita todas as permissões que o bot pode ter (como ler mensagens de canais, acessar a lista de membros
bot = commands.Bot(command_prefix='!', intents=intents) # Cria uma instância do bot que usa o prefixo '!' para os comandos.
 
messages_data = [] # Lista que armazena informações sobre as mensagens coletadas.
 
# Define o fuso horário
saopaulo_tz = timezone('America/Sao_Paulo')
 
@bot.event
async def on_ready():
    try:
        print(f'Logged in as {bot.user.name}')
    
        for guild in bot.guilds:
            print(guild.name)
            
            for channel in guild.text_channels:
                async for message in channel.history(after=datetime.fromisoformat('2024-04-05')):
                
                    messages_data.append({
                        "Message": message.content,
                        "Message Datetime": message.created_at.astimezone(saopaulo_tz),  # Convert to Sao Paulo timezone
                        "User": message.author.name,
                        "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                        "Channel": channel.name,
                        "Thread": "None",
                        "Server Name": guild.name,
                        "Category": channel.category.name if channel.category != None else "None"
                    })
                    
                    
                for thread in channel.threads:
                    async for message in thread.history(after=datetime.fromisoformat('2024-04-05')):
                  
                        messages_data.append({
                            "Message": message.content,
                            "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                            "User": message.author.name,
                            "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                            "Channel": channel.name,
                            "Thread": thread.name,
                            "Server Name": guild.name,
                            "Category": channel.category.name if channel.category != None else "None"
                        })
        
            for forum in guild.forums:
                for thread in forum.threads:
                    async for message in thread.history(after=datetime.fromisoformat('2024-09-18')):
                    
                        messages_data.append({
                            "Message": message.content,
                            "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                            "User": message.author.name,
                            "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                            "Channel": forum.name,
                            "Thread": thread.name,
                            "Server Name": guild.name,
                            "Category": forum.category.name if forum.category != None else "None"
                        })

        #Depois de coletar todas as mensagens, ele as organiza em um pandas.DataFrame e exporta para um arquivo CSV chamado teste.csv
        df = pd.DataFrame(messages_data)
    

        df.sort_values(by="Message Datetime", ascending=False, inplace=True)
    
        
        df.to_csv('teste.csv', sep='§', encoding='utf-8', index=False)
        exit()
    except:
        exit()
 
 
bot.run(DISCORD_TOKEN)

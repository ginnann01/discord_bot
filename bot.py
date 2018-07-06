# -*- coding: utf-8 -*-
import discord
import os
import random
import yaml

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):

    # yamlファイルの読み込み
    with open("dict.yaml", "rb") as f:
        data = yaml.load(f)
    
    passphrases = data["passphrases"]
    volumes = data["volumes"]
    folder = data["folder"]

    
    if message.content == "--usage": #キーワード一覧を表示
        for k in passphrases.keys():
            await client.send_message(message.channel, k)
    
    elif message.content in passphrases:
       if client.user != message.author:
            #対応する発言が複数ある場合はランダムに取り出し
            comment, audio = random.choice(list(passphrases[message.content].items()))

            #チャットに反応
            if len(comment) != 0:
                await client.send_message(message.channel, comment)
            
            #ボイスチャンネルに突撃
            if len(audio) != 0:
                voice_channel = message.author.voice_channel
                voice = await client.join_voice_channel(voice_channel)
                player = voice.create_ffmpeg_player(os.path.join(folder, audio))
                player.volume = volumes[message.content]
                player.start()
                
                #再生終了待ち
                while player.is_playing():
                    pass
    
                for x in client.voice_clients:
                    pass
                await x.disconnect()

#----------------
# トークンの指定
#----------------
token = "{ディスコードからもらったトークン}"
client.run(token)
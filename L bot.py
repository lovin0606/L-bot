import discord
from datetime import datetime
import random
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("L bot")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author.bot:
        return None

    MESS = message.content.split()
    M = MESS[0]

    if M == "/edit":
        role = message.guild.get_role(807238764027576352)
        await role.edit(name=MESS[1])

    if M == "/채금":
        member = message.mentions[0]
        role = message.guild.get_role(772077952279379978)
        await member.add_roles(role)
        await message.channel.send("%s 님의 입을 막았습니다" % member.name)

    if M == "/채금해제":
        member = message.mentions[0]
        role = message.guild.get_role(772077952279379978)
        await member.remove_roles(role)
        await message.channel.send("%s 님이 돌아왔습니다" % member.name)

    if M == "/count":
        guild = message.guild
        Total_member = message.guild.member_count
        User = 0
        Bot = 0
        i = 0
        while not i == Total_member:
            if guild.members[i].bot:
                Bot += 1
                i += 1
            else:
                User += 1
                i += 1
        Tm = guild.get_channel(800699982604533811)
        U = guild.get_channel(805429158091685910)
        B = guild.get_channel(805429217525235732)
        await Tm.edit(name="총 인원: %s" % Total_member)
        await U.edit(name="유저: %s" % User)
        await B.edit(name="봇: %s" % Bot)
        await message.channel.send("counted")

    if message.channel.id == 777582005776285766:
        await message.author.edit(nick=str(message.content))

    if M == "/청소":
        await message.channel.purge(limit=int(MESS[1]) + 1)
        await message.channel.send("청소 %s" % MESS[1])

    if M == "/서버정보":
        guild = message.guild
        random_number = random.randint(0, 16777215)
        hex_number = int(hex(random_number), 16)
        ServerName = guild.name
        created = guild.created_at
        ServerBirthday = created.strftime('%Y-%m-%d %H:%M:%S')
        Total_Members = guild.member_count
        User = 0
        Bot = 0
        i = 0
        while not i == Total_Members:
            if guild.members[i].bot:
                Bot += 1
                i += 1
            else:
                User += 1
                i += 1
        channels = guild.channels
        text_channels = guild.text_channels
        voice_channels = guild.voice_channels
        Total_Channels = len(channels)
        Text_Channels = len(text_channels)
        Voice_Channels = len(voice_channels)
        ServerOwner = guild.owner
        ServerId = guild.id
        AFK_Channel = guild.afk_channel
        ServerIcon = guild.icon_url
        Rules_Channel = guild.rules_channel
        if guild.rules_channel:
            Rules_Channel = guild.rules_channel.mention
        embed = discord.Embed(title="서버 정보", description="이 서버의 정보입니다!", color=hex_number)
        embed.set_thumbnail(url=ServerIcon)
        embed.add_field(name="서버 이름", value=str(ServerName), inline=False)
        embed.add_field(name="서버 생일", value=str(ServerBirthday), inline=False)
        embed.add_field(name="총 인원 수", value=str(Total_Members), inline=False)
        embed.add_field(name="유저 수", value=str(User), inline=False)
        embed.add_field(name="봇 수", value=str(Bot), inline=False)
        embed.add_field(name="총 채널 수", value=str(Total_Channels), inline=False)
        embed.add_field(name="채팅 채널 수", value=str(Text_Channels), inline=False)
        embed.add_field(name="음성 채널 수", value=str(Voice_Channels), inline=False)
        embed.add_field(name="서버 주인", value=ServerOwner, inline=False)
        embed.add_field(name="서버 ID", value=str(ServerId), inline=False)
        embed.add_field(name="AFK 채널", value=AFK_Channel, inline=False)
        embed.add_field(name="규칙 채널", value=Rules_Channel, inline=False)
        await message.channel.send(embed=embed)

BT = os.environ["BT"]
client.run("BT")

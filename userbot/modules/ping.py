# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported by @mrismanaziz
# FROM Man-Userbot
# ReCode by @Pocongonlen

import random
import time
from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot, DEVS
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, poci_cmd

absen = [
    "**Hadir bang daz** 😁",
    "**Hadir kak daz** 😉",
    "**Hadir dong daz** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@poci_cmd(pattern="ping$")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cping$")
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "**ping**")
    await xx.edit("**Ping !!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await xx.edit(
        f"**• Pong**  `%sms`\n"
        f"**• Uptime -** `{uptime}` \n" % (duration)
    )

@poci_cmd(pattern="tping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Pong**")
    await pong.edit("__**•**__")
    await pong.edit("__**••**__")
    await pong.edit("__**•••**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**Pongs ᴘɪɴɢ**\n"
        f"**ᴘɪɴɢ:** "
        f"`%sms` \n"
        f"**ᴏɴʟɪɴᴇ:** "
        f"`{uptime}` \n" % (duration))

#  .Coded by alvin Lord-Userbot


@poci_cmd(pattern="rping$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await ram.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await ram.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await ram.edit("**40% ████▒▒▒▒▒▒**")
    await ram.edit("**60% ██████▒▒▒▒**")
    await ram.edit("**80% ████████▒▒**")
    await ram.edit("**100% ██████████**")
    await ram.edit("✨")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await ram.edit(
        f"**◕ 𝙐𝙍𝙊-𝘽𝙊𝙏 ◕**\n"
        f"** ➠  Sɪɢɴᴀʟ   :** "
        f"`%sms` \n"
        f"** ➠  Uᴘᴛɪᴍᴇ  :** "
        f"`{uptime}` \n"
        f"** ➠  Oᴡɴᴇʀ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )

#  .Coded by Ramadhani RAM-UBOT

@poci_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@poci_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Gass!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🏓 **Ping!**\n`%sms`" % (duration))


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def DAZII(ganteng):
    await ganteng.reply(random.choice(absen))


# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  •  **Syntax :** `{cmd}ping`\
        \n  •  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  •  **Syntax :** `{cmd}pong`\
        \n  •  **Function : **Sama seperti perintah ping\
        \n\n  •  **Syntax :** `{cmd}tping`\
        \n  •  **Function : **Sama seperti perintah ping\
        \n\n  •  **Syntax :** `{cmd}rping`\
        \n  •  **Function : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  •  **Syntax :** `{cmd}speedtest`\
        \n  •  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)

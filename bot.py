# لاین پایین رو پاک کنی یعنی ننتو فرستادی پیشم
# Creator : @TheMrVirus

from telethon import TelegramClient , events
import asyncio , aiocron , pytz , time
from telethon.tl import functions
from datetime import datetime
from random import choice

api_id = 3784395 # آی پی آی آیدی بزارید
api_hash = "585d5d9f5ac26d8ced1f1cb5e2b44420" # آی پی آی هش بزارید
client = TelegramClient('MrVirus' , api_id , api_hash)
client.start()

AdminBot = 1892713280 # آیدی عددی اکانتی که میخاید ران کنید
main = '9876543210'
fonts = ['❾➇➆➅➄➃➂❷❶⓪','➒➑➐➏➎➍➌➋➊⓿','𝟫𝟪𝟩𝟨𝟧𝟦𝟥𝟤𝟣𝟢','𝟡𝟠𝟟𝟞𝟝𝟜𝟛𝟚𝟙𝟘','𝟵𝟴𝟳𝟲𝟱𝟰𝟯𝟮𝟭𝟬','𝟗𝟖𝟕𝟔𝟓𝟒𝟑𝟐𝟏𝟎','９８７６５４３２１０','₉₈₇₆₅₄₃₂₁₀','⁹⁸⁷⁶⁵⁴³²¹⁰','⑨⑧⑦⑥⑤④③②①⓪',]
heart = ['💘','💝','💔','💗','💖','🖤','🤎','💜','💙','💚','💛','🧡','❤','🤍',]
name_list = []
bio_list = []

@client.on(events.NewMessage(pattern=r"AddName (.*)" , from_users=AdminBot))
async def add_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) in name_list:
        await event.edit(f"**Name ( {xxx} ) In Name Listed . . . !**")
    else:
        try:
            name_list.append(xxx)
            await event.edit(f"**Name ( {xxx} ) Aded In List Name . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage(pattern=r"DelName (.*)" , from_users=AdminBot))
async def del_name(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) not in name_list:
        await event.edit(f"**Name ( {xxx} ) Not In Name Listed . . . !**")
    else:
        try:
            name_list.remove(xxx)
            await event.edit(f"**Name ( {xxx} ) Removed In List Name . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage())
async def clean_name(event):
    text = (event.raw_text)
    if (text == "ClearName" and event.sender_id == AdminBot):
        if name_list == []:
            await event.edit("**Name List Has Been Empty . . . !**")
        else:
            name_list.clear()
            await event.edit("**Name List Has Been Cleared . . . !**")

@client.on(events.NewMessage(pattern=r"AddBio (.*)" , from_users=AdminBot))
async def add_bio(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) in bio_list:
        await event.edit(f"**Bio ( {xxx} ) In Bio Listed . . . !**")
    else:
        try:
            bio_list.append(xxx)
            await event.edit(f"**Bio ( {xxx} ) Aded In List Bio . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage(pattern=r"DelBio (.*)" , from_users=AdminBot))
async def del_bio(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    xxx = (input_str)
    if (xxx) not in bio_list:
        await event.edit(f"**Bio ( {xxx} ) Not In Bio Listed . . . !**")
    else:
        try:
            bio_list.remove(xxx)
            await event.edit(f"**Bio ( {xxx} ) Removed In List Bio . . . !**")
        except:
            await event.edit("**No Invalid . . . !**")

@client.on(events.NewMessage())
async def clean_bio(event):
    text = (event.raw_text)
    if (text == "ClearBio" and event.sender_id == AdminBot):
        if bio_list == []:
            await event.edit("**Bio List Has Been Empty . . . !**")
        else:
            bio_list.clear()
            await event.edit("**Bio List Has Been Cleared . . . !**")

@client.on(events.NewMessage())
async def timebio_on(event):
    text = (event.raw_text)
    if (text == "TimeBio On" and event.sender_id == AdminBot):
        if bio_list == []:
            await event.edit("**You Must First Have A Name In The List Of Names . . . !**")
        else:
            await event.edit(f'**Time Bio Is [Actived](tg://user?id={AdminBot}) !**')
            @aiocron.crontab('*/1 * * * *')
            async def clockbio():
                ir=pytz.timezone("Asia/Tehran")
                time=datetime.now(ir).strftime("%H:%M")
                time=time.translate(time.maketrans(main, choice(fonts)))
                await client(functions.account.UpdateProfileRequest(about=f'{choice(heart)} {choice(bio_list)} {time}'))
                clockbio.start()

@client.on(events.NewMessage())
async def timename_on(event):
    text = (event.raw_text)
    if (text == "TimeName On" and event.sender_id == AdminBot):
        if name_list == []:
            await event.edit("**You Must First Have A Name In The List Of Names . . . !**")
        else:
            await event.edit(f'**Time Name Is [Actived](tg://user?id={AdminBot}) !**')
            @aiocron.crontab('*/1 * * * *')
            async def clockname():
                ir=pytz.timezone("Asia/Tehran")
                time=datetime.now(ir).strftime("%H:%M")
                time=time.translate(time.maketrans(main, choice(fonts)))
                await client(functions.account.UpdateProfileRequest(first_name=f'{choice(name_list)} {time} {choice(heart)}'))
                clockname.start()

@client.on(events.NewMessage())
async def timename_off(event):
    text = (event.raw_text)
    if (text == "TimeName Off" and event.sender_id == AdminBot):
        await event.edit(f'**Time Name Is [DeActived](tg://user?id={AdminBot}) !**')
        clockname.stop()

@client.on(events.NewMessage())
async def timebio_off(event):
    text = (event.raw_text)
    if (text == "TimeBio Off" and event.sender_id == AdminBot):
        await event.edit(f'**Time Bio Is [DeActived](tg://user?id={AdminBot}) !**')
        clockbio.stop()

@client.on(events.NewMessage())
async def timebio_on(event):
    text = (event.raw_text)
    if (text == "Help" and event.sender_id == AdminBot):
        await event.edit("**Welcome To Help !\n\nتوجه : \nبرای روشن کردن تایم اسم یا بیوگرافی حتما قبلش یه بیوگرافی یا اسم اضافه کنید به لیست ها !\n\nاضافه کردن اسم : \n`AddName `MrVirus\nاضافه کردن بیو : \n`AddBio `@TheMrVirus\nروشن یا خاموش کردن تایم روی اسم : \n`TimeName On`\n`TimeName Off`\nروشن یا خاموش کردن تایم روی بیوگرافی : \n`TimeBio On`\n`TimeBio Off`\nپاکسازی لیست اسم ها : \n`ClearName`\nپاکسازی لیست بیوگرافی ها : \n`ClearBio`\n\nCr : @TheMrVirus**")

client.run_until_disconnected()
asyncio.get_event_loop().run_forever()

# لاین پایین رو پاک کنی یعنی ننتو فرستادی پیشم
# Creator : @TheMrVirus

import asyncio
from pyrogram.enums import ChatType, ChatMemberStatus
from Sifra import app
from pyrogram import filters
from Sifra.utils.admin_check import admin_filter



SPAM_CHATS = []


@app.on_message(filters.command(["utag", "uall"]) & filters.group & admin_filter)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**◈ 𝚁𝙴𝙿𝙻𝚈 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙷𝙴𝙽 𝚄𝚂𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙾𝚁 𝚆𝚁𝙸𝚃𝙴 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙾𝚁 𝚃𝙰𝙶𝙶𝙸𝙽𝙶 𝙱𝚈 ||𝚂𝙸𝙵𝚁𝙰 ❤️|| ◈**") 
        return                  
    if replied:
       SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 2
            usertxt += f"\n✦ [{m.user.first_name}](tg://user?id={m.user.id})✦ \n"
            if usernum == 6:
                await app.send_message(message.chat.id,f'   ⤜⤜⤜ ||𝚂𝙸𝙵𝚁𝙰 ❤️ 𝙰𝚈𝙰𝙽𝙾|| ⤛⤛⤛\n\n🌔━━━━━━━━━━━━━━━━━━━━━🌔\n\n➜{text}\n\n🌔━━━━━━━━━━━━━━━━━━━━━🌔\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""          
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
       SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 2
            usertxt += f"\n✦ [{m.user.first_name}](tg://user?id={m.user.id})✦ \n"
            if usernum == 6:
                await app.send_message(message.chat.id,f'   ⤜⤜⤜ ||𝚂𝙸𝙵𝚁𝙰 ❤️ 𝙰𝚈𝙰𝙽𝙾|| ⤛⤛⤛\n\n🌔━━━━━━━━━━━━━━━━━━━━━🌔\n\n➜{text}\n\n🌔━━━━━━━━━━━━━━━━━━━━━🌔\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                           
        try :
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           
@app.on_message(filters.command("cancel") & ~filters.private)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try :
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**≕≕ 𝚃𝙰𝙶 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝚂𝚃𝙾𝙿𝙴𝙳 𝙱𝚈 ||𝚂𝙸𝙵𝚁𝙰 ❤️|| ≔≔**")     
                                     
    else :
        await message.reply_text("**◈ 𝙽𝙾 𝙾𝙿𝙴𝚁𝙰𝚃𝙸𝙾𝙽 𝙸𝚂 𝙶𝙾𝙸𝙽𝙶 𝙾𝙽 ||𝚂𝙸𝙵𝚁𝙰 ❤️|| ◈**")  
        return       

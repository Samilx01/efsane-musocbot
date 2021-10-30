from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""<b>👋🏻 Merhaba {message.from_user.first_name}!</b>\n\n**Telegram Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Sizi şaşırtacak pek çok harika özelliğim var!** 🥳 \n\n🔴 **Telegramda Beni nasıl kullanabileceğinizi öğrenmek için lütfen >> /help Butonuna basınız.** \n\n🔴 **Grubunuzun sesli sohbetinde, Müzik çalabilmem için Asistanın Grubunuzda olması gerekir.** \n\n🔵 Bu çalışma [Sohbet Destek](https://t.me/Sohbetdestek) Tarafından keyfe değer düzenlenmiştir.!
      """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekle ➕", url="https://t.me/ProMaxMusic_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Maxmusic_Asistan" 
                    ),
                    InlineKeyboardButton(
                        "💬 Sohbet", url="https://t.me/Sohbetskyfall"
                    ),
                    InlineKeyboardButton(
                        "🙎‍♂️ Geliştirici", url="https://t.me/Mahoaga") 
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Kaynak Kodu", url="https://github.com/Mehmetbaba55/Efsane-Voice2021"
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️YouTube videosu aramak istiyor musunuz? ?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Sohbetskyfall"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Merhaba {message.from_user.first_name}! 
\n/oynat - ᴍᴘ3 ꜰᴏʀᴍᴀᴛɪɴᴀ ᴜʏɢᴜɴ ᴅᴏꜱʏᴀʟᴀʀɪ ᴄᴀʟɪꜱᴛɪʀᴍᴀᴋ ɪᴄɪɴ ᴅᴇᴇꜱᴇʀ ᴍᴜꜱɪᴄ ᴅᴇꜱᴛᴇᴋʟᴇʀ
/bul - ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ꜱᴀʀᴋɪʟᴀʀɪ ʜɪᴢʟɪ ʙɪʀ ꜱᴇᴋɪʟᴅᴇ ɪɴᴅɪʀɪɴ
/dinle - ʏᴏᴜᴛᴜʙᴇ'ᴅᴀɴ ɪꜱᴛᴇᴅɪɢɪɴɪᴢ ᴍᴜᴢɪɢɪ ᴄᴀʟᴀʀ
/id - ꜱᴏʜʙᴇᴛ ɪᴅ ᴠᴇ ᴋᴜʟʟᴀɴɪᴄɪɴɪɴ ɪᴅ'ꜱɪ ʜᴀᴋᴋɪɴᴅᴀ ʙɪʟɢɪ ᴠᴇʀɪʀ
\n*🙋‍♂️ ʏᴀʟɴɪᴢᴄᴀ ʏᴏɴᴇᴛɪᴄɪʟᴇʀ ɪᴄɪɴ*
/durdur - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴀᴋʟᴀᴛᴍᴀ
/devam - ꜱᴀʀᴋɪ ᴄᴀʟᴍᴀʏᴀ ᴅᴇᴠᴀᴍ ᴇᴛ
/atla - ꜱᴏɴʀᴀᴋɪ ꜱᴀʀᴋɪʏɪ ᴄᴀʟ
/son- ᴍᴜᴢɪᴋ ᴄᴀʟᴍᴀʏɪ ᴅᴜʀᴅᴜʀᴍᴀ
/asistan - ᴀꜱɪꜱᴛᴀɴɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴇ ᴅᴀᴠᴇᴛ ᴇᴛᴍᴇ
/asistanby - ᴀꜱɪꜱᴛᴀɴɪɴɪᴢɪ ꜱᴏʜʙᴇᴛɪɴɪᴢᴅᴇɴ ᴄɪᴋᴀʀɪʀ
/volume - Ses ayarını 0-200 arası ayarlar
/ver - Üyenin müzik botunu yönetici gibi kullanması için yetkilendiriniz.
/al - Üyeye vermiş olduğunuz müzik botu yetkisini almak için. 
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👨‍💻 Düzenleyen", url="https://t.me/Sohbetdestek" 
                    )
                ]
            ]
        )
    )    

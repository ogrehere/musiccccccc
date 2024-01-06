# Import necessary modules and functions
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
from io import BytesIO
from VIPMUSIC import app
from pyrogram import filters

async def ping_com(client, message: Message, _):
    gif_url = "https://graph.org/file/76d832bf75bcebd1a4cdd.mp4"
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**"
    response = await app.send_media(gif_url, caption=(captionss))
    
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)

    captions = "**🏓 ᴘɪɴɢ...ᴘᴏɴɢ...ᴘɪɴɢ✨\n🎸 ᴅɪɴɢ...ᴅᴏɴɢ...ᴅɪɴɢ💞**"
    
    await message.reply_photo((carbon), caption=captions,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=_["S_B_5"],
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="✦ ɢʀᴏᴜᴘ ✦", url=f"https://t.me/TG_FRIENDSS",
                    ),
                    InlineKeyboardButton(
                        text="✧ ᴍᴏʀᴇ ✧", url=f"https://t.me/VIP_CREATORS",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
                    )
                ],
            ]
        ),
    )
    
    await response.delete()

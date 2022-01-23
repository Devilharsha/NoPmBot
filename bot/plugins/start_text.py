from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    OWNER_ID,
    START_IMG,
    NAME,
    COMMM_AND_PRE_FIX,
    START_COMMAND
)
from bot.bot import Bot 
from bot.hf.flifi import uszkhvis_chats_ahndler
from pykeyboard import InlineKeyboard
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup

# wants to add your own text read this https://core.telegram.org/bots/api#html-style 
START_TEXT = f"""
──「 <a href="{START_IMG}">{NAME}</a> 」──
<b>Hey Master! ,</b>
<b>I Am Working Properly With Awesome Speed</b>
<b>➖➖➖➖➖➖➖➖➖➖➖➖➖</b>
<code>My Repo Is Public</code> <a href="https://github.com/AASFCYBERKING/NoPmBot">Here</a>
"""

button = InlineKeyboard(row_width=1)
button.add(InlineKeyboardButton(text="Repo", url="t.me/sctbots"), InlineKeyboardButton(text="Owner", url=f"tg://user?id={OWNER_ID}"))

@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    ~uszkhvis_chats_ahndler([OWNER_ID])
)
async def num_start_message(client: Bot, message: Message):
    await message.reply_text(
        client.commandi[START_COMMAND],
        quote=True
    )


@Bot.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    uszkhvis_chats_ahndler([OWNER_ID])
)
async def nimda_start_message(_, message: Message):
    await message.reply_text(
        START_TEXT,
        quote=True,
        reply_markup=button
    )

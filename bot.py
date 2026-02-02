import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import API_ID, API_HASH, BOT_TOKEN, DELETE_DELAY

bot = Client(
    "media_delete_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

MEDIA_TYPES = ["photo", "video", "audio", "document", "animation", "sticker"]

@bot.on_message(filters.group & filters.media)
async def auto_delete_media(client: Client, message: Message):
    print(f"Got media in {message.chat.id} msg={message.id}", flush=True)

    try:
        await asyncio.sleep(int(DELETE_DELAY))
        await message.delete()
        print(f"Deleted msg {message.id}", flush=True)
    except Exception as e:
        print(f"Failed to delete message {message.id}: {e}", flush=True)


@bot.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    me = await bot.get_me()
    await message.reply_photo(
        photo="https://envs.sh/HcV.jpg",
        caption=f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•
┆✦ » ʜᴇʏ {message.from_user.mention}
└──────────────────────•
✦ » ɪ'ᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇ ᴍᴇᴅɪᴀ ɢᴜᴀʀᴅɪᴀɴ ʙᴏᴛ.
✦ » ɪ ᴡɪʟʟ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇᴅɪᴀ ᴍᴇssᴀɢᴇs ᴀғᴛᴇʀ 𝟻 ᴍɪɴᴜᴛᴇs ɪɴ ɢʀᴏᴜᴘ
✦ » ᴄʜᴇᴄᴋ ᴍʏ ᴀʙɪʟɪᴛʏ, ɢɪᴠᴇ ᴍᴇ ᴏɴʟʏ ᴅᴇʟᴇᴛᴇ ᴘᴏᴡᴇʀ ᴀɴᴅ ꜱᴇᴇ ᴍᴀɢɪᴄ ɪɴ ɢʀᴏᴜᴘ.

•──────────────────────•
❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ ➪ [˹ 𝐁ᴏᴛᴢ 𝐄ᴍᴩɪʀᴇ⚡️ ˼](https://t.me/BotzEmpire)
•──────────────────────•""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(
                "✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙",
                url=f"https://t.me/{me.username}?startgroup=true"
            )],
            [
                InlineKeyboardButton("˹ ᴏᴡɴᴇʀ ˼", url="https://t.me/btw_deva"),
                InlineKeyboardButton("˹ υᴘᴅᴀᴛᴇs ˼", url="https://t.me/BotzEmpire")
            ],
            [
                InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/Yaaro_kimehfill"),
                InlineKeyboardButton("˹ ᴍᴜsɪᴄ ʙᴏᴛ ˼", url="https://t.me/DEVA_MUSICBOT")
            ]
        ])
    )

async def main():
    await bot.start()
    print("Bot started", flush=True)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

from os import environ
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, ChatMember, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from PIL import Image, ImageDraw, ImageFont

# Initialize Pyrogram Client
app = Client("my_bot")

# Constants
bg_path = "Sifra/assets/adipic.png"
font_path = "Sifra/assets/Anya.ttf"

# --------------------------------------------------------------------------------- #

# Lambda function to get font
get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)

# --------------------------------------------------------------------------------- #

# Callback function to close messages
@app.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

# --------------------------------------------------------------------------------- #

# Callback function to provide video source
@app.on_callback_query(filters.regex("gib_source"))
async def gib_repo_callback(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaPhoto("https://telegra.ph/file/b1367262cdfbcd0b2af07.mp4"),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data="close")]])
    )

# --------------------------------------------------------------------------------- #

# Function to generate user info image
async def get_userinfo_img(bg_path: str, font_path: str, user_id: int, profile_path: str = None):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((514, 514))
        bg.paste(resized, (94, 102), resized)

    img_draw = ImageDraw.Draw(bg)

    # Draw user ID
    img_draw.text((260, 645), text=str(user_id).upper(), font=get_font(46, font_path), fill=(255, 255, 255))

    # Save image
    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

# Event handler for new members joining the channel
@app.on_chat_member(filters.channel & filters.new_chat_members)
async def on_chat_member_join(client: Client, member: ChatMember):
    for new_member in member.new_chat_members:
        if new_member.user:
            photo = await client.download_media(new_member.user.photo.big_file_id)

            # Generate user info image
            welcome_photo = await get_userinfo_img(bg_path=bg_path, font_path=font_path, user_id=new_member.user.id, profile_path=photo)

            print(f"{new_member.user.first_name} Joined 🤝")

            # Send welcome message
            await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=environ.get("APPROVED_WELCOME_TEXT", "").format(mention=new_member.user.mention, title=member.chat.title),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ʀᴇᴘᴏ •", callback_data="gib_source")]])
            )

# --------------------------------------------------------------------------------- #

if __name__ == "__main__":
    app.run()

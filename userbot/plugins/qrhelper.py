# Credit - Ultra-X Userbot
# Legend X 
# Dont Remove this Line

import os
import qr_img
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern="qrimg ?(.*)"))
async def _(event):
    tx = event.pattern_match.group(1)
    if not tx:
        return await event.edit("Give Text")
    await event.edit("processing")
    p = await event.client.get_profile_photos(bot.me.id)
    if len(p)>=1:
       file = await borg.download_media(p[0])
    else:
       file= "  "
    out = "dc.png"
    qr_img.qrpic(event, file, tx, out)
    await borg.send_file(event.chat_id, out, force_document=False)
    await event.delete()
    
@borg.on(admin_cmd(pattern="qrmark ?(.*)"))
async def _(event):
    tx = event.pattern_match.group(1)
    r = await event.get_reply_message()
    if not (tx and r and r.media):
        return await event.edit("reply to image and Give Text")
    await event.edit("processing")
    d = await borg.download_media(r.media)
    out = "dc.png"
    qr_img.watermark_qr(event, d, tx, out)
    await borg.send_file(event.chat_id, out, force_document=False)
    await event.delete()
 
    
@borg.on(admin_cmd(pattern="qrdecode$"))
async def _(event):
    r = await event.get_reply_message()
    if not (r and r.media):
        return await event.edit("reply to image and Give Text")
    await event.edit("processing")
    image = await borg.download_media(r.media)
    tx = qr_img.qr_decode(image)
    await event.edit("Decoded Text:\n\n" + tx)

#оригинал - t.me/memeframe
from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap

def register(cb):
	cb(DanMod())
	
class DanMod(loader.Module):
	"""JevilQuotes"""
	strings = {
		'name': 'JevilQuotes',
		'usage': '<b>Ошибка!</b> Пропишите <code>.help JevilQuotes</code> для помощи.'
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
		
	async def jcmd(self, message):
		""".jevil <в ответ на сообщение/свой текст>. """
		
		ufr = requests.get("https://github.com/Dan1ello/FTGModules/raw/main/3952.ttf")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Всем приятного дня ❤️!</b>")
		pic = requests.get("https://x0.at/zwN.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		#txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 19))
		t = text + "\n"
		#t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 32, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+10, h+10), (0, 0,0,0))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((10, 10),t,(0,0,0),font=font, align='left')
		imtext.thumbnail((339, 181))
		w, h = 339, 181
		img.paste(imtext, (10,10), imtext)
		out = io.BytesIO()
		out.name = "jevil.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()

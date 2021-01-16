#оригинал - t.me/memeframe
from .. import loader
import requests
import re
@loader.tds
class HeartsMod(loader.Module):
  "Максимально простой антивирус для проверки модулей на код, который может удалить аккаунт"
  strings = {"name": "MicroAV"}
  @loader.owner
  async def avcmd(self, m):
	  "Проверить модуль на угрозы"
	  reply = await m.get_reply_message()
	  if reply and reply.file:
	    if not reply.file.ext in [".py", ".txt", ".bin"]:
	      await m.edit("[AV] UNSUPPORTED_FILE")
	      return
	  else:
	    await m.edit("[AV] REPLY_TO_FILE")
	    return
	  ch = (await reply.download_media(bytes)).decode().split("\n")
	  avdb = re.compile("|".join([i for i in requests.get("http://d4n13l3k00.ml/files/avdb").text.split("\n") if i != ""]))
	  s = 1
	  t = 0
	  result = "<b>[AV] Результат проверки:</b>\n"
	  for i in ch:
	    if avdb.match(i):
	      t += 1
	      result += f"<b>Строка</b> <code>{s}</code>: <i>Вредноносный код</i>\n"
	    s += 1
	  await m.edit(result + f"<b>Всего найдено угроз:</b> <code>{t}</code>")

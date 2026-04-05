#from bot import app, bot
from pyrogram import filters, idle, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyromod import listen
from pymongo import MongoClient
import os, sys
mo = MongoClient("mongodb+srv://MAKER:MAKER@cluster0.5jwntiw.mongodb.net/?retryWrites=true&w=majority")
mo = mo["database"]
db = mo.moltqa
dbb = mo.moltqadata
apro = {}
token = "8644976327:AAEZc4DpRYeRrkdXI8TqFTjJqR557ln2ik4"
app = Client("ElNqYbD", api_id=20702511, api_hash="5c9b9dbf8394f4d247e60cd729ad5e4a", bot_token=token)
devs = ["NQYYB", "AhmedAbouelela1998"]
ban = [1343308286]
txt = """مرحبا بك في بوت تيم الملتقي
يمكن الاستمتاع الي التسجيلات الخاصه بكليه الحقوق
يتم مراجعه طلبات الاستماع بواسطة الاداره
تم تطوير هذه الاداه بواسطة [احمد النقيب ☘️☕](https://t.me/NQYYB)"""
for xxx in db.find({}):
    text = xxx["text"]
    if not apro.get(text):
       apro[text] = []
    apro[text].append(xxx["user_id"])
#@app.on_message(filters.command("/start", ""))
async def startco(c, m):
       if not m.from_user.username in devs:
         await m.reply_text(text)
       else:
         await m.reply_text("Hello Sir", reply_markup=ReplyKeyboardMarkup([["انشاء تسجيل"]], resize_keyboard=True))
@app.on_message(filters.command("انشاء تسجيل", ""))
async def crate(c, m):
    if not m.from_user.username in devs: return
    ask = await c.ask(m.chat.id, "ابعت التسجيل", filters=filters.user(m.from_user.id), timeout=360)
    ask2 = await c.ask(m.chat.id, "ارسل الوصف لهذا التسجيل", filters=filters.user(m.from_user.id), timeout=360)
    await m.reply_text("جاري حفظ الملف انتظر")
    mm = await ask.download()
    ask = await c.send_voice(m.chat.id, mm, caption=ask2.text)
    if not ask.media: return await m.reply_text("ابعت ملف صوتي")
    id = f"{m.from_user.id}elnqyb{ask.id}"
    if m.from_user.username == "NQYYB":
      id = f"{m.from_user.id}elnqyb{ask.id}admin"
    await m.reply_text(f"**تم انشاء رابط التسجيل ✨♥️**\n\nhttps://t.me/{c.me.username}?start={id}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"رابط التسجيل", url=f"https://t.me/{c.me.username}?start={id}")]]))

@app.on_message(filters.command("انشاء ماده", ""))
async def cratenew(c, m):
    if not m.from_user.username in devs: return
    text = ""
    ask = await c.ask(m.chat.id, "اسم الماده اي", filters=filters.user(m.from_user.id), timeout=360) 
    name = ask.text
    ask = await c.ask(m.chat.id, "للفرقه الكام", filters=filters.user(m.from_user.id), timeout=360) 
    group = ask.text
    ask = await c.ask(m.chat.id, "عدد التسجيلات", filters=filters.user(m.from_user.id), timeout=360)
    try:
      xo = int(ask.text)
    except:
      return await m.reply_text("عدد غير صالح")
    num = int(ask.text)
    for x in range(num):     
        ask = await c.ask(m.chat.id, "ابعت التسجيل", filters=filters.user(m.from_user.id), timeout=360)
        ask2 = await c.ask(m.chat.id, "ارسل الوصف لهذا التسجيل", filters=filters.user(m.from_user.id), timeout=360)
        await m.reply_text("جاري حفظ الملف انتظر")
        mm = await ask.download()
        ask = await c.send_voice(m.chat.id, mm, caption=ask2.text)
        if not ask.media: return await m.reply_text("ابعت ملف صوتي")
        text += str(ask.id)
        if not x + 1 == num:
          text += "-"
    id = f"{m.from_user.id}elnqyb{text}"
    dbb.insert_one({"id": id, "name": name, "group": group})
    if m.from_user.username == "NQYYB":
      id = f"{m.from_user.id}elnqyb{text}admin"
    await m.reply_text(f"**تم انشاء رابط للماده ✨♥️**\n\nhttps://t.me/{c.me.username}?start={id}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"رابط التسجيل", url=f"https://t.me/{c.me.username}?start={id}")]]))
    
    
tryy = {}

@app.on_callback_query(filters.regex("no"))
async def callhhbackno(c, q):
       callback_data = q.data.strip()
       text = callback_data.split(None, 1)[1]
       user_id = int(text.split("|")[0])
       await c.send_message(user_id, "تم رفض طلبك لسماع التسجيل")
       return await q.answer("تم رفض الطلب بنجاح ✅", show_alert=True)
xx = {}
@app.on_callback_query(filters.regex("ok"))
async def callback(c, q):
       data = q.data.strip()
       text = data.split(None, 1)[1]
       user_id = int(text.split("|")[0])
       text = text.split("|")[1]
       chat = int(text.split("elnqyb")[0])
    #   id = int(text.split("elnqyb")[1])
       chat_id = q.message.chat.id
       message_id = q.message.id
       if not apro.get(text):
         apro[text] = []
       if not q.from_user.username == "NQYYB":
         if user_id in apro[text]: return await q.answer("المستخدم مقبول بالفعل ✅", show_alert=True)
       apro[text].append(user_id)
       db.insert_one({"text": text, "user_id": user_id})
       if q.from_user.username == "NQYYB":
          meen = "[احمد النقيب](https://t.me/NQYYB)"
       else:
          meen = men(q.from_user)
       xb = dbb.find_one({"id": text})
       if xb:
               group = xb["group"]
               nme = xb["name"]
               data = f"لماده {nme} للفرقه {group}\n"
       else:
               data = ""
       await c.send_message(user_id, f"تم قبول طلبك \n{data}بواسطة {meen}")
       xcode = f"{text}{user_id}"
     #  if xx.get(xcode):
         #await c.delete_messages(user_id, [xx[xcode], xx[xcode] - 1])
       id = text.split("elnqyb")[1]
       for n in id.split("-"):
           id = int(n)
           x = await c.copy_message(user_id, chat, id, protect_content=True)
   #    xx[xcode] = x.id
       await q.answer("تم قبول الطلب وإرسال التسجيل بنجاح ✅", show_alert=True)



def men(name, id=None):
    if not id:
       id = name.id
       name = name.first_name
    return f"[{name}](tg://openmessage?user_id={id})"

@app.on_message(filters.command("حدث"))
async def upppp(c, m):
    os.system("screen -dmS moltqa python3 moltqa.py")
    sys.exit()

@app.on_message(filters.command("start"))
async def start(c, m):
  if m.from_user.id in ban: return await m.reply_text("تم حظرك من خلال الاداره")
  if len(m.text.split()) > 1:
    text = m.text.split(None, 1)[1]
    ss = None
    if "admin" in text:
         ss = True
    text = text.replace("admin", "")
    code = text + str(m.from_user.id)
    user_id = m.from_user.id
    if not apro.get(text):
      apro[text] = []
    if not m.from_user.username in devs:
     if not m.from_user.id in apro[text]:
      if not tryy.get(code): 
        xb = dbb.find_one({"id": text})
        if xb:
               group = xb["group"]
               nme = xb["name"]
               data = f"الفرقه {group}\nماده {nme}\n"
        else:
               data = ""
        ask = await c.ask(m.chat.id, "ارسل اسمك بالكامل", timeout=360)
        name = ask.text
        ask = await c.ask(m.chat.id, "ارسل رقم الهاتف", timeout=360)
        num = ask.text
        for d in devs:
           if ss and not d == "NQYYB": continue
           try:
            await c.send_message(d, f"طلب جديد\nالحساب : {men(m.from_user)}\nالاسم : {name}\nالرقم : {num}\n{data}الكود التعريفي للتسجيل :\n\nhttps://t.me/{c.me.username}?start={text}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                text="« قبول »",
                callback_data=f"ok {user_id}|{text}")
            ],
            [
            InlineKeyboardButton(
                text="« رفض »",
                callback_data=f"no {user_id}")
            ]]),
            reply_to_message_id=int(text.split("elnqyb")[1].split("-")[0]))
           except Exception as a:
             print(a)
        tryy[code] = True
        return await m.reply_text("تم ارسال طلبك الي الاداره")
      else:
        return await m.reply_text("لقد قدمت طلب مسبقاً")
    chat = int(text.split("elnqyb")[0])
    id = text.split("elnqyb")[1]
    print(id)
    for x in id.split("-"):
        id = int(x)
        await c.copy_message(m.chat.id, chat, id, protect_content=True)
  else:
     if not m.from_user.username in devs:
         await m.reply_text(txt)
     else:
         await m.reply_text("Hello Sir", reply_markup=ReplyKeyboardMarkup([["انشاء تسجيل"]], resize_keyboard=True))



@app.on_message(filters.command(["المقبولين"], ""))
async def getalll(client, message):
       if not message.from_user.username == "NQYYB": return
       ask = await client.ask(message.chat.id, "ارسل الكود التعريفي •")
       xx = ask.text.replace(f"https://t.me/{client.me.username}?start=", "")
       text = ""
       c = 0
       for x in apro[xx]:
           c += 1
           try:
             user = await client.get_users(x)
             text += f"{c}- {men(user)}\n"
           except Exception as a:
              print(a)
       text = f"عدد المقبولين {c}\n\n{text}"
       await message.reply_text(text)

@app.on_message(filters.command(["رد"], ""))
async def sssendtodev(client, message):
  if not message.chat.username in ["NQYYB"]: return
  ask = await client.ask(message.chat.id, "ارسل معرف الان •")
  if "@" in ask.text:
    dev = ask.text.replace("@", "")
  else:
   try:
    dev = int(ask.text)
   except:
    dev = ask.text
  try:
    text = message.text.replace("رد", "")
    await client.send_message(dev, text)
    await message.reply_text("Done")
  except Exception as a:
       await message.reply_text(a)
    
@app.on_message(filters.private)
async def check(client, message):
   if message.from_user.username in ["NQYYB"]: return
   await client.send_message("NQYYB", f"New Message ✨♥️ \nUser : {men(message.from_user)} \nUser ID : {message.from_user.id}\n\nMessage Text : {message.text}")
app.start()
print("Running 💨💚")
print(app.me.username)
idle()
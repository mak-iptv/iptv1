import telebot
import requests,json
from telebot import types
from flask import Flask, request
imports
from datetime import datetime
import traceback


TOKEN = os.environ['']
WEBHOOK = os.environ['']


bot = telebot.TeleBot('5542422773:AAGF9JrWa2cbCSpWWXyQ2UeyUw8f9J-bRo')
server = Flask(__name__)

@bot.message_handler(commands={"start"})
def start(message):
cid = message.chat.id
bot.send_message(cid,"Hello!\nThis bot will allow you to check the status of your lists using the Xtream Codes API.\nTo check your list you just have to send me the link and I will show you all the information\n\nBot developed by stbemu\nhttps://github.com/mak-iptv/iptv1/iptv-checker")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
try:
number_streams = 0
cid = message.chat.id
url = message.text
url = url.replace('get.php','panel_api.php')
response = requests.get(url)
open('response.json', 'wb').write(response.content)
f = open('response.json')
json_file = json.load(f)
json_str = json.dumps(json_file)
resp = json.loads(json_str)
username = resp['user_info']['username']
password = resp['user_info']['password']
status = resp['user_info']['status']

expire_dates = resp['user_info']['exp_date']
if (expire_dates != None):
expire_date = datetime.fromtimestamp(int(expire_dates))

expire=True

expire_year = expire_date.strftime("%Y")
expire_month = expire_date.strftime("%m")
expire_day = expire_date.strftime("%d")
else:
expire = False

creates_dates = resp['user_info']['created_at']
create_date = datetime.fromtimestamp(int(creates_dates))
create_year = create_date.strftime("%Y")
create_month = create_date.strftime("%m")
create_day = create_date.strftime("%d")

a_connections = resp['user_info']['active_cons']
m_connections = resp['user_info']['max_connections']

for stream in resp['available_channels']:
number_streams = number_streams+1

url_server = resp['server_info']['url']
port_server = resp['server_info']['port']
client_area = "http://"+url_server+":"+port_server+"/client_area/index.php?username="+username+"&password="+password+"&submit"

if (expire == True):
message ="This is your list information ⬇️\n\n🟢 Status: "+status+"\n👤 Username: "+username+"\n🔑 Password: "+password+"\n📅 Expiration Date: "+str (expire_day)+"-"+str(expire_month)+"-"+str(expire_year)+"\n📅 Creation Date: "+str(create_day)+"-"+str(create_month)+"-"+ str(create_year)+"\n👥Active connections: "+a_connections+"\n👥Maximum connections: "+m_connections+"\n🔢Number of Channels: "+str(numero_streams)+"\n🖥️Server: "+url_server+" :"+port_server+"\n🔒 Client Area: "+client_area+"\n\n🤖: @STB_EMU_bot\ n Develop by STB_EMU"
else:
message="This is your list information ⬇️\n\n🟢 Status: "+status+"\n👤 Username: "+username+"\n🔑 Password: "+password+"\n📅 Expiration Date: Never\n 📅 Creation Date: "+str(create_day)+"-"+str(create_month)+"-"+str(create_year)+"\n👥 Active Connections: "+a_connections+"\n👥 Maximum Connections: "+m_connections+ "\n🔢 Number of Channels: "+str(numero_streams)+"\n🖥️ Server: "+url_server+":"+port_server+"\n🔒 Client Area: "+client_area+"\n\n🤖: @STB_EMU_bot\ n Develop by STB_EMU "
except:
message= "I couldn't get the information from this link. Try another one"

bot.reply_to(message, message)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
return "!", 200


@server.route("/")
def webhook():
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK + TOKEN)
return "!", 200

if __name__ == "__main__":
server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

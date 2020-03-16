from telethon.sync import TelegramClient, events
#import telehon



def checkSell(listsell,listMessage):
    for message in listMessage:
        if message.upper() in listsell:
            return True
    return False

def checkBuy(listBuy,listMessage):
    for message in listMessage:
        if message.upper() in listBuy:
            return True
    return False
    
#check quantity number and unit (k,....) convert to number
def isNumber(number):
    #return a number

    return number

#check type of coin 100eth 3btc 

#check price

# def get
# reject message not buy/sell
def processMessage(message)->list():
    listMessage = message.split()
    ojbMessage={}
    for msg in listMessage:
        if checkBuy(msg)==True:
            ojbMessage["action"]= "Buy"
        else:
            ojbMessage["action"]= "Sell"



    return ojbMessage


def conect():
    #config
    api_id = "1265435"
    api_hash = '17e1fd69156fa33ec73960a5806b4897'
    client = TelegramClient('lhvietanh', api_id, api_hash)
    group_name = {'Chợ Bitcoin Sài Gòn','Các thánh than cà khịa'}
    listSell= {'Bán','ban'}
    listBuy={'mua'}

    @client.on(events.NewMessage(chats=group_name))
    async def handler(event):
        # Good
        chat = await event.get_chat()
        #print(chat)
        sender = await event.get_sender()
        print("GroupID:",chat.id,"Group_name: ",chat.title,"UserName: ",sender.username," --- Chat: ",event.raw_text)

        sender = await event.get_sender()
        #print("send_information:", sender)
        print ("------------------------")
        #chat_id = event.chat_id
        #sender_id = event.sender_id        
        #print(sender,"(",sender_id,"): ",chat)
    
    
    #client.conversation()
    client.start()
    client.run_until_disconnected()

def main():
    conect()

if __name__ == "__main__":
    main()

'''
hat:  bán 100eth 3b 30k u giá rẻ
send_information: User(id=738172024, is_self=False, contact=False, 
mutual_contact=False, deleted=False, bot=False, bot_chat_history=False, 
bot_nochats=False, verified=False, restricted=False, min=False, bot_inline_geo=False,
 support=False, scam=False, access_hash=-4169309912405523607, first_name='🤗🤗Nguyễn Văn Liêm🤗🤗',
  last_name=None, username='Liemnv0982439993', phone=None, photo=UserProfilePhoto(photo_id=3170424702358366124, 
  photo_small=FileLocationToBeDeprecated(volume_id=857419100, local_id=285381), 
  photo_big=FileLocationToBeDeprecated(volume_id=857419100, local_id=285383), dc_id=5),
   status=UserStatusOnline(expires=datetime.datetime(2020, 3, 14, 15, 31, 39, tzinfo=datetime.timezone.utc)),
    bot_info_version=None, restriction_reason=[], bot_inline_placeholder=None, lang_code=None)

-->get_chat
 Channel(id=1090543698, title='Chợ Bitcoin Sài Gòn', photo=ChatPhoto(photo_small=FileLocationToBeDeprecated(volume_id=858110199, 
 local_id=133965), photo_big=FileLocationToBeDeprecated(volume_id=858110199, local_id=133967), dc_id=5), 
 date=datetime.datetime(2020, 3, 14, 1, 47, 28, tzinfo=datetime.timezone.utc), version=0,
  creator=False, left=False, broadcast=False, verified=False, megagroup=True
  , restricted=False, signatures=False, min=False, scam=False, has_link=True, h
  as_geo=False, slowmode_enabled=False, access_hash=9213263521758470225, username=None, 
  restriction_reason=[], admin_rights=None, banned_rights=None, default_banned_rights=ChatBannedRights
  (until_date=datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=datetime.timezone.utc),
   view_messages=False, send_messages=False, send_media=False, send_stickers=False,
    send_gifs=False, send_games=False, send_inline=False, embed_links=False,
     send_polls=False, change_info=True, invite_users=False, pin_messages=True), participants_count=None)
UserName:  thanhnhan0963731294  --- Chat:  Ngủ đến tối là lại lên
------------------------   
'''
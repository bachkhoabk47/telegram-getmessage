from telethon.sync import TelegramClient, events
#import telehon
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (PeerChannel)

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


def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
#check quantity number and unit (k,....) convert to number


#check type of coin 100eth 3btc 

#tack so va chu 
def splitNumberString(string,count,list_coint)->dict():
    numStr =dict()
    Quanlity= ""
    CoinType =""
    for a in string: 
        if (a.isnumeric()) == True:
            Quanlity += str(a)
        else: 
            CoinType += str(a)
        if a.upper() == 'K':
            Quanlity = Quanlity + '000'
            CoinType = ''
    numStr['Quanlity'+str(count)]=Quanlity
    if CoinType.upper() in list_coint:
        numStr['CoinType'+str(count)]=CoinType
    return numStr
# kiem tra xem chuoi cos chu va so ko
def isNumStr(string):
    num =0
    str =0
    for a in string: 
        if (a.isnumeric()) == True: 
            num = num +1
        else:
            if a == '.'or a == ',' : 
                continue
            str = str +1
    if num > 0 and str > 0:
        return True
    else:
        return False

#count coint
def countCoin(messageList,listCoin):
    count = 0
    for msg in messageList:
        for coin in listCoin:
            if coin in msg.upper():
                count +=1        
    return count

#chek name of coin


#check soluon
#check price

# def get
# reject message not buy/sell
def processMessage(message,listCoin)->list():
    #message = "MUA 50K USDT 24300"
    listMessage = message.split()
    ojbMessage=dict()
    countCoint = countCoin(listMessage,listCoin)
    print( "coint count In proce: ",countCoint)
    count_price =0
    flagAction = 0
    for msg in listMessage:
        if (msg.upper() == "MUA")and flagAction==0:
            ojbMessage['action']= "Buy"
            flagAction=1
        elif msg.upper() in {"BÁN","BAN"} and flagAction==0:
            ojbMessage['action']= "Sell"
            flagAction=1
        if isNumStr(msg)==True:
            temp = splitNumberString(msg,count_price,listCoin)
            ojbMessage.update(temp)
            if (ojbMessage["Quanlity"+str(count_price)] != 0):
                count_price += 1
        if  (is_float(msg) == True) and count_price < countCoint - 1 :
            ojbMessage['Quanlity'+str(count_price)] = msg
            count_price += 1
        if msg.upper() in listCoin:
            ojbMessage["CoinType"+str(count_price-1)]= msg.upper()

    if is_float(msg)==True:
        ojbMessage["price"] = msg

    return ojbMessage


def conect():
    #config
    api_id = "1265435"
    api_hash = '17e1fd69156fa33ec73960a5806b4897'
    client = TelegramClient('sessiong_name', api_id, api_hash)
    #group_name = {'Các thánh than cà khịa','Chợ Bitcoin Hà Nội'}
    listCoin = {'ETH',' B','BTC','U','USDT','BIT','E'}
   
   

    
    
    try:
        @client.on(events.NewMessage(chats=None))
        async def handler(event):
        # Good
            try:
                chat = await event.get_chat()
                
            #print(chat)
                sender =await event.get_sender()
                print("GroupID:",str(chat.id),"Group_name: ",str(chat.title),"UserName: ",str(sender.username)," --- Chat: ",str(event.raw_text))
                list_record = list()
                
                list_chat= processMessage(event.raw_text,listCoin)
                print(list_chat)
                
                num_record =0 
                for i in range(10):
                    if ("Quanlity"+str(num_record)) in list_chat and ("CoinType"+str(num_record)) :
                       
                        recorddb = dict()
                        recorddb['Groupid']= chat.id
                        recorddb['GroupName']= chat.title
                        recorddb['UserName']= sender.username
                        recorddb['UserID']= sender.id
                        recorddb['UserPhone']= sender.phone
                        recorddb['Chat']= event.raw_text
                        recorddb['action']= list_chat['action']
                        recorddb['Quanlity']= list_chat['Quanlity'+str(num_record)]
                        recorddb['CoinType']= list_chat['CoinType'+str(num_record)]
                        list_record.append(recorddb)
                        ####
                        # send thist record to database >>> list_record
                        '''
                        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
                        mydb = myclient["mydatabase"]
                        mycol = mydb["customers"]
                        ----recorddb is dict() type
                        recorddb =  {'Groupid': 1135988787, 'GroupName': 'Chợ Bitcoin Hà Nội', 'UserName': 'isabeLLathu', 'UserID': 155296816, 'UserPhone': None, 'Chat': 'Bán 60 eth giá tốt', 'action': 'Sell', 'Quanlity': '60', 'CoinType': 'ETH'}

                        x = mycol.insert_one(recorddb)
                        '''
                        ####
                        print ("Recrod to database ",recorddb)
                        num_record = num_record +1
                    
            #sender = await ev81ent.get_sender()
            #print("send_information:", se  nder)

                #print (str(processMessage(event.raw_text,listCoin)))
                print("-------------")
            #chat_id = event.chat_id
            except Exception as identifier:
                pass
    except Exception as identifier:
        pass
   
    #client.conversation()
    client.start()
    client.run_until_disconnected()


def main():
    listCoin = {'ETH',' B','BTC','USDT'}
    msg = "bán 100ETH và 2 BTC , 20kUSDT giá 23.56"
    #print (processMessage(msg,listCoin))
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

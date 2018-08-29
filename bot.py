import telepot
import os

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global caption
    global num
    global nameFile
    #keepFile = open('num.txt', 'r')
    #lista = []
    #for val in keepFile.read().split():
        #lista.append(int(val))
    #keepFile.close()
    #num = lista[0]
    #print(num)
    listaFoto = []
    #keepFile = open('num.txt', 'w')

    username = msg['from']['username']

    if username == 'Giusmat' or username == 'VeryRareBoyz' or username == 'Cr3sh':
        print("Username corretto!")
        if content_type == 'photo':
            listaFoto.append(msg)
            for x in listaFoto:
                if 'caption' in x:
                    caption = str(x['caption'])
                    print(caption)
                else:
                    print("Caption non presente!")
        
            for x in listaFoto:
                if not 'caption' in x:
                    msg.update({'caption': caption})
                    print("Aggiunto con successo!")
                    print(listaFoto)

        
       
            nameFile = caption.lower() +'0.png'

            if os.path.isfile(nameFile) == True: #se il file esiste
                num = 0
                while os.path.isfile(nameFile) != False:
                    new = list(nameFile)
                    new[len(nameFile)-5] = str(num)
                    nameFile = ''.join(new)
                    num += 1
                    print("Ottenuto : ", nameFile)
            
                #keepFile.write(str(num))
                #keepFile.close()
                bot.download_file(msg['photo'][-1]['file_id'], nameFile)
            else:
                bot.download_file(msg["photo"][-1]["file_id"], nameFile)

        if content_type == 'text':
            nome = msg['text'].lower()
            #nameFile = str(msg['text'])+'0.png'
            conta = 0
            print(nome)
            print(num)

            for x in range(num):
                name = str(nome)+str(conta)+'.png'
                print(name)
                bot.sendPhoto(chat_id, open(name, 'rb'))
                conta += 1
        
            #print(msg,'\n\n\n')
            #print("Caption messaggio : ", msg['caption'])

TOKEN = "672480353:AAFo25cYizqnkNuqSOZ1jNR0eOTKOw7mR_M"
bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': on_chat_message})

import time
while 1:
    time.sleep(10)

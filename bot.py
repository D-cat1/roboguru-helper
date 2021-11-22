from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import pytesseract
import random
import string
from roboguru import cari
from time import sleep
import os
import imgkit
from pyvirtualdisplay import Display

client_robo = Client("hiyahiya",bot_token='1998370175:AAGBRDmRSGhHwlCSI95u_nZfx-_lHXoYZvk', api_id=1428215, api_hash='e7cc39008d3f5f1ee045f6b323c16786')

def jenjang(jeneng_file):
    return [[InlineKeyboardButton("SD", callback_data='jj 94LL64YTJA dig {}'.format(jeneng_file))],[InlineKeyboardButton("SMP", callback_data='jj XHAGLMC2TA dig {}'.format(jeneng_file))],[InlineKeyboardButton("SMA", callback_data='jj 3GAWQ3PJRB dig {}'.format(jeneng_file))],[InlineKeyboardButton("SBMPTN & STAN", callback_data='jj 489EUDXNA8 dig {}'.format(jeneng_file))]]

def versi_sd(jeneng_file):
    return [[InlineKeyboardButton("➗ Matematika", callback_data='mpl matematika {}'.format(jeneng_file))], [InlineKeyboardButton('🇮🇩 Bahasa Indonesia', callback_data='mpl bahasa%20indonesia {}'.format(jeneng_file))], [InlineKeyboardButton('🌱 IPA Terpadu', callback_data='mpl ipa%20terpadu {}'.format(jeneng_file))]]

def versi_nonsd(jeneng_file):
    return [[InlineKeyboardButton("➗ Matematika", callback_data='mpl matematika {}'.format(jeneng_file))], [InlineKeyboardButton('🇮🇩 Bahasa Indonesia', callback_data='mpl bahasa%20indonesia {}'.format(jeneng_file))], [InlineKeyboardButton('🌱 Biologi', callback_data='mpl biologi {}'.format(jeneng_file))], [InlineKeyboardButton('🍎 Fisika', callback_data='mpl fisika {}'.format(jeneng_file))], [InlineKeyboardButton('‍🔬 Kimia', callback_data='mpl kimia {}'.format(jeneng_file))], [InlineKeyboardButton('🇬🇧 Bahasa Inggris', callback_data='mpl bahasa%20inggris {}'.format(jeneng_file))], [InlineKeyboardButton('⏳ Sejarah', callback_data='mpl sejarah {}'.format(jeneng_file))], [InlineKeyboardButton('💵 Ekonomi', callback_data='mpl ekonomi {}'.format(jeneng_file))], [InlineKeyboardButton('🌏︎ Geografi', callback_data='mpl geografi {}'.format(jeneng_file))], [InlineKeyboardButton('🫂 Sosiologi', callback_data='mpl sosiologi {}'.format(jeneng_file))]]

def randomize():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(3))

@client_robo.on_message(filters.command('start'))
def start(client, message):
    #print(message)
    client.send_message(message["chat"]["id"], """Hai {} 👋
saya adalah bot penjawab soal
kamu bisa memberikan soal kesaya melalui foto atapun text😊""".format(message["from_user"]["first_name"]))

@client_robo.on_message(filters.command('tanya'))
def cuaks(client, pesan):
    if pesan.reply_to_message:
        if pesan.reply_to_message.photo:
            nama_file = randomize()
            client_robo.download_media(pesan.reply_to_message.photo.file_id, file_name=nama_file+'.jpg')
            client_robo.send_message(pesan.chat.id, "Silahkan pilih jenjang dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(jenjang(nama_file+'.jpg')))
            #ocr_text = pytesseract.image_to_string('downloads/{}.jpg'.format(pesan.reply_to_message.photo.file_unique_id), lang='eng')
            #pesan.reply_text(ocr_text)
        elif pesan.reply_to_message.document.mime_type == 'image/png':
            nama_file = randomize()
            client_robo.download_media(pesan.reply_to_message.document.file_id, file_name=nama_file+'.png')
            client_robo.send_message(pesan.chat.id, "Silahkan pilih jenjang dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(jenjang(nama_file+'.png')))
        else:
            print(False)
    else:
        if len(pesan.command) == 1:
            client_robo.send_message(pesan.chat.id, "**Silahkan ketik pertanyaan atau foto pertanyaan lalu reply foto dengan command /tanya**")
        else:
            nama_file = randomize()
            display = Display(visible=0)
            display.start()
            imgkit.from_string('<p>{}</p>'.format(pesan.text.split('/tanya ')[1]), 'downloads/{}.jpg'.format(nama_file))
            client_robo.send_message(pesan.chat.id, "Silahkan pilih jenjang dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(jenjang(nama_file+'.jpg')))

@client_robo.on_callback_query()
def hailah(client, pesan):
    commandfin = pesan.data.split(' ')[0]
    if commandfin == 'jj':
       selector = pesan.data.split(' ')[1]
       if selector == '94LL64YTJA':
           client_robo.delete_messages(pesan.message.chat.id, pesan.message.message_id)
           client_robo.send_message(pesan.message.chat.id, "Silahkan pilih mapel dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(versi_sd(pesan.data)))
       elif selector == 'XHAGLMC2TA':
           client_robo.delete_messages(pesan.message.chat.id, pesan.message.message_id)
           client_robo.send_message(pesan.message.chat.id, "Silahkan pilih mapel dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(versi_nonsd(pesan.data)))
       elif selector == '3GAWQ3PJRB':
           client_robo.delete_messages(pesan.message.chat.id, pesan.message.message_id)
           client_robo.send_message(pesan.message.chat.id, "Silahkan pilih mapel dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(versi_nonsd(pesan.data)))
       elif selector == '489EUDXNA8':
           client_robo.delete_messages(pesan.message.chat.id, pesan.message.message_id)
           client_robo.send_message(pesan.message.chat.id, "Silahkan pilih mapel dengan mengklik tombol dibawah", reply_markup=InlineKeyboardMarkup(versi_nonsd(pesan.data)))
    elif commandfin == 'mpl':
        client_robo.delete_messages(pesan.message.chat.id, pesan.message.message_id)
        namefile = pesan.data.split('dig ')[1]
        mapela = pesan.data.split('mpl ')[1].split(' ')[0]
        kode_kelas = pesan.data.split('jj ')[1].split(' ')[0]
        ocr_text = pytesseract.image_to_string('downloads/{}'.format(namefile), lang='eng')
        aaaaa = client_robo.send_message(pesan.message.chat.id, "Harap tunggu.. Mencari soal yang mirip 🔍")
        aings = cari(ocr_text, mapela, kode_kelas)
        client_robo.edit_message_text(aaaaa.chat.id, aaaaa.message_id, 'Ditemukan {} soal yang mirip\n__Mengirim jawaban  📃__'.format(len(aings)))
        for aing in aings:
            client_robo.send_photo(pesan.message.chat.id, aing)
            sleep(3)
            os.remove(aing)


client_robo.run()

import json
import requests as robo_ribet
import urllib.parse as asik
import html2text
import imgkit
import string
from pyvirtualdisplay import Display

def listAlphabet(isi: int):
  return list(string.ascii_uppercase)[isi]

def cari(soal: str, mapel: str, kodse_kelas: str):
    datajawaban = []
    header = {"accept": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "country": "id",
    "sec-ch-ua": '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "with-auth": "true"}
    h = html2text.HTML2Text()
    h.ignore_images = True
    asri = robo_ribet.get('https://roboguru.ruangguru.com', headers=header)
    a = robo_ribet.get('https://roboguru.ruangguru.com/api/v3/roboguru-discovery/search/question?gradeSerial={}&subjectName={}&withVideo=true&text={}&imageURL=&singleQuestion=false'.format(kodse_kelas, mapel ,asik.quote(soal)), headers=header, cookies=asri.cookies).json()

    #print('Soal : ' +h.handle(a["data"]["questions"][0]["contents"]))
    #print('Link Ke Soal & Jawaban : https://roboguru.ruangguru.com/question/{}'.format(a["data"]["questions"][0]["serial"]))
    #print('Jawab : '+h.handle(a["data"]["questions"][0]["contentDefinition"]))

    #with open('data.json', 'w') as f:
    #    json.dump(a, f)

    for list_quest in a["data"]["questions"]:
        if len(list_quest["options"]) == 0:
            display = Display(visible=0, size(
            display.start()
            imgkit.from_string('<p><b>Soal :</b></p>{}<p><b>Jawaban :</b></p>{}'.format(list_quest["contents"], list_quest['contentDefinition']), 'jawaban/{}.jpg'.format(list_quest['serial']))
            datajawaban.append('jawaban/{}.jpg'.format(list_quest['serial']))
        else:
            dumpopt = ''
            abjad = 0
            for all_answer in list_quest["options"]:
                dumpopt += all_answer.replace("<p>", listAlphabet(abjad)+'. ').replace("<p style=\"text-align: justify;\">", listAlphabet(abjad)+'. ').replace("</p>", "<br>")
                abjad += 1
            display = Display(visible=0)
            display.start()
            imgkit.from_string('<p><b>Soal :</b></p>{}{}<p><b>Jawaban :</b></p>{}'.format(list_quest["contents"],dumpopt, list_quest['contentDefinition']), 'jawaban/{}.jpg'.format(list_quest['serial']))
            datajawaban.append('jawaban/{}.jpg'.format(list_quest['serial']))
    return datajawaban
        
    


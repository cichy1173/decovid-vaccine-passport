import zlib
import base45
import cbor2
import json
import savetofiles
from datetime import datetime

def decodeCertificate(cert):
    b45date = cert.replace("HC1:","")

    zlibdate = base45.b45decode(b45date)

    cbordata = zlib.decompress(zlibdate)
    decoded = cbor2.loads(cbordata)
    decodedstr=cbor2.loads(decoded.value[2])
    jsdate=json.loads(json.dumps(decodedstr, indent=4))
    jssave=json.dumps(decodedstr, indent=4)
    savetofiles.save(jssave)

    #Drukowanie danych
    print("")
    print("Wersja certyfikatu: ", jsdate['-260']['1']['ver'])
    print("Data wydania certyfikatu: ",datetime.utcfromtimestamp(int(jsdate['6'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("Data ważnośći certyfikatu: ",datetime.utcfromtimestamp(int(jsdate['4'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("")
    print("Dane osoby zaszczepionej:")
    print("")
    print("Imię: ", jsdate['-260']['1']['nam']['gnt'])
    print("Nazwisko: ", jsdate['-260']['1']['nam']['fnt'])
    print("Data urodzenia: ", jsdate['-260']['1']['dob'])
    print("")
    print("Przyjęte dawki: ", jsdate['-260']['1']['v'][0]['dn'])
    print("Kod producenta szczepionki: ", jsdate['-260']['1']['v'][0]['ma'])
    print("Typ szczepionki: ", jsdate['-260']['1']['v'][0]['vp'])
    print("Data przyjęcisa ostatniej dawki: ", jsdate['-260']['1']['v'][0]['dt'])
    print("Identyfikator kraju podania szczepionki: ", jsdate['-260']['1']['v'][0]['co'])
    print("Identyfikator certyfikatu : ", jsdate['-260']['1']['v'][0]['ci'])
    print("Kod szczepionki: ", jsdate['-260']['1']['v'][0]['mp'])
    print("Wystawca certyfikatu: ", jsdate['-260']['1']['v'][0]['is'])
    print("LIczba dawek w kuracji: ", jsdate['-260']['1']['v'][0]['sd'])
    print("Kod choroby: ", jsdate['-260']['1']['v'][0]['tg'])
    print("")

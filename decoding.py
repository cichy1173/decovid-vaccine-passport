import zlib
import base45
import cbor2
import json
import savetofiles
from datetime import datetime

#cert = "HC1:6BFOXN%TS3DH1QG9WA6H98BRPRHO DJS4/ R-%2% I+:9AVDQ81LO2-36/X0X6BMF6.UCOMIN6R%E5UX4795:/6N9R%EPXCROGO3HOWGOKEQBKL/645YPL$R-ROM47L*K1UPB65%PDMOL*9DJZI202K-JKYJGCC:H3J1D1I3-*TW C57DNGSE%C-3EXED2SSRST BD%USVJC1HCK0DM.C86U*XC0SSNST$JCD8CBZI+PB/VSQOL9DLSWCZ3EBKDVIJGDBDIT1NJGIA+OJ:CI-L3ZJA/3CZIJFVA.QO5VA81K0ECM8CXVDC8C 1JI7JSTNCA7G6M%28ODSINQIVQUIRYYQ4P7M9SB95S6M/355X7C25E8DLFEA3LS6FPOSXD79NT+X4VIOS0I63K*+7SLS9NTRFBOX4YGFD.O8RJ5XPUVPQRHIY1+ HNQ1PRAAUICO12Y99UE$V1*65PC8Q8J.Y37DT/Z7X.HB:I- 57HH1H1TRR9+VB-F4*2V4712IE2B:0WT/PUXR*2B$Y843C-NAKG6SWMC3VJ*F92215IY3SRZTM$0B61M10HOKU5"

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
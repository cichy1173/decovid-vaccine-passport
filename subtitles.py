from sys import exit
from datetime import datetime

BARCODESCANNER = "https://f-droid.org/packages/com.example.barcodescanner/"

def chooseLanguage():
    print("Choose language")
    print("1. English")
    print("2. Polish")
    print("3. Exit")

    language = input("Type number: ")

    return language


def englishFirstStep():
    
    print("To begin please scan your QR code")
    print("To do this you can use Barcode&QR Scanner from F-Droid")
    print(BARCODESCANNER)

def polishFirstStep():    

    print("Aby zaczac, musisz zeskanowac kod QR, który otrzymales po szczepieniu.")
    print("Aby to zrobic, skorzystaj z aplikacji, np. QR&Barcode Scanner z F-Droid")
    print(BARCODESCANNER)

def quiting():
    exit("Quiting")

def firstStep(lang):

    if lang == "1":
        englishFirstStep()
    elif lang == "2":
        polishFirstStep()
    elif lang == "3":
        quiting()
    else:
        print("Wrong number, try again")
        firstStep()


def englishSecondStep():
    value = input("Paste code here: ")

    return value

def polishSecondStep():
    value = input("Wklej kod tutaj: ")

    return value

def secondStep(lang):
    if lang == "1":
        CERT = englishSecondStep()
    elif lang == "2":
        CERT = polishSecondStep()

    else:
        quiting()

    return CERT
    
            


def printingData(lang, jsonObject):
    if lang == "2":
        polishPrintingData(jsonObject)
    elif lang == "1":
        englishPrintingData(jsonObject)
    else:
        quiting()        

def polishPrintingData(jsonObject):
    print("")
    print("Wersja certyfikatu: ", jsonObject['-260']['1']['ver'])
    print("Data wydania certyfikatu: ",datetime.utcfromtimestamp(int(jsonObject['6'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("Data ważnośći certyfikatu: ",datetime.utcfromtimestamp(int(jsonObject['4'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("")
    print("Dane osoby zaszczepionej:")
    print("")
    print("Imię: ", jsonObject['-260']['1']['nam']['gnt'])
    print("Nazwisko: ", jsonObject['-260']['1']['nam']['fnt'])
    print("Data urodzenia: ", jsonObject['-260']['1']['dob'])
    print("")
    print("Przyjęte dawki: ", jsonObject['-260']['1']['v'][0]['dn'])
    print("Kod producenta szczepionki: ", jsonObject['-260']['1']['v'][0]['ma'])
    print("Typ szczepionki: ", jsonObject['-260']['1']['v'][0]['vp'])
    print("Data przyjęcisa ostatniej dawki: ", jsonObject['-260']['1']['v'][0]['dt'])
    print("Identyfikator kraju podania szczepionki: ", jsonObject['-260']['1']['v'][0]['co'])
    print("Identyfikator certyfikatu : ", jsonObject['-260']['1']['v'][0]['ci'])
    print("Kod szczepionki: ", jsonObject['-260']['1']['v'][0]['mp'])
    print("Wystawca certyfikatu: ", jsonObject['-260']['1']['v'][0]['is'])
    print("Liczba dawek w kuracji: ", jsonObject['-260']['1']['v'][0]['sd'])
    print("Kod choroby: ", jsonObject['-260']['1']['v'][0]['tg'])
    print("")

def englishPrintingData(jsonObject):
    print("")
    print("Certificate version: ", jsonObject['-260']['1']['ver'])
    print("Release date: ",datetime.utcfromtimestamp(int(jsonObject['6'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("Expiration date: ",datetime.utcfromtimestamp(int(jsonObject['4'])).strftime('%Y-%m-%d %H:%M:%S'))
    print("")
    print("Details of the vaccinated person:")
    print("")
    print("First Name: ", jsonObject['-260']['1']['nam']['gnt'])
    print("Last name: ", jsonObject['-260']['1']['nam']['fnt'])
    print("Birthdate: ", jsonObject['-260']['1']['dob'])
    print("")
    print("Doses: ", jsonObject['-260']['1']['v'][0]['dn'])
    print("Producent code: ", jsonObject['-260']['1']['v'][0]['ma'])
    print("Type: ", jsonObject['-260']['1']['v'][0]['vp'])
    print("Date of last dose: ", jsonObject['-260']['1']['v'][0]['dt'])
    print("Country ID: ", jsonObject['-260']['1']['v'][0]['co'])
    print("Certificate ID : ", jsonObject['-260']['1']['v'][0]['ci'])
    print("Vaccine code: ", jsonObject['-260']['1']['v'][0]['mp'])
    print("Certificate provider: ", jsonObject['-260']['1']['v'][0]['is'])
    print("Maximum number of doses: ", jsonObject['-260']['1']['v'][0]['sd'])
    print("Disease code: ", jsonObject['-260']['1']['v'][0]['tg'])
    print("")

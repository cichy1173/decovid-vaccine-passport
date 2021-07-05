from sys import exit
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
    
            



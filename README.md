# deCOVID Vaccine Passport
Application that helps read data from EU Vaccine Passport.


# Installation
Script uses generic Python libraries but You can miss one - CBOR2. Just paste command below

```bash
pip install cbor2
```
# Usage
To read data from EU Vaccine Passport, You need to scan your QR code, for example with open source application [QR & Barcode Scanner](https://github.com/dmitriy-ilchenko/QrAndBarcodeScanner). Application will show you long code starting with ``HC1``.

After that type:
```bash
git clone https://github.com/cichy1173/decovid-vaccine-passport.git
cd decovid-vaccine-passport
python main.py
```
Choose your language and just paste code starting with ``HC1`` into application and press ``Enter``. 

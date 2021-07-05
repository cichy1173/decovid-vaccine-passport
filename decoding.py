import zlib
import base45
import cbor2
import json
import savetofiles

def decodeCertificate(cert):
    b45date = cert.replace("HC1:","")

    zlibdate = base45.b45decode(b45date)

    cbordata = zlib.decompress(zlibdate)
    decoded = cbor2.loads(cbordata)
    decodedstr=cbor2.loads(decoded.value[2])
    jsdate=json.loads(json.dumps(decodedstr, indent=4))
    jssave=json.dumps(decodedstr, indent=4)
    savetofiles.save(jssave)

    return jsdate


   
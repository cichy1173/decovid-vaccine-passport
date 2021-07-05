import zlib
<<<<<<< Updated upstream
=======
import pprint
>>>>>>> Stashed changes
import base45
import cbor2
import json
import savetofiles

import json

# cert = "HC1:6BFOXN%TS3DH1QG9WA6H98BRPRHO DJS4/ R-%2% I+:9AVDQ81LO2-36/X0X6BMF6.UCOMIN6R%E5UX4795:/6N9R%EPXCROGO3HOWGOKEQBKL/645YPL$R-ROM47L*K1UPB65%PDMOL*9DJZI202K-JKYJGCC:H3J1D1I3-*TW C57DNGSE%C-3EXED2SSRST BD%USVJC1HCK0DM.C86U*XC0SSNST$JCD8CBZI+PB/VSQOL9DLSWCZ3EBKDVIJGDBDIT1NJGIA+OJ:CI-L3ZJA/3CZIJFVA.QO5VA81K0ECM8CXVDC8C 1JI7JSTNCA7G6M%28ODSINQIVQUIRYYQ4P7M9SB95S6M/355X7C25E8DLFEA3LS6FPOSXD79NT+X4VIOS0I63K*+7SLS9NTRFBOX4YGFD.O8RJ5XPUVPQRHIY1+ HNQ1PRAAUICO12Y99UE$V1*65PC8Q8J.Y37DT/Z7X.HB:I- 57HH1H1TRR9+VB-F4*2V4712IE2B:0WT/PUXR*2B$Y843C-NAKG6SWMC3VJ*F92215IY3SRZTM$0B61M10HOKU5"

def decodeCertificate(cert):
    b45date = cert.replace("HC1:","")

    zlibdate = base45.b45decode(b45date)

    cbordata = zlib.decompress(zlibdate)
    
    decoded = cbor2.loads(cbordata)
<<<<<<< Updated upstream
    decodedstr=cbor2.loads(decoded.value[2])
    jsdate=json.loads(json.dumps(decodedstr, indent=4))
    jssave=json.dumps(decodedstr, indent=4)
    savetofiles.save(jssave)
    print("Dane certyfikatu")
    print(jsdate['-260']['1']['v'][0])
=======
    pprint(cbor2.loads(decoded.value[2]))

    
>>>>>>> Stashed changes

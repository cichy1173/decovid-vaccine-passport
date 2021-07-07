import subtitles
import decoding

LANGUAGE = subtitles.chooseLanguage()


subtitles.firstStep(LANGUAGE)
CERTIFICATE = subtitles.secondStep(LANGUAGE)

decodedData = decoding.decodeCertificate(CERTIFICATE)

subtitles.printingData(LANGUAGE, decodedData)





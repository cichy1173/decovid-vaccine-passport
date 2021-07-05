import subtitles
import decoding

LANGUAGE = subtitles.chooseLanguage()


subtitles.firstStep(LANGUAGE)
CERTIFICATE = subtitles.secondStep(LANGUAGE)

decoding.decodeCertificate(CERTIFICATE)




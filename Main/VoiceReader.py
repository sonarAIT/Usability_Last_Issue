import speech_recognition as sr


class VoiceReader:
    ERROR_CODE = "__error__"

    def __init__(self):
        self.__rec = sr.Recognizer()
        self.__mic = sr.Microphone()
    
    def ReadVoice(self):
        with self.__mic as source:
            print("ノイズ収集中…")
            self.__rec.adjust_for_ambient_noise(source)
            print("ノイズ収集完了")
        with self.__mic as source:
            print("どうぞ")
            audio = self.__rec.listen(source)
            try:
                text = self.__rec.recognize_google(audio, language="ja-JP")
                return text
            except sr.UnknownValueError:
                return VoiceReader.ERROR_CODE


if __name__ == "__main__":
    voiceReader = VoiceReader()
    print(voiceReader.ReadVoice())
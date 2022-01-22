import speech_recognition as sr


class VoiceReader:
    rec = sr.Recognizer()
    mic = sr.Microphone()

    def ReadVoice(self):
        with self.mic as source:
            print("ノイズ収集中…")
            self.rec.adjust_for_ambient_noise(source)
            print("ノイズ収集完了")
        with self.mic as source:
            print("どうぞ")
            audio = self.rec.listen(source)
            try:
                text = self.rec.recognize_google(audio, language="ja-JP")
                return text
            except sr.UnknownValueError:
                return "error"


if __name__ == "__main__":
    voiceReader = VoiceReader()
    print(voiceReader.ReadVoice())
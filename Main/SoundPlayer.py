import wave
import numpy as np
import sounddevice as sd
from SoundNameRepository import SoundNameRepository


class SoundPlayer:
    def __init__(self) -> None:
        self.__soundMap = {}
        for name, path in SoundNameRepository.GetAll():
            try:
                with wave.open(path) as wf:
                    fs = wf.getframerate()
                    data = wf.readframes(wf.getnframes())
                    data = np.frombuffer(data, dtype='int16')

                    self.__soundMap[name] = (data, fs)
            except Exception as e:
                print('ERROR: 音声読み込み中にエラーが発生しました')
                print(type(e))
                print(e)

    def PlaySound(self, soundName: str) -> None:
        sound = self.__soundMap[soundName]
        sd.play(sound[0], sound[1])
        # sd.play(sound[0], sound[1] * 2) # stereo

    def StopSound(self) -> None:
        sd.stop()


if __name__ == "__main__":
    import time
    soundPlayer = SoundPlayer()
    soundPlayer.PlaySound('CALCING')
    time.sleep(3)
    soundPlayer.StopSound()

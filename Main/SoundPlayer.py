import wave
from SoundNameRepository import SoundNameRepository
import pyaudio


class SoundPlayer:
    def __init__(self) -> None:
        self.__pyaudio = pyaudio.PyAudio()
        self.__streams = []
        self.__soundMap = {}
        for name, path in SoundNameRepository.GetAll():
            try:
                self.__soundMap[name] = wave.open(path)
            except Exception as e:
                print('ERROR: 音声読み込み中にエラーが発生しました')
                print(type(e))
                print(e)

    def PlaySound(self, soundName: str) -> None:
        wf = self.__soundMap[soundName]

        def callback(in_data, frame_count, time_info, status):
            data = wf.readframes(frame_count)
            return (data, pyaudio.paContinue)

        stream = self.__pyaudio.open(format=self.__pyaudio.get_format_from_width(wf.getsampwidth()),
                                     channels=wf.getnchannels(),
                                     rate=wf.getframerate(),
                                     output=True,
                                     stream_callback=callback)

        stream.start_stream()
        self.__streams.append(stream)

    def StopSound(self) -> None:
        for stream in self.__streams:
            stream.stop_stream()
            stream.close()
        self.__streams.clear()

    def __del__(self) -> None:
        for stream in self.__streams:
            stream.close()
        for sound in self.__soundMap:
            self.__soundMap[sound].close()
        self.__pyaudio.terminate()


if __name__ == "__main__":
    import time
    soundPlayer = SoundPlayer()
    soundPlayer.PlaySound('CALCING')
    time.sleep(3)
    soundPlayer.StopSound()
    time.sleep(3)
    del soundPlayer

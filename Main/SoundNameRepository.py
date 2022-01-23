class SoundNameRepository:
    __PATH = "./Main/wav/"
    __SOUND_NAME_DICT = {'CALCING': __PATH + "calcing.wav", 'LAUGHTER1': __PATH + "laughter1.wav", 'LAUGHTER2': __PATH + "laughter2.wav",
                         'LAUGHTER3': __PATH + "laughter3.wav", 'LAUGHTER4': __PATH + "laughter4.wav", 'LAUGHTER5': __PATH + "laughter5.wav", 'PHRASE': __PATH + "phrase.wav"}

    def Get(name: str) -> str:
        return SoundNameRepository.__SOUND_NAME_DICT[name]

    def GetAll() -> list[str]:
        return [(sound, SoundNameRepository.__SOUND_NAME_DICT[sound]) for sound in SoundNameRepository.__SOUND_NAME_DICT]

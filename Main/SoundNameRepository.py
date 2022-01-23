class SoundNameRepository:
    __PATH = "./Main/wav/"
    __SOUND_NAME_DICT = {'CALCING': __PATH + "calcing.wav"}

    def Get(name: str) -> str:
        return SoundNameRepository.__SOUND_NAME_DICT[name]

    def GetAll() -> list[str]:
        return [(sound, SoundNameRepository.__SOUND_NAME_DICT[sound]) for sound in SoundNameRepository.__SOUND_NAME_DICT]

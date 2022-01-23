class SoundNameRepository:
    __PATH = "./Main/wav/"
    __SOUND_NAME_DICT = {'PATH': __PATH, 'CALCING': __PATH + "calcing.wav"}

    def get(name: str) -> str:
        return SoundNameRepository.__SOUND_NAME_DICT[name]

    def getAll() -> list[str]:
        return [(sound, SoundNameRepository.__SOUND_NAME_DICT[sound]) for sound in SoundNameRepository.__SOUND_NAME_DICT]

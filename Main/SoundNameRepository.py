class SoundNameRepository:
    def __init__(self) -> None:
        PATH = "./Main/wav/"

        self.SoundNameDict = {}
        self.SoundNameDict['PATH'] = PATH
        self.SoundNameDict['CALCING'] = PATH + "calcing.wav"

    def get(self, name: str) -> str:
        return self.SoundNameDict[name]

    def getAll(self) -> list[str]:
        return [self.SoundNameDict[sound] for sound in self.SoundNameDict]
import threading
import time
from SoundPlayer import SoundPlayer
from LaughtPlayer import LaughtPlayer
from UI import UI
from FaceName import FaceName
from VoiceReader import VoiceReader
from FunnyUtil import FunnyUtil


class MainProcess:
    def __init__(self) -> None:
        self.__resultDict = {0: self.__badResult, 1: self.__goodResult}
        self.__soundPlayer = SoundPlayer()
        self.__voiceReader = VoiceReader()
        self.__ui = UI(self.StartButtonHandler)
        self.__ui.SetMainLabel('スタートボタンを押してください')
        self.__ui.SetHeadLabel('Gyaha')
        self.__ui.SetFace(FaceName.Normal)
        self.__ui.SetButtonText('スタート')
        self.__ui.MainLoop()

    def StartButtonHandler(self) -> None:
        self.__soundPlayer.StopSound()

        def startButtonProcess():
            recText = self.__voiceReadScene()
            resJudge = self.__judgeScene(recText)
            self.__resultScene(resJudge)

        thread = threading.Thread(target=startButtonProcess)
        thread.start()

    def __voiceReadScene(self) -> str:
        self.__soundPlayer.PlaySound('START')
        self.__ui.SetButtonDisable(True)
        self.__ui.SetMainLabel('ダジャレを言ってください')
        self.__ui.SetHeadLabel('Gyaha')
        self.__ui.SetFace(FaceName.Normal)

        while True:
            retText = self.__voiceReader.ReadVoice()
            if retText != VoiceReader.ERROR_CODE:
                break
            self.__voiceReadErrorScene()

        return retText

    def __voiceReadErrorScene(self):
        self.__soundPlayer.StopSound()
        self.__soundPlayer.PlaySound('ERROR')
        self.__ui.SetMainLabel('うまく聞き取れませんでした．\nもう一度お願いします．')

    def __judgeScene(self, recText: str) -> int:
        self.__soundPlayer.PlaySound('CALCING')
        self.__ui.SetMainLabel('判定中')
        self.__ui.SetHeadLabel(recText)

        dummyThread = threading.Thread(target=time.sleep, args=(5,))
        dummyThread.start()
        resJudge = FunnyUtil.JudgeFunny(recText)
        dummyThread.join()
        return resJudge

    def __resultScene(self, resJudge: int):
        self.__soundPlayer.StopSound()
        self.__ui.SetButtonText('もう一度')
        self.__ui.SetButtonDisable(False)
        self.__resultDict[resJudge]()

    def __goodResult(self):
        LaughtPlayer.PlayLaught(self.__soundPlayer)
        self.__soundPlayer.PlaySound('PHRASE')
        self.__ui.SetMainLabel('判定結果: おもしろ〜い！！！！！！！\n！！！！！！！')
        self.__ui.SetFace(FaceName.Funny)

    def __badResult(self):
        self.__soundPlayer.PlaySound('BAD')
        self.__ui.SetMainLabel('判定結果: つまらないです。')
        self.__ui.SetFace(FaceName.Sad)


if __name__ == "__main__":
    main = MainProcess()

import PySimpleGUI as sg
from FaceName import FaceName


class UI:
    def __init__(self, MainButtonHandler) -> None:
        self.__mainButtonHandler = MainButtonHandler
        LAYOUT = [
            [sg.Column(
                [[sg.Text("", font=("", 50), key="-HEAD_LABEL-")]])],
            [sg.Frame('', [[sg.Image(FaceName.Normal, key="-FACE_IMAGE-"), sg.Text("", font=(
                "", 30), expand_x=True, justification='c', key="-MAIN_LABEL-")]], expand_x=True)],
            [sg.Column([[sg.Button("", key="-START_BUTTON-")]])]
        ]
        self.WINDOW = sg.Window(
            "Gyaha", LAYOUT, size=(900, 300), element_justification='c', finalize=True)

    def MainLoop(self) -> None:
        while True:
            event, values = self.WINDOW.read()
            if event == sg.WIN_CLOSED:
                self.Close()
                break

            if event == "-START_BUTTON-":
                self.__mainButtonHandler()

    def SetMainLabel(self, text: str) -> None:
        self.WINDOW["-MAIN_LABEL-"].Update(text)

    def SetHeadLabel(self, text: str) -> None:
        self.WINDOW["-HEAD_LABEL-"].Update(text)

    def SetFace(self, faceName: str) -> None:
        self.WINDOW["-FACE_IMAGE-"].Update(faceName)

    def SetButtonText(self, text: str) -> None:
        self.WINDOW["-START_BUTTON-"].Update(text)

    def SetButtonDisable(self, flag: bool) -> None:
        self.WINDOW["-START_BUTTON-"].Update(disabled=flag)

    def Close(self) -> None:
        self.WINDOW.close()


if __name__ == "__main__":
    ui = None

    def testButtonHander():
        ui.SetMainLabel("ウホウホウホウホウホウホウホウホウホウホ")
        ui.SetHeadLabel("ウホウホウホウホウホ")
        ui.SetFace(FaceName.Funny)
        ui.SetButtonText("ウホ")
        ui.SetButtonDisable(True)
    ui = UI(testButtonHander)
    ui.SetMainLabel("スタートボタンを押してください")
    ui.SetHeadLabel("Gyaha")
    ui.SetButtonText("スタート")
    ui.MainLoop()

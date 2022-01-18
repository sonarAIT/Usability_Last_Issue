import PySimpleGUI as sg
from FaceName import FaceName


class UI:
    def __init__(self) -> None:
        LAYOUT = [
            [sg.Text("", font=("", 50), key="-HEAD_LABEL-")],
            [sg.Image(FaceName.Normal, key="-FACE_IMAGE-"), sg.Text("", font=("", 30), key="-MAIN_LABEL-")],
            [sg.Button("スタート", key="-START_BUTTON-")]
        ]
        self.WINDOW = sg.Window("ほげ", LAYOUT, element_justification='c')

    def Read(self) -> None:
        event, values = self.WINDOW.read()
        return (event, values)

    def UpdateMainLabel(self, text) -> None:
        self.WINDOW["-MAIN_LABEL-"].Update(text)

    def UpdateHeadLabel(self, text) -> None:
        self.WINDOW["-HEAD_LABEL-"].Update(text)

    def UpdateFace(self, faceName) -> None:
        self.WINDOW["-FACE_IMAGE-"].Update(faceName)

    def Close(self) -> None:
        self.WINDOW.close()


if __name__ == "__main__":
    ui = UI()

    while True:
        event, values = ui.Read()
        if event == sg.WIN_CLOSED:
            ui.Close()
            break

        if event == "-START_BUTTON-":
            ui.UpdateMainLabel("ウホウホウホウホウホウホウホウホウホウホ")
            ui.UpdateHeadLabel("ウホウホウホウホウホ")
            ui.UpdateFace(FaceName.Funny)

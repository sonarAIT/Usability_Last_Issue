from SoundPlayer import SoundPlayer


class LaughtPlayer:
    def __init__(self, soundPlayer: SoundPlayer):
        self.__soundPlayer = soundPlayer

    def PlayLaught(self):
        for i in range(1, 6):
            self.__soundPlayer.PlaySound(f"LAUGHTER{i}")


if __name__ == "__main__":
    import time
    laughtPlayer = LaughtPlayer(SoundPlayer())
    laughtPlayer.PlayLaught()
    time.sleep(6)

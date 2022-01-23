from SoundPlayer import SoundPlayer


class LaughtPlayer:
    def PlayLaught(soundPlayer: SoundPlayer):
        for i in range(1, 6):
            soundPlayer.PlaySound(f"LAUGHTER{i}")


if __name__ == "__main__":
    import time
    soundPlayer = SoundPlayer()
    LaughtPlayer.PlayLaught(soundPlayer)
    time.sleep(6)
    del soundPlayer

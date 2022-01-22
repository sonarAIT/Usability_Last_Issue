import numpy as np
import sounddevice as sd  # 録音・再生系のライブラリ
from ttslearn.pretrained import create_tts_engine  # 音声合成ライブラリ
import torch  # 深層学習のライブラリ

SPK2ID = {
    "spk01": "jvs010",
    "spk02": "jvs020",
    "spk03": "jvs030",
    "spk04": "jvs040",
    "spk05": "jvs050",
    "spk06": "jvs060",
    "spk07": "jvs070",
    "spk08": "jvs080",
    "spk09": "jvs090",
    "spk10": "jvs100",
}

class VoicePlayer:
    def PlayVoice(self, text):
        if torch.cuda.is_available():
            DEVICE = torch.device("cuda")
        else:
            DEVICE = torch.device("cpu")
        PWG_ENGINE = create_tts_engine("multspk_tacotron2_hifipwg_jvs24k", device=DEVICE)
        DEFAULT_SPK = "spk01"  # 初期話者
        SPK_ID = PWG_ENGINE.spk2id[SPK2ID[DEFAULT_SPK]]

        # テキストから音声合成
        wavList = []

        for id in ["jvs010", "jvs020", "jvs030", "jvs040", "jvs050"]:
            wav, sr = PWG_ENGINE.tts(text, spk_id=PWG_ENGINE.spk2id[id])
            # 音割れ防止
            wav = (wav / np.abs(wav).max()) * (np.iinfo(np.int16).max / 2 - 1)
            wavList.append(wav)

        # 再生
        for wav in wavList:
            sd.play(wav.astype(np.int16), sr)
            sd.sleep(int(1000 * len(wav) / sr))

if __name__ == "__main__":
    voicePlayer = VoicePlayer()
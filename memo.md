# ユーザビリティ 最終課題
## 要件
ギャグを言うと笑ってくれるアプリケーション
- 音声を入力し，音声を文章に変換(音声認識)
- 入力された文章に「面白さ」をつける
- 「面白さ」に応じてアプリケーションが様々な反応を示す
    - 音声合成などを利用する

## 設計
- 画面
    - ヘッダ
    - メイン
        - 顔
        - テキストラベル
    - ボトム
        - ボタン
- 処理の流れ
    - スタート画面
        - ボタンを押してスタート
    - 音声入力
    - 反応を示す
        - ボタンを押すと音声入力に戻る

## モジュール
- MainProcess
    - メインの流れを制御するモジュール
    - flontScene
    - voiceInputScene
    - resultScene
- UI
    - UIの制御を行うモジュール
    - GetEvent
    - ChangeMainLabel
    - ChangeHeadLabel
    - ChangeFace
- FunnyUtil
    - 面白さの判定を行うモジュール
    - JudgeFunny
- VoicePlayer
    - 音声を再生するモジュール
    - PlayVoice
- VoiceReader
    - 音声を入力するモジュール
    - ReadVoice
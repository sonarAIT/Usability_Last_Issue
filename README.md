# Usability_Last_Issue
ダジャレを聞いて笑ってくれる人工知能アプリケーション

## Setup
```
git clone 
brew install python-tk@3.9 portaudio mecab mecab-ipadic
pip3 install -r requirements.txt
```
また，`mecab-ipadic-neologd`をインストールする必要がある．
https://github.com/neologd/mecab-ipadic-neologd/blob/master/README.ja.md

## Run
```
./launch
```

## Requirements
|言語/FW|Version|
|---|---|
|python|3.9.9|
|python-tk@3.9|3.9.10|
|portaudio|19.7.0|
|MeCab|0.996.3|
|mecab-ipadic|2.7.0-20070801|
|alkana|0.0.3|
|fuzzysearch|0.7.3|
|numpy|1.20.3|
|PyAudio|0.2.11|
|pykakasi|2.2.1|
|PySimpleGUI|4.56.0|
|sounddevice|0.4.4|
|SpeechRecognition|3.8.1|
|torch|1.8.1|
|ttslearn|0.2.2|

## ダジャレ判定スクリプトについて
MIT LICENSEに乗っ取って，vaaaaanquish氏作成の「shareka_v4.py」スクリプトを改変, 利用しています．
https://github.com/vaaaaanquish/dajare-detector/blob/main/shareka/shareka_v4.py

## 効果音素材
OtoLogic(CC BY 4.0)
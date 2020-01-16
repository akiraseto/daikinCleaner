# daikinCleaner
ダイキンの空気清浄機をAppleHomeで制御

# appleWatchから制御できるようにする。
- ON: 加湿モード
- OFF: OFF

# センサー利用
- 室温
- 湿度
- pm25
- dust ホコリ
- ニオイ

## 基本情報取得
/common/basic_info

## センサー取得
/cleaner/get_sensor_info

## コントロール取得
/cleaner/get_control_info

## コントロールする
/cleaner/set_control_info

GETでリクエスト

- pow
- mode
- airvol
- humd

### pow
電源off/on 0/1
powだけの指定でもOK
その場合は、前回の設定で稼働する

それ以外は全パラメータのリクエストが必要

### mode
- 0:風量自動(もしくは風量設定)
- 1:おまかせ
- 2:節電
- 3:花粉
- 4:のど・はだ
- 5:サーキュレーター

### humd
- :OFF
- :ひかえめ
- :標準
- :高め
- :(のど・はだにしている場合)

### airvol
- 0:(mode設定されている場合)
- 1:しずか
- 2:弱
- 3:標準
- 4:-
- 5:ターボ

## タイマー情報
/cleaner/get_scdltimer_body?target=c

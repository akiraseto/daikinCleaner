# daikinCleaner
`ダイキン 加湿ストリーマ空気清浄機 MCK70W`
上記機種をAppleHomeで制御する。

Siri,appleWatch,iPhoneのHomeで操作検証済み。

# API仕様

## 基本情報取得
機種の主な情報、設定したユーザー名や、パスワードなどの取得
`/common/basic_info`

## センサー取得
空気清浄機のセンサー情報を取得
`/cleaner/get_sensor_info`

取得内容

- htemp:室温
- hhum: 湿度
- pm25: PM2.5(空気の汚れ)
- dust: ホコリ
- odor: ニオイ

## タイマー情報
/cleaner/get_scdltimer_body?target=c

## コントロール取得
`/cleaner/get_control_info`

## 機種を制御。コントロールする
GETでリクエスト
`/cleaner/set_control_info`

パラメータは以下の通り

- pow
- mode
- airvol
- humd

### pow
電源(power)パラメータ
off=0, on=1

powパラメータだけの指定でも可。
その場合は、前回の設定で稼働となる。
それ以外は全パラメータのリクエストが必要

### mode
動作モードの選択パラメータ

- 0:風量自動(もしくは風量設定)
- 1:おまかせ
- 2:節電
- 3:花粉
- 4:のど・はだ
- 5:サーキュレーター

### humd
加湿量の設定パラメータ

- 0:OFF
- 1:ひかえめ
- 2:標準
- 3:高め
- 4:(のど・はだモードにしている場合)

### airvol
風量の設定パラメータ

- 0:(mode設定されている場合)
- 1:しずか
- 2:弱
- 3:標準
- 4:-
- 5:ターボ

# プログラム(dsaikinCleaner.py)引数
- off: 空気清浄機をオフ
- max: 風力最大、湿度最大で起動
- hum: 加湿モードで起動

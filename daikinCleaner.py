import sys

import requests

args = sys.argv
if len(args) == 1:
    print('An argument is necessary.')
    exit()
arg = args[1]

# 空気清浄機のIPアドレス
url = 'http://192.168.0.10'

# 基本情報
basic_info = '/common/basic_info'
# センサー取得
get_sensor = '/cleaner/get_sensor_info'

# コントロール取得
get_control = '/cleaner/get_control_info'
# コントロールSET
set_control = '/cleaner/set_control_info'

# 実行したいパラメータのセット
param_off = {'pow': 0}

param_max = {'pow': 1,
             'mode': 0,
             'humd': 3,
             'airvol': 5,
             }

param_hum = {'pow': 1,
             'mode': 4,
             'humd': 4,
             'airvol': 0,
             }


def control(params):
    return requests.get(url + set_control, params)


print('param: ', arg)

if arg == 'off':
    res = control(param_off)
    text = res.text
elif arg == 'max':
    res = control(param_max)
    text = res.text
elif arg == 'hum':
    res = control(param_hum)
    text = res.text
else:
    text = 'nothing'

print('res: ', text)

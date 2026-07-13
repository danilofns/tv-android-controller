from ppadb.client import Client

adb = Client(host="127.0.0.1", port=5037)

devices = adb.devices()

if devices:
    tv = devices[0]
    tv.shell("input keyevent 26")  # Liga/desliga tela
    tv.shell("input keyevent 19")  # Seta para cima
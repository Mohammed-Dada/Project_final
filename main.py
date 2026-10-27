import time
import importlib
import config  

print("بدأ تشغيل النظام الأساسي...")

while True:
    print(config.get_banner())
    print(config.post_banner())

    importlib.reload(config)

    time.sleep(5)
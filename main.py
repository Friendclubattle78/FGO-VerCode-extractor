from libs.python.update import check_update
from libs.python.download import download_latest
from libs.python.decompile import decompile_apk, decrypt
from libs.python.verCode import get_latest_verCode

import sys

if check_update():
    download_latest()
    decompile_apk()
    decrypt()
    get_latest_verCode();
else:
    print('[App] Workflow Canceled!', file=sys.stdout)

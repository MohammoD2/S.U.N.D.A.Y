from datetime import date
import datetime
import random
import sys ,os
sys.path.append(os.path.abspath(os.path.dirname("DATA")))
from DATA.zaki_dlg_dataset.DLG import good_morningdlg, good_afternoondlg, good_eveningdlg, good_nightdlg
from FUNCTION.zaki_speak.speak import speak

today = date.today()
formatted_date = today.strftime("%d %b %y")
nowx = datetime.datetime.now()


def wish():
    current_hour = nowx.hour
    if 5 <= current_hour < 12:
        gd_dlg = random.choice(good_morningdlg)
        speak(gd_dlg)
    elif 12 <= current_hour < 17:
        ga_dlg = random.choice(good_afternoondlg)
        speak(ga_dlg)
    elif 17 <= current_hour < 21:
        ge_dlg = random.choice(good_eveningdlg)
        speak(ge_dlg)
    else:
        gn_dlg = random.choice(good_nightdlg)
        speak(gn_dlg)


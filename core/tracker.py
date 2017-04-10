__author__ = 'a.paoletti'

import os
from datetime import datetime
import ctypes

FILE_ATTRIBUTE_HIDDEN = 0x02


def info():
    user = os.getenv('USERNAME')
    pc = os.getenv('COMPUTERNAME')
    day = datetime.today().strftime("%A")
    time = datetime.now().strftime('%H:%M:%S')
    date = datetime.now().strftime('%d/%m/%Y')

    text = 'Uploaded on {day} {date} at {time}\t\t\tuser: {user} on {pc}\n'.format(
        time=time, day=day, user=user, date=date, pc=pc
    )

    return text


def track_it(file_dir):
    file_name = os.path.join(file_dir, '.track')

    with open(file_name, 'a') as f:
        f.write(info())

    # set the file hidden on windows
    if os.name == 'nt':
        ret = ctypes.windll.kernel32.SetFileAttributesW(file_name, FILE_ATTRIBUTE_HIDDEN)

        if not ret:
            raise ctypes.WinError()

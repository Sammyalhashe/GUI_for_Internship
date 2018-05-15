import time
from datetime import datetime as dt
from multiprocessing import Process

temp_host = r".\host"
host = r"C:\Windows\System32\drivers\etc\hosts"
localhost = '127.0.0.1'

sites = ['www.facebook.com', 'facebook.com', 'www.youtube.com',
         'youtube.com', 'www.twitter.com', 'twitter.com', 'www.espn.com', 'espn.com']


def work_time():
    while dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Work Time...")
        with open(host, 'r+') as fh:
            content = fh.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    fh.write(localhost + ' ' + site + '\n')
        time.sleep(500)
    return False


def free_time():
    while not (dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17)):
        print("Free Time...")
        with open(host, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            for line in lines:
                #print(line, any([site in line for site in sites]))
                if not any([site in line for site in sites]):
                    fh.write(line)
            fh.truncate()
        time.sleep(500)
    return True


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Work Time...")
        with open(host, 'r+') as fh:
            content = fh.read()
            for site in sites:
                if site in content:
                    pass
                else:
                    fh.write(localhost + ' ' + site + '\n')
    else:
        print("Free Time...")
        with open(host, 'r+') as fh:
            lines = fh.readlines()
            fh.seek(0)
            for line in lines:
                #print(line, any([site in line for site in sites]))
                if not any([site in line for site in sites]):
                    fh.write(line)
            fh.truncate()
    time.sleep(500)

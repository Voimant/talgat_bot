from main_db import update_subscription_days, list_username
from db_func import conn
import asyncio
import time

def get_day():
    username_list = list_username()
    print(username_list)
    for username in username_list:
        try:
            update_subscription_days(username)
            conn.commit()
        except TypeError:
            print('ошибку обошел')
            pass



def get_go():
    get_day()

# update_subscription_days()


if __name__ == "__main__":

    while True:
        get_go()
        time.sleep(86400)

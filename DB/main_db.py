import psycopg2
from psycopg2.errorcodes import UNIQUE_VIOLATION
import psycopg2.extras
from DB.db_func import conn


# def add_user(user_name: str, chat_id: int):
#     """
#     Функция проверяет есть пользователь в базе, если нет, записывает в базу
#     :param user_name: user_name пользователя
#     :param chat_id: chat_id пользователя
#     :return: Новый пользователь добавлен или Пользователь с таким user_name уже есть в базе
#     """
#     with conn.cursor() as cur:
#         select_query = """SELECT user_name FROM users WHERE user_name = %s"""
#         cur.execute(select_query, (user_name,))
#         cur.fetchone()
#         if cur.fetchone() is None:
#             try:
#                 insert_query = """UPSERT INTO users(user_name, chat_id)
#                                   VALUES (%s, %s)"""
#                 cur.execute(insert_query, (user_name, chat_id))
#             except UNIQUE_VIOLATION:
#                 return 'Пользователь с таким user_name уже есть в базе'
#         return 'Новый пользователь добавлен'



def add_group_id(id):
    with conn.cursor() as cur:
        insert_query = """INSERT INTO tg_group_id(id)
                            VALUES(%s)
                            ON CONFLICT (id) DO NOTHING"""
        cur.execute(insert_query, (id, ))


# add_group_id(-1001775356070)
# add_group_id(-1001798452123)
# add_group_id(-1001798452123)
# add_group_id(-1001815223396)
conn.commit()


def list_group_id():
    """
    Список групп tg в которых состоит бот
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM tg_group_id""")
        list_1 = [item for i in cur.fetchall() for item in i]
        return list_1




def add_user(user_name: str, chat_id: int):
    """
    Функция проверяет есть пользователь в базе, если нет, записывает в базу
    :param user_name: user_name пользователя
    :param chat_id: chat_id пользователя
    :return: Новый пользователь добавлен или Пользователь с таким user_name уже есть в базе
    """
    with conn.cursor() as cur:
        select_query = """SELECT user_name FROM users WHERE user_name = %s"""
        cur.execute(select_query, (user_name,))
        cur.fetchone()
        if cur.fetchone() is None:
            insert_query = """INSERT INTO users(user_name, chat_id)
                                   VALUES(%s, %s)
                                   ON CONFLICT (user_name) DO NOTHING"""
            cur.execute(insert_query, (user_name, chat_id))
            # except UNIQUE_VIOLATION:
            #     return 'Пользователь с таким user_name уже есть в базе'
        return 'Новый пользователь добавлен'


us_name = 'Cate'
us_chat_id = 3333333333333
# print(add_user(us_name, us_chat_id))
conn.commit()





def list_chat_id():
    """
    Функция выдаёт список chat_id пользователей
    :return: список chat_id пользователей
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT chat_id FROM users""")
        list_1 = [item for i in cur.fetchall() for item in i]
        return list_1

def list_username():
    """
    Функция выдаёт список chat_id пользователей
    :return: список chat_id пользователей
    """
    with conn.cursor() as cur:
        cur.execute("""SELECT user_name FROM users""")
        list_1 = [item for i in cur.fetchall() for item in i]
        return list_1


# print(list_chat_id())


def add_data(user_name: str, text: str, media: str, link: str, subscription_days: int, chat_id: int):
    """
    Функция заполнения таблицы данных по подписке
    :param chat_id:
    :param user_name: user_name пользователя
    :param text: текст
    :param media: изображение
    :param link: ссылка
    :param subscription_days: количество дней подписки
    :return:
    """
    with conn.cursor() as cur:
        insert_query = """INSERT INTO data_subscriptions(user_name, text, media, link, subscription_days, chat_id)
                                          VALUES (%s, %s, %s, %s, %s, %s)"""
        cur.execute(insert_query, (user_name, text, media, link, subscription_days, chat_id))
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        a = list(cur.fetchone())
        return f'Подписка оформлена {a} на дней'


us_name = 'Asya'
us_text = 'zdvd ggnghh hfthfth'
us_media = 'hgbwwwwwwwwwwwww'
us_link = 'qqqqqqqqqqqqqqqqqqq'
us_sub_days = 7
# print(add_data(us_name, us_text, us_media, us_link, us_sub_days))
conn.commit()


def add_data_two(user_name: str, text: str, subscription_days: int, chat_id: int):
    """
    Функция заполнения таблицы данных по подписке
    :param chat_id:
    :param subscription_days:
    :param user_name: user_name пользователя
    :param text: текст
    :return:
    """
    with conn.cursor() as cur:
        insert_query = """INSERT INTO data_subscriptions(user_name, text, subscription_days, chat_id)
                                          VALUES (%s, %s, %s, %s)"""
        cur.execute(insert_query, (user_name, text, subscription_days, chat_id))
        # cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        # a = list(cur.fetchone())
        return f'данные внесены'


def update_post_1(user_name: str, text: str, media: str, link: str, chat_id: int):
    """
    Функция заполнения таблицы данных по подписке
    :param chat_id:
    :param user_name: user_name пользователя
    :param text: текст
    :param media: изображение
    :param link: ссылка
    :return:
    """
    with conn.cursor() as cur:
        insert_query = """UPDATE data_subscriptions
        SET
        user_name = %s,
        text = %s,
        media = %s,
        link = %s,
        chat_id = %s
        WHERE user_name = %s"""
        cur.execute(insert_query, (user_name, text, media, link, chat_id, user_name))
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        a = list(cur.fetchone())
        return f'Подписка оформлена {a} на дней'


us_name = 'Asya'
us_text = 'zdvd ggnghh hfthfth'
us_media = 'hgbwwwwwwwwwwwww'
us_link = 'qqqqqqqqqqqqqqqqqqq'
us_sub_days = 7
# print(add_data(us_name, us_text, us_media, us_link, us_sub_days))
conn.commit()


def update_post_two(user_name: str, text: str, chat_id: int, media: str):
    """
    Функция заполнения таблицы данных по подписке
    :param media:
    :param chat_id:
    :param user_name: user_name пользователя
    :param text: текст
    :return:
    """
    with conn.cursor() as cur:
        insert_query = """UPDATE data_subscriptions
        SET
        user_name = %s,
        text = %s,
        media = %s,
        chat_id = %s
        WHERE user_name = %s"""
        cur.execute(insert_query, (user_name, text, media, chat_id, user_name))
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        a = list(cur.fetchone())
        return f'Подписка оформлена {a} на дней'


def update_subscription_days(user_name: str):
    """
    Функция уменьшает количество дней подписки на 1 и, если число равняется нулю, удаляет информацию по подписке.
    :param user_name: user_name пользователя
    :return: До окончания подписки осталось (количкство) дней
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE data_subscriptions SET subscription_days = subscription_days - 1 WHERE user_name = %s""", (user_name,))
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        a = list(cur.fetchone())
        cur.execute("""DELETE FROM data_subscriptions WHERE subscription_days = 0""")
        return f'До окончания подписки осталось {a} дней'


def update_new_subs(user_name: str, subscription_days: int):
    """
    Функция уменьшает количество дней подписки на 1 и, если число равняется нулю, удаляет информацию по подписке.
    :param subscription_days:
    :param user_name: user_name пользователя
    :return: До окончания подписки осталось (количкство) дней
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE data_subscriptions SET subscription_days = subscription_days + %s WHERE user_name = %s""",(subscription_days, user_name))
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        a = list(cur.fetchone())
        cur.execute("""DELETE FROM data_subscriptions WHERE subscription_days = 0""")
        return f'До окончания подписки осталось {a} дней'


us_name = 'Asya'
# print(update_subscription_days(us_name))
conn.commit()


def data_output_subs():
    """
    Функция выводит информацию из таблицы data_subscriptions
    :return: список словарей из таблицы data_subscriptions
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT * FROM data_subscriptions""")
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list

def data_day_subs(user_name):
    """
    сколько осталось дней подпискиdata_subscriptions
    :return: список словарей из таблицы data_subscriptions
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT subscription_days FROM data_subscriptions WHERE user_name = %s""", (user_name,))
        res = list(cur.fetchone())
        return res



#print(data_output())


def data_output_users():
    """
    Функция выводит информацию из таблицы users
    :return: список словарей из таблицы users
    """
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""SELECT * FROM users""")
        res = cur.fetchall()
        res_list = [dict(row) for row in res]
        return res_list


def insert_subscription_days(user_name: str, subscription_days: int):
    """
    Функция записи в таблицу количества дней подписки
    :param user_name: имя пользователя, оформившего подписку
    :param subscription_days: количество дне подписки
    :return: Количество дней подписки записано в таблицу
    """
    with conn.cursor() as cur:
        cur.execute("""UPDATE data_subscriptions SET subscription_days = subscription_days + %s WHERE user_name = %s""",
                    (subscription_days, user_name))
        return 'Количество дней подписки записано в таблицу'


us_sub_days = 7
us_name = 'Cate'
#print(insert_subscription_days(us_name, us_sub_days))
conn.commit()


def db_del_post(post_id):
    """Удаляем по chat_id пост"""
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM data_subscriptions WHERE chat_id = {}""").format(int(post_id))
        conn.commit()
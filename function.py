from SQdb import *
import requests as inet
import json

url_region = 'https://namaztimes.kz/ru/api/states?id={}'
url_city = 'https://namaztimes.kz/ru/api/cities?id={}'
url_time = 'https://namaztimes.kz/api/praytimes?id={}'
db = SQdb('country.db')


def get_dic_country(name):
    row = db.exfetchone(f"SELECT * FROM countries WHERE name='{name.lower()}'")
    if row is None:
        return False
    else:
        return row
def get_api_reg(reg):
    x = inet.get(url_region.format(reg))
    x = json.loads(x.text)
    return x
def get_api_city(city):
    x = inet.get(url_city.format(city))
    x = json.loads(x.text)
    return x
def get_api_time(city):
    try:
        x = inet.get(url_time.format(city))
        x = json.loads(x.text)
        text = f"""
        Сегодня:
        📆 ⛪По  Григорянскому кал. {x['date']}
        📆 🕌По Мусульманскому кал. {x['islamic_date']}
        ======================
        🕰️🕋Времена намаз:
        🌄Фаджр - {x['praytimes']['bamdat']}
        🏜️Зухр - {x['praytimes']['besin']}
        🏙️Аср - {x['praytimes']['asriauual']}
        🌆Магриб - {x['praytimes']['ishtibaq']}
        🌃Иша - {x['praytimes']['quptan']}
        ======================
        Дополнительные молитвы :
        Ишрак - {x['praytimes']['ishraq']}
        Тахаджуд - {x['praytimes']['ishaisani']}
        ======================
        🕰️ Времена:
        🌄Восход - {x['praytimes']['kun']}
        🌇Закат - {x['praytimes']['aqsham']}"""
        return text
    except error as e:
        text = 'Ошибка повторите позже\n Код ошибки:', e
        return text

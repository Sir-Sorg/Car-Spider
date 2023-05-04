import sqlite3

connection = sqlite3.connect("cars_db.sqlite")
cursor = connection.cursor()


def preProcess(data: list):
    dataSet = list()
    for info in data:
        if info['type'] == 'banner':
            continue
        if len(info['price']['price']) <= 2:
            continue
        car = {'COLOR': info['detail']['body_color'],
               'KM_RUNNING': info['detail']['mileage'],
               'FUEL': info['detail']['fuel'],
               'GEAR': info['detail']['transmission'],
               'YEAR': info['detail']['year'],
               'MODEL': info['detail']['title'],
               'BODY_CONDITION': info['detail']['body_status'],
               'PRICE': info['price']['price']}
        dataSet.append(car)
    return dataSet


def save(data: list):
    cursor.execute('DELETE FROM INFO_CAR;')
    query = '''INSERT INTO INFO_CAR (COLOR, KM_RUNNING, FUEL, GEAR, YEAR, MODEL, BODY_CONDITION, PRICE)
                VALUES (%s,%i,%i,%i,%i,%s,%i,%i);'''
    cursor.execute(query, ())

import sqlite3


def preProcess(data: list):
    dataSet = list()
    for info in data:
        if info['type'] == 'banner':
            continue
        if len(info['price']['price']) <= 2:
            continue
        car = {'COLOR': info['detail']['body_color'],
               'KM_RUNNING': info['detail']['mileage'].replace(' کیلومتر', '').replace(',', ''),
               'FUEL': info['detail']['fuel'],
               'GEAR': info['detail']['transmission'],
               'YEAR': info['detail']['year'],
               'MODEL': info['detail']['title'],
               'BODY_CONDITION': info['detail']['body_status'],
               'PRICE': info['price']['price'].replace(',', '')}
        dataSet.append(car)
    return dataSet


connection = sqlite3.connect("cars_db.sqlite")
cursor = connection.cursor()


def save(cars: list):
    counter = 0
    print('Conecting to Database\nSaving Started...')
    cursor.execute('DELETE FROM INFO_CAR;')
    connection.commit()
    query = '''INSERT INTO INFO_CAR (COLOR, KM_RUNNING, FUEL, GEAR, YEAR, MODEL, BODY_CONDITION, PRICE)
                VALUES (?,?,?,?,?,?,?,?);'''
    for car in cars:
        value = (car['COLOR'], car['KM_RUNNING'], car['FUEL'], car['GEAR'],
                 car['YEAR'], car['MODEL'], car['BODY_CONDITION'], car['PRICE'])
        cursor.execute(query, value)
        connection.commit()
        counter += 1

    cursor.close()
    print(f'{counter} items saved in database')

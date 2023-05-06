import sqlite3
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn import preprocessing

connection = sqlite3.connect("cars_db.sqlite")
cursor = connection.cursor()


def standardization(model):
    scaler = preprocessing.StandardScaler()
    scaler.fit(model)
    STD_data = scaler.transform(model)
    return STD_data


def dummy_variables(data):
    for column in [0, 2, 3, 5, 6]:
        featureStatus = set(data[:, column])
        tranasformer = preprocessing.LabelEncoder()
        tranasformer.fit(list(featureStatus))
        data[:, column] = tranasformer.transform(data[:, column])
    data = data.astype(int)
    return data


def read_data():
    query = 'SELECT * FROM INFO_CAR LIMIT 200'
    dataSet = list(cursor.execute(query))
    dataSet = list(filter(lambda x: type(x[2]) == int, dataSet))
    dataSet = np.array(dataSet)
    
    # remove ID Column of data
    dataSet = dataSet[:, 1:]

    return dataSet


def predict(userInput:list):
    # read data from Database and splite feture and lbale
    dataSet = read_data()
    X, Y = dataSet[:, :-1], dataSet[:, -1]

    # add user input into data and numberize & standarding its value
    X = np.vstack([X, userInput])
    X = dummy_variables(X)
    X = standardization(X)
    Y = Y.astype(int)

    # Splite user input from data set
    userInput = [X[-1, :]]
    X = X[:-1, :]

    # Train knn regresion model
    neigh = KNeighborsRegressor(n_neighbors=5)
    neigh.fit(X, Y)

    # predict price of the car
    y_hat = neigh.predict(userInput)
    y_hat = y_hat.astype(int)[0]
    y_hat = (y_hat // 100000)*100000

    # return the value of price
    print(f'Best Value for your car is "{y_hat}" toman')
    return y_hat

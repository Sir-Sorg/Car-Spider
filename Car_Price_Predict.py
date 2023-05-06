import Spider
import Storage
import Foreteller


def regression_preparation(Y: list):
    data = Spider.scraper()
    data = Storage.preProcess(data)
    Storage.save(data)
    price = Foreteller.predict(Y)
    return price
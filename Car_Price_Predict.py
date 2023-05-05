import Spider
import Storage

data = Spider.scraper()
data = Storage.preProcess(data)
Storage.save(data)

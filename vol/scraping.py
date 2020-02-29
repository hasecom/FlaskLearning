from bs4 import BeautifulSoup
import requests

class Scraping:
    __SCRAPING_URL = "https://5ch.net/"
    __output = []
    def collectData(self):
        res = requests.get(self.__SCRAPING_URL)
        soup = BeautifulSoup(res.content, "html.parser")
        items = soup.select(".thread_title")
        self.__output = []
        for item in items:
            self.__output.append(item.get_text())
        return self.__output
import requests
import json
import logging

LOGGER = logging.getLogger()


class SenderLink:

    """Метод для парсинга данных и формирования ссылки"""
    @staticmethod
    def creating_link(data, link):
        url = "https://nominatim.openstreetmap.org/"
        parametrs = {"accept-language": "ru", "format": "jsonv2"}

        if link == "search":
            url += "search"
            parametrs.update({"q": data["address"], })

        elif link == "reverse":
            url += "reverse"
            parametrs.update({"lat": data["lat"], "lon": data["lon"], })

        return url, parametrs

    """Метод для отправления запроса"""
    def sending_request(self, data, link):
        query = self.creating_link(data, link)
        url = query[0]
        parametrs = query[1]
        response = requests.get(url, params=parametrs)
        try:
            LOGGER.debug("Отправлен запрос на url: {url} ""с параметрами: {query}".format(url=url, query=parametrs))
            response = requests.get(url, params=parametrs)
            LOGGER.debug("Получен ответ от сервера: {status}, {text}".format(status=response.status_code, text=response.text))
            assert response.status_code == 200, ("Ответ сервера {status} != 200".format(status=response.status_code))
        except requests.Timeout:
            LOGGER.debug("Превышено время ожидания ответа от сервера")
        return response


def data_link(file_name):
    with open(file_name) as file:
        return json.loads(file.read())

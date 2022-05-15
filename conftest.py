import pytest
import requests
import logging
import json


LOGGER = logging.getLogger(__name__)


class SenderLink:

    #Метод для парсинга данных и формирования ссылки
    def creating_link(self, data, link):
        url = "https://nominatim.openstreetmap.org/"
        parametrs = {"accept-language": "ru", "format": "jsonv2"}

        if link == "search":
            url += "search"
            parametrs.update({"q": data["address"], })

        elif link == "reverse":
            url += "reverse"
            parametrs.update({"lat": data["lat"], "lon": data["lon"], })
        return url, parametrs

    #Метод для отправления запроса
    def sending_request(self, data, link):
        query = self.creating_link(data, link)
        url = query[0]
        parametrs = query[1]
        response = requests.get(url, params=parametrs)
        return response


def get_testing_data(file_name):
    with open(file_name) as file:
        return json.loads(file.read())


@pytest.fixture(params=get_testing_data("data_straight.json"))
def data_straight(request):
    return request.param


@pytest.fixture(params=get_testing_data("data_reverse.json"))
def data_reverse(request):
    return request.param


@pytest.fixture
def logger():
    return LOGGER


@pytest.fixture(scope="module")
def sender():
    sender_link = SenderLink()
    return sender_link

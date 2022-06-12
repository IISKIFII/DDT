import pytest
import allure
from .sender_link import data_link


@allure.feature("Тестирование прямого запроса")
@allure.severity(allure.severity_level.BLOCKER)
@allure.link('https://nominatim.org/release-docs/latest/api/Overview/', name='API Click me')
@allure.description("""
Тест проверяет соответствие введенного адреса координатам
полученным в ответе от сервера.
""")
@pytest.mark.nominatim
@pytest.mark.parametrize('data_straight', data_link("data_straight.json"))
def test_straight_address(sender, data_straight, logger):
    error = "В ответе сервера нет ожидаемой координаты - {value}"
    lat = data_straight["lat"]
    lon = data_straight["lon"]
    with allure.step("Запрос к серверу и получение ответа"):
        response = sender.sending_request(data_straight, "search")
    with allure.step("Сравнение ожидаемого результата с фактическим"):
        for item in (lat, lon):
            if item not in response.text:
                logger.debug(error.format(value=item))
            assert item in response.text, error.format(value=item)


@allure.feature("Тестирование обратного запроса")
@allure.severity(allure.severity_level.BLOCKER)
@allure.link('https://nominatim.org/release-docs/latest/api/Overview/', name='API Click me')
@allure.description("""
Тест проверяет соответствие введенных координат полученному от сервера адресу.
""")
@pytest.mark.nominatim
@pytest.mark.parametrize('data_reverse', data_link("data_reverse.json"))
def test_reverse_address(sender, data_reverse, logger):
    error = "В ответе сервера нет ожидаемого адреса - {address}"
    address = data_reverse["address"]
    with allure.step("Запрос к сереверу и получение ответа"):
        response = sender.sending_request(data_reverse, "reverse")
    with allure.step("Сравнение ожидаемого результата с фактическим"):
        if address not in response.text:
            logger.debug(error.format(address=address))
        assert address in response.text, error.format(address=address)

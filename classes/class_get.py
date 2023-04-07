from .class_base_page_API import BasePageApi
import requests

class GET_REQUEST(BasePageApi):
    def get_request_OK(link, answer):
        get = requests.get(link, verify =False)
        assert get.status_code == 200, 'сообщение не доставлено'
        assert str(get.json()) == answer, 'тело ответа некорректно'

    def get_request_404(link, answer):
        get = requests.get(link, verify =False)
        assert get.status_code == 404, 'Неверный код ошибки'
        assert str(get.json()) == answer, 'тело ответа некорректно'



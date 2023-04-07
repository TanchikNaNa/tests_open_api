import pytest
from classes.class_main_page_WEB import MainPage
import requests 


class TestLoginFromMainPage:
    def test_web_LIST_USERS(self, browser):
        link = "https://reqres.in/"
        page = MainPage(browser, link)
        page.open()
        status_code_web, ans_json_web = page.web_get_list_users()
        get = requests.get('https://reqres.in/api/users?page=2', verify =False)
        assert  get.status_code == int(status_code_web), 'статус код не совпадают на web и api'
        json_API = str(get.json())
        json_API1 = json_API.replace(" ", "")
        json_API2 = json_API1.replace("\n","")
        json_API3 =json_API2.replace("'", "!")
        assert json_API3 == ans_json_web, 'тело ответа не совпадают на web и api'
        
  


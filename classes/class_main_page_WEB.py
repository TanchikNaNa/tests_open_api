from .class_base_page_WEB import BasePageWeb
from locators import MainPageLocators
from jsons.jsons_for_get import class_jsons_for_get 

class MainPage(BasePageWeb):
    def web_get_list_users(self):
        button = self.browser.find_element(*MainPageLocators.LIST_USERS_BUTTON)
        button.click()
        code_ans_web = self.browser.find_element(*MainPageLocators.LIST_USERS_CODE_ANS)
        ans_code = code_ans_web.text
        assert ans_code == '200', 'Сообщение не доставлено'
        json_ans_web = self.browser.find_element(*MainPageLocators.LIST_USERS_JSON)
        ans_json_from_web = json_ans_web.text
        ans_json_from_web1 = ans_json_from_web.replace(" ", "")
        ans_json_from_doc1 = class_jsons_for_get.body_LIST_USERS.replace(" ", "")
        ans_json_from_web2 = ans_json_from_web1.replace("\n","")
        ans_json_from_doc2 = ans_json_from_doc1.replace("\n","")
        ans_json_from_web3 = ans_json_from_web2.replace('"', '!')  
        ans_json_from_doc3 = ans_json_from_doc2.replace("'", "!")  
        assert ans_json_from_web3 == ans_json_from_doc3, 'тело ответа некорректно'
        return ans_code, ans_json_from_web3


    






from selenium.webdriver.common.by import By

class MainPageLocators:
    LIST_USERS_BUTTON = (By.CSS_SELECTOR, '[data-id="users"]')
    LIST_USERS_JSON = (By.XPATH, '/html/body/div[2]/div/div/section[1]/div[2]/div[2]/pre')
    LIST_USERS_CODE_ANS = (By.CSS_SELECTOR, '.response-code')
    

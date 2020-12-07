from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_check_button_add_to_cart(browser):
    browser.get(link)
    button = WebDriverWait(browser, 5).until( EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-add-to-basket")))


    

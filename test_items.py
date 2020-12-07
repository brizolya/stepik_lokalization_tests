import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(button) == 1, "Only one button expected!"
    


    

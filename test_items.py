from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_is_element_exists(browser):

    browser.get(link)
    #time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "form#add_to_basket_form>button[type='submit']")
    assert button, "корзинка не найдена"
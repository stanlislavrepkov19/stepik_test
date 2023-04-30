import 
pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):

    def test_reg1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstname = browser.find_element(By.CSS_SELECTOR,
                                         "body > div > form > div.first_block > div.form-group.first_class > input")
        firstname.send_keys("Potter")
        lastname = browser.find_element(By.CSS_SELECTOR,
                                        "body > div > form > div.first_block > div.form-group.second_class > input")
        lastname.send_keys("Harry")
        email = browser.find_element(By.CSS_SELECTOR,
                                     "body > div > form > div.first_block > div.form-group.third_class > input")
        email.send_keys("harry.potter@mail.ru")
        phone = browser.find_element(By.CSS_SELECTOR,
                                     "body > div > form > div.second_block > div.form-group.first_class > input")
        phone.send_keys("+79510959868")
        address = browser.find_element(By.CSS_SELECTOR,
                                       "body > div > form > div.second_block > div.form-group.second_class > input")
        address.send_keys("London, Jameson str. 21p1")

        submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        submit.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text


        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(3)
        browser.quit()

    def test_reg2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstname = browser.find_element(By.CSS_SELECTOR,
                                         "body > div > form > div.first_block > div.form-group.first_class > input")
        firstname.send_keys("Potter")
        lastname = browser.find_element(By.CSS_SELECTOR,
                                        "body > div > form > div.first_block > div.form-group.second_class > input")
        lastname.send_keys("Harry")
        email = browser.find_element(By.CSS_SELECTOR,
                                     "body > div > form > div.first_block > div.form-group.third_class > input")
        email.send_keys("harry.potter@mail.ru")
        phone = browser.find_element(By.CSS_SELECTOR,
                                     "body > div > form > div.second_block > div.form-group.first_class > input")


ЭТО ТЕСТ через unittest и PyTest 
Задаие 3.3
        phone.send_keys("+79510959868")
        address = browser.find_element(By.CSS_SELECTOR,
                                       "body > div > form > div.second_block > div.form-group.second_class > input")
        address.send_keys("London, Jameson str. 21p1")

        submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
        submit.click()

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(3)
        browser.quit()

if "main" == name:
    unittest.main()
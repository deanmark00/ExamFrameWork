from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.loginPage import LoginPage
from Pages.mainPage import MainPage
import HtmlTestRunner


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = "C:/Users/denma/PycharmProjects/ExamFrameWork/drivers/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def test_mainPageTitle(self):
        driver = self.driver
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        main_page_title = self.driver.title
        if main_page_title == "OWASP Juice Shop":
            assert True
        else:
            self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_mainPageTitle.png")
            assert False


    def test_login_valid(self):
        driver = self.driver

        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage = MainPage(driver)
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        time.sleep(2)
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_login_valid.png")


    def test_logout(self):
        driver = self.driver
        self.driver.get("http://139.99.96.214:3000/#/search")
        self.driver.find_element_by_xpath("//body//mat-dialog-container//button[2]").click()
        mainpage = MainPage(driver)
        mainpage.account_button()
        mainpage.account_login()
        login = LoginPage(driver)
        login.enter_email("test@test.com")
        login.enter_password("abcd1234")
        login.click_login()
        mainpage.account_button()
        mainpage.account_logout()
        time.sleep(2)
        self.driver.save_screenshot("C:/Users/denma/PycharmProjects/ExamFrameWork/Screenshots" + "test_logout_valid.png")

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
        print("Test Complete")

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/denma/PycharmProjects/ExamFrameWork/Reports'))

